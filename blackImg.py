from PIL import Image

img = Image.new('RGB', (1080, 720), (0,0,0))
img.save("black.png")