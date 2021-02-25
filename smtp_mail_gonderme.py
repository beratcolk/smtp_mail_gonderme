import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

"""

SMTP Modülü ile mail gönderme...

İlk olarak daha az güvenli uygulamalar için aşağıdaki linkte tıklayarak güvenliği kaldırıyoruz.
İki faktörlü kimlik doğrulaması olan hesaplarda çalışmamaktadır.

https://myaccount.google.com/lesssecureapps

"""

mesaj = MIMEMultipart() #Mail yapımızı oluşturuyoruz.

mesaj["From"] = "-----" #Mailin kimden gideceğini yazıyoruz.

mesaj["To"] = "------" #Mailin kime gideceğini yazıyoruz.

mesaj["Subject"] = "Smtp Mail Gönderme" #Mailin konusunu yazıyoruz.


#içerik olarak ne göndereceğimizi yazıyoruz.
yazi = """

Smtp ile mail gönderiyorum.

Berat ÇOLAK

"""


mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi) #Mesaj gövdesini maile gönderiyoruz.

try:
    mail = smtplib.SMTP("smtp.gmail.com",587) #server portuna bağlanma.

    mail.ehlo() #SMTP server'ına bağlanıyoruz.

    mail.starttls() #Kullanıcı adımızı ve şifremizi şifreliyoruz.

    mail.login("","") #Mail sistemine bağlanıyoruz. İlk olarak mail adresimizi, ikinci olarak şifremizi giriyoruz.

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string()) #Mail gönderiliyor.

    print("Mail başarıyla gönderildi...")

    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu")
    sys.stderr.flush()

                  
