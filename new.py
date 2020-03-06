import smtplib
import imaplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('levva.tsepesh@gmail.com', ')mn1aM3aM3cumP0rt012')
smtpObj.sendmail('levva.tsepesh@gmail.com', 'vlyahovich@c-i-p.ru', 'test mail')

mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
mail.login('levva.tsepesh@gmail.com', ')mn1aM3aM3cumP0rt012')
print(mail.list())




