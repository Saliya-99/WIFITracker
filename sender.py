import smtplib

sender = 'saliyadinusha99@gmail.com'
receivers = 'dinushasaliya@gmail.com'

message = "Example"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('saliyadinusha99@gmail.com', 'yhgoeelcfvewyguv')
server.sendmail(sender, receivers, message)         
print ("Successfully sent email")