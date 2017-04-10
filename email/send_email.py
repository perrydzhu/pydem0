import smtplib

from_addr = "ski2per@163.com"
to_addr = "67784480@qq.com"

# smtp_server = smtplib.SMTP("smtp.163.com", port=25)
smtp = smtplib.SMTP()
smtp.connect("smtp.163.com", 25)
smtp.login("ski2per@163.com", "skippeR1986")

msg = "From: %s\r\nTO: %s\r\n\r\n%s" %(from_addr, to_addr, "yo buddy")

smtp.sendmail(from_addr, to_addr, msg)
smtp.close()
