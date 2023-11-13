from PIL import Image, ImageDraw

# Replace with your image file path
image_path = './outputs/SynthDoG_en/test/image_4.jpg'

# Open an image
image = Image.open(image_path)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define bbox coordinates (x1, y1, x2, y2, x3, y3, x4, y4)
# Replace with your bbox coordinates
bbox = [162.685, 166.77496, 330.06577, 164.0787, 326.52252, 193.89839, 158.90587, 196.92804]
bbox_x = [162.685, 330.06577, 326.52252, 158.90587]
bbox_y = [166.77496, 164.0787, 193.89839, 196.92804]

x_min = min(bbox_x)
x_max = max(bbox_x)
y_min = min(bbox_y)
y_max = max(bbox_y)


# Draw the bbox
# The 'outline' argument specifies the color of the bbox
# draw.polygon(bbox, outline='red')
draw.rectangle([326.59128, 342.19955, 447.36945, 387.04205], outline='red')

# Save or show the image
image.show()  # This will show the image with bbox
image.save('./example.jpg')  # Uncomment to save the image
