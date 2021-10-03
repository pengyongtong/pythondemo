import requests

url1="http://192.168.3.12/ac_portal/default/pc.html?template=default&tabs=pwd&vlanid=4093&url=http://www.msftconnecttest.com%2fredirect"

headler={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"

}


def login_text(url):
    sta = requests.get(url,headers=headler).status_code
    if sta ==200:
        return 1
    else:
        return 0

def login(user,passwd):
    url ="http://192.168.3.12/ac_portal/login.php"
    data ={
        "opr": "pwdLogin"
        "userName": user
        "pwd": passwd
        "auth_tag": "1632882585072"
        "rememberPwd": "0"      


    }
    sta = requests.post(url=url,data=data,headers=headler).status_code
    if sta ==200:
        return 1
    else:
        return 0

user = "19234037"
passwd = "513021200003265313"

if __name__ =="__main__":
    if login_text(url1)==1:
        if login_text()==1:
            print("登录成功")
        else:
            print("登录失败")             
    else:
        print("未能在登录页面")
