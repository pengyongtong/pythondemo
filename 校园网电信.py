#!/usr/bin/python3

import requests
from requests.api import post
from requests.models import Response
from requests.sessions import session

url ="http://172.16.3.2/a70.htm"
url1 = 'http://172.16.3.2:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=172.16.3.2&iTermType=1&mac=000000000000&ip=10.0.1.134&loginMethod=1'
headler ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
login_userlist=["19138591243@dx","19161568244@dx"]
login_paswdlist=["16608220460...","123456"]



def loginStart(user,paswd):
    postdata={
        "DDDDD": user,
        "upass": paswd,
        "R1": "0",
        "R2": "0",
        "R6": "0",
        "para": "00",
        "0MKKey": "123456",
        "buttonClicked":"",
        "redirect_url":"" ,
        "err_flag":"" ,
        "username":"",
        "password":"" ,
        "user":"",    

    }
    userlt =iter(user)
    paswdlt =iter(paswd)
    Response = requests.get(url=url,headers=headler)
    for user in userlt:
        for paswd in paswdlt:
            if Response.status_code==200:
                postdata['DDDDD']=str(user)
                postdata['upass']=str(paswd)
                Response1 =   requests.post(url=url1,data=postdata,headers=headler)
            if Response1.status_code==200:
                print("登录成功")
                return 1
            else:
                print("登录失败")
    return 0





if __name__ =='__main__':
    loginStart(login_userlist,login_paswdlist)
    

