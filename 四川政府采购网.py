#!/usr/bin/env python
#--*-- coding:utf-8 --*--

from ctypes import windll
import requests
from lxml import etree
import sqlite3
import os

cont=0



def getItemName(page):
    proxiexurl ='113.141.222.35'
    proxiexport = '9999'
    proxies = {'http://':proxiexurl+':'+proxiexport,'https://':proxiexurl+':'+proxiexport}
    url ='http://www.ccgp-sichuan.gov.cn/CmsNewsController.do?method=recommendBulletinList&rp=25&page='+str(page)+'&moreType=provincebuyBulletinMore&channelCode=sjcg1'
    headler={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"

    }
    data ={
    "method": "recommendBulletinList",
    "rp": "25",
    "page":str(page),
    "moreType": "provincebuyBulletinMore",
    "channelCode": "sjcg1",
    }
    respose = requests.get(url=url,headers=headler)
    print(respose)
    with open("mytemp.html",'w',encoding='utf-8') as fp:
        fp.write(respose.text)
    return remenber(parserUrl(),getOneIteByName())

def parserUrl():
    tree = etree.parse('mytemp.html',parser=etree.HTMLParser())
    r = tree.xpath("//a[@target='_blank']//@href")
    return r


def getOneIteByName():
    tree = etree.parse('mytemp.html',parser=etree.HTMLParser())
    r = tree.xpath("//a[@target='_blank']//@title")
    return r

def remenber(urlg,urlname):
    pageCont=0
    it =iter(urlg)
    it1 = iter(urlname)
    with open('recv.txt',mode='a',encoding='utf-8') as fp:
        for urls in it:
            for urlname in it1:
                fp.write("\r"+str(pageCont+1)+"\r"+urlname+urlname+"\r"+urls+"\r")
                pageCont+=1
                try:
                    addBaseTableData(pageCont+cont*25,"'"+urlname+"'","'"+urls+"'")   
                except:
                    print("加入数据库失败")                
    return pageCont
        # fp.write("到这共有"+str(pageCont-1)+"条数据")

def rcvAllPageMessege(page):
    PageNu=0
    global cont
    with open('recv.txt','w',encoding='utf-8') as fp:
        fp.write("      四川采购网信息     ")         
    for x in range(1,page+1):
        PageNu = PageNu + getItemName(x)
        cont=cont+1
        print("已经爬取了%s条项目"%PageNu)
    with open('recv.txt','a',encoding='utf-8') as fp:
        fp.write("\r\n共有"+str(PageNu)+"条数据")



def creatBaseTable(tablename,):
    try:
        cz = os.path.exists('text.db')
        if not cz:
            with open('text.db') as fp:
                pass50
        else:
            pass
    except:
        pass
    conn = sqlite3.connect(database='text.db')
    c = conn.cursor()
    try:
        c.execute('DROP TABLE '+str(tablename))             #删除之前的表
    except:
        pass

    try:
        c.execute("create table "+tablename+"(ID int primary key NOT NULL,ProjectName text,Url text)")
        print("创建表biao1成功")
        conn.commit()    
    except sqlite3.OperationalError:
        print("已经创建了该表:biao1")
    conn.close()

def addBaseTableData(id,name,url):
    conn = sqlite3.connect(database='text.db')
    c = conn.cursor()    
    try:
        print("INSERT INTO biao1 VALUES ("+str(id)+","+name+","+url+")")        
        c.execute("INSERT INTO biao1 VALUES ("+str(id)+","+name+","+url+")")

        print("加入数据成功")
        conn.commit()    
    except sqlite3.OperationalError:
        print("加入数据失败")   
    conn.close()


if __name__ =="__main__":
    creatBaseTable("biao1")
    pagenu = input("请输入爬取页面数最大不超过400:")
    rcvAllPageMessege(int(pagenu))





    









