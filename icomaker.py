from PIL import Image
filename = r'test.png'
img = Image.open(filename)
img.save('logo1.ico')

# ====================
# Optionally, you may specify the icon sizes you want:

icon_sizes = [(16,16), (32, 32), (48, 48), (64, 64)]
img.save('logo2.ico', sizes=icon_sizes)
