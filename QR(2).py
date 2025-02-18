import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border= 4,)
qr.add_data('https://www.linkedin.com/in/ali-hasnain-raza-892153285/')
qr.make(fit=True)
img = qr.make_image(fill_color='white',back_color='black')
img.save("linkedin_qr.png")





