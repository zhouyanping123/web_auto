import unittest
from common import HTMLTestRunner_cn
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os,sys

def send_mail(sender,psw,receiver,smtpserver,report_file,port):
    with open(report_file,"rb") as f:
        mail_body = f.read()
    #定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['Subject'] = "自动化测试报告"
    msg["from"] = sender
    if isinstance(receiver,str):
        msg["to"] = receiver
    if isinstance(receiver,list):
        msg["to"] = ",".join(receiver)
    msg.attach(body)
    #添加附件
    att = MIMEText(open(report_file,"rb").read(),"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposotion"] = 'attachment; filename="result.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(sender,psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver,port)
        smtp.login(sender,psw)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()

if __name__ == "__main__":
    #用例的路径
    casePath = "F:\study\web_auto\case"
    rule = "test*.py"
    discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)

    reportPath = "F:\\study\\web_auto\\report\\"+"result.html"
    fp = open(reportPath,'wb')
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                              title='报告的title',
                                              description="描述")

    runner.run(discover)
    fp.close()
    propath = os.path.dirname(os.getcwd())
    print(propath)
    # file_path = os.path.join(propath, "report","result.html")
    file_path = "F:\\study\\web_auto\\report\\"+"result.html"
    sender = "zyp272458867@163.com"
    psw = "abc19910515"
    smtp_server = "smtp.163.com"
    port = 465
    receiver = "272458867@qq.com"
    send_mail(sender,psw,receiver,smtp_server,file_path,port)