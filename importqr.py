import qrcode
import time
import base64
from datetime import datetime
import secrets
from urllib.parse import quote

# ==============================
# CONFIGURATION
# ==============================
url_photo = "https://swhjidou.github.io/schoolqr.github.io/Cap1.PNG"
photo_path = r"C:\Users\pc\Desktop\QRPro1.png"
duree_validite = 3  # minutes

# ==============================
# FONCTION : générer URL temporaire
# ==============================
def generer_url_temporelle():
    timestamp_creation = int(time.time())
    timestamp_expiration = timestamp_creation + (duree_validite * 60)

    token = secrets.token_hex(16)

    url_encodee = base64.urlsafe_b64encode(url_photo.encode("utf-8")).decode("utf-8")

    url_temporelle = (
        f"https://swhjidou.github.io/schoolqr.github.io/verifier.html"
        f"?url={quote(url_encodee)}"
        f"&exp={timestamp_expiration}"
        f"&token={token}"
    )

    return url_temporelle, timestamp_expiration

# ==============================
# GÉNÉRATION
# ==============================
url_temp, expiration = generer_url_temporelle()

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(url_temp)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(photo_path)

# ==============================
# AFFICHAGE
# ==============================
print("=" * 50)
print("✅ QR CODE TEMPORAIRE GÉNÉRÉ !")
print("=" * 50)
print(f"\n📁 Emplacement : {photo_path}")
print(f"⏱️ Validité : {duree_validite} minutes")
print(f"🕐 Expire à : {datetime.fromtimestamp(expiration).strftime('%H:%M:%S')}")
print(f"\n🔗 URL du QR :\n{url_temp}")
print("\n⚠️ Le QR expirera seulement si verifier.html existe sur GitHub Pages.")