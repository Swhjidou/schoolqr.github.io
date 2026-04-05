import qrcode
from PIL import Image


# url = "https://github.com/Swhjidou/schoolqr.github.io/"

url = "https://swhjidou.github.io/schoolqr.github.io/"


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("static/images/qr_code.png")

print(f"QR code cree pour : {url}")
print("Fichier sauvegarde : static/images/qr_code.png")
