import qrcode

photo = "1NONIkONBbxPYc7ovvUesOXeupAcMGOER"

url_photo = f"https://drive.google.com/file/d/{photo}/view?usp=sharing"

photo_path = "QRPro1.png"


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(url_photo)
qr.make(fit=True)

img = qr.make_image(
    fill_color = "black", 
    back_color = "white"
)
img.save(photo_path)

print("QR Code was generated in Name : QRPro1")
