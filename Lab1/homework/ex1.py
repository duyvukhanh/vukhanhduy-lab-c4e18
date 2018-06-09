# from datetime import datetime
# time = datetime.now()
# print(time)
# print(time.hour)
# print(time.minute)

from gmail import GMail, Message
from random import choice
from datetime import datetime

gmail = GMail('duyvukhanhc4e@gmail.com','vukhanhduy')

html_content = """
<p style="text-align: center;"><strong>Cộng h&ograve;a X&atilde; hội Chủ nghĩa Việt Nam</strong></p>
<p style="text-align: center;"><strong>Độc lập - Tự do - Hạnh ph&uacute;c</strong></p>
<p style="text-align: center;">&nbsp;</p>
<h2 style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></h2>
<p>K&iacute;nh gửi : Gia&oacute; vi&ecirc;n chủ nhiệm lớp C4E18</p>
<p>T&ecirc;n em l&agrave; : Vũ Kh&aacute;nh Duy</p>
<p>Em viết đơn n&agrave;y xin ph&eacute;p nghỉ học ng&agrave;y xx/yy/zz do em bị {{sickness}} . Em hứa sẽ học b&agrave;i v&agrave; l&agrave;m b&agrave;i đầy đủ. Em xin ch&acirc;n th&agrave;nh cảm ơn.</p>
<p>Sinh vi&ecirc;n</p>
<p>&nbsp; &nbsp;Duy</p>
"""

reasons = ["Sùi","HIV","Giang mai","Lậu","ung thư","AIDS"]

loop = True
while loop:
    reason = choice(reasons)
    new_html = html_content.replace("{{sickness}}",reason)
    msg = Message('Hello',to='duyvukhanhc4e@gmail.com',html=new_html)
    time = datetime.now()   
    if time.hour == 7 and time.minute == choice(range(60)):
        gmail.send(msg)
        loop = False

