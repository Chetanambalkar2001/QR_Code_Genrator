import qrcode
import image
qr=qrcode.QRCode(
    version=15, #15 means the version of qr code high the number bigger the code image & complicated pictures.
    box_size=10, #size of the box where qr code will be displayed.
    border=5, #it is the white part of image -- border in all 4 sides with white color.
)

data="It is vital to go through a national daily like The Hindu or The Indian Express and while reading these, pay special attention to news items and editorials that are either related to the Indian Constitution or the national as well as international political systems, in one way or the other."
#as i have the given oath of any link or channel like the same way you can give anything.
#if you dont want to redirect & create for normal text that write text in the quotes.

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("test.png")
