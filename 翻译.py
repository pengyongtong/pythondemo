import json
import requests


headler ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}

if __name__=="__main__":
    post_url = "https://fanyi.baidu.com/sug"
    text = input("请输入")
    data ={
        "kw": text

    }
    
    Response = requests.post(url=post_url,data=data,headers=headler)
    dic_obj = Response.json()
    print(dic_obj)
    
    fp = open("a.txt",'w',encoding="utf-8")
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print("over!!!")



