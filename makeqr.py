import qrcode
from PIL import Image

img = qrcode.make("https://github.com/SatomiWatanabe")
img.save('qr_code.png')

img.show()