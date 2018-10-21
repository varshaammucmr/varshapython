
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("varshapn27@gmail.com","ABCDEFGHIJK")
msg="hello"
s.sendmail("varshapn27@gmail.com","vadisenays@gmail.com",msg)
print('sent')
s.quit()



dl211@soetcse:~/varsha$ python3 smtp.py
sent

