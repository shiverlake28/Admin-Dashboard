# import PIL.Image as pillow
# import PIL.ImageFilter as ImageFilter
# img = pillow.open("C:\\Users\\HP\\Downloads\\The Rookies.png")
# print(img)
# print(img.size)
# print(img.format)
# print(img.mode)

# filtered_img = img.filter(ImageFilter.BoxBlur(10))
# filtered_img.save("blue.png","png")

# convert_img = img.convert("L")
# convert_img.save('gray.png','png')
# #convert_img.show()

# resize = convert_img.resize((3000,3000))
# resize.save('graay.png','png')
# #resize.show()

# cropped = resize.crop([1000,1000,2500,2500])
# cropped.save('croped.png','png')
# #cropped.show()

# thumb = cropped.thumbnail((400,200))
# thumb.save('thumb.png','png')
# thumb.show()
'''
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['From'] = 'adityapasari227@gmail.com'
email['To'] = 'adityapasari278@gmail.com'
email['Subject'] = 'you are my friend but have to get your ass fucked'

email.set_content("i am a student")

with smtplib.SMTP(host = "smtp.gmail.com" ,port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("adityapasari227@gmail.com","wsbf qpqc zxpo zydv")
    smtp.send_message(email)
    print("done")
'''










