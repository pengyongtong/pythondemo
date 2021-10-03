#--*-- coding:utf-8 --*--

import requests
from lxml import etree
import re
import sqlite3
import os


imgcont=0
# https://pic.netbian.com/4kmeinv/index_2.html
urlmain="https://pic.netbian.com"
url ="https://pic.netbian.com/4kmeinv/"
headler ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
cont=0

def getpage(nu):
    orderUrl=''
    if nu==1:
        # print(url)
        orderUrl =url
    else:
        # print(url+"index_{}.html".format(nu))
        orderUrl =url+"index_{}.html".format(nu)
    Response=requests.get(url=orderUrl,headers=headler)
    Response.status_code='gbk'
    Response.encoding='gbk'                
    with open("meilv.html",'w') as fp:
        fp.write(Response.text)    
    # print("get url page ok")


def parseURL():
    conn = etree.parse("meilv.html",etree.HTMLParser())
    urllist = conn.xpath("//a[@target='_blank']//img//@src")
    return urllist       
def parseImagName():
    conn = etree.parse("meilv.html",etree.HTMLParser())
    namelist = conn.xpath("//a[@target='_blank']//img//@alt")
    return namelist       





def CreatNewBase():
    try:
        os.remove("./img/meilv.db")
        with open("./img/meilv.db",'wb') as fp:
            pass
    except:
        pass

    try:
        conn = sqlite3.connect("./img/meilv.db")
        print("连接数据库成功")
        c = conn.cursor()
    except:
        print("连接数据库失败")
    try:
        c.execute("DROP TABLE biao1")
        conn.commit()
        print("删除旧表成功")
        c.execute("create table biao1(ID PRIMARY KEY,NAME TEXT,URL TEXT)")
        conn.commit()
        print("创建新表成功\r\n")             
    except:
        c.execute("create table biao1(ID PRIMARY KEY,NAME TEXT,URL TEXT)")
        conn.commit()
        print("创建新表成功\r\n")         
    c.close()
    conn.close()



def downURLImg(url,name):
    img = requests.get(url)
    # print("/img/{}".format(name))
    with open("./img/{}".format(name),'wb') as fp:
        fp.write(img.content)

def parseData(urls,names):
    global cont
    pattern = re.compile('\d*-.*')
    urlitr = iter(urls)
    namesitr = iter(names)
    for urlnu in urlitr:
        for namenu in namesitr:
            urlhe =urlmain+urlnu
            try:
                downURLImg(urlhe,pattern.search(urlnu).group(0))
                rcvDataBase(namenu,urlnu)
                cont=cont+1 
            except:
                # downURLImg(urlhe,str(cont)+'.jpg')
                print("无用图片丢弃")
            break   
        print("\r已下载第{}张".format(cont))


def rcvDataBase(name,urls):
    global cont
    try:
        conn = sqlite3.connect("./img/meilv.db")
        c = conn.cursor()
    except:
        print("连接数据库失败")    
    c.execute("insert into biao1 values ({},'{}','{}')".format(cont+1,str(name),urlmain+str(urls)))
    conn.commit()
    c.close()
    conn.close()





def downManyImg(nu):
    for pagenu in range(1,nu+1):
        getpage(pagenu)
        parseData(parseURL(),parseImagName())







def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".jpg"):
                os.remove(os.path.join(root, name))
                # print ("Delete File: " + os.path.join(root, name))



  


if __name__=="__main__":
    del_files('./img')
    CreatNewBase()
    nu = input("请输入要抓取的页数:")
    downManyImg(int(nu))
    downManyImg(2)
    # # getpage(1)
    # # print(parseURL())

    



    
