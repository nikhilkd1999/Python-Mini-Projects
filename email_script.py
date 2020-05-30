import pandas 
import datetime
import smtplib

GMAIL_ID=''
PASSWORD = ''
RANGE = 6

if __name__ == "__main__":
    count = 0
    target_id = []
    total = RANGE*len(target_id)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, PASSWORD)
    for a in range(RANGE):
        for id in target_id:
            s.sendmail(GMAIL_ID, id, "Subject: \n\nBuffer Overflow!! \n\n Stay safe and secure your account.\n\n    You know who I am")
            count+=1
            print("Sent {count}/{total}".format(count=count,total=total))
    s.quit()