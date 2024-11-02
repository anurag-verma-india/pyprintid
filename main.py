import simple_pdf_to_png
from PIL import Image

"""
Step of converstion

[x] Convert pdf to jpg

[x] Make a new blank with a4 size paper 

Place some margin (~5mm)
[x] Place front_photo on the left and back on the right (with size less than 65x95 mm)

[] Place 4 images one below the other (margin of ~5mm before each one)

[] Save this file as pdf
"""


simple_pdf_to_png.convert_pdf_to_png("./pdf-files", "./png-files")

"""
1in = 2.54cm x 10 (*because there is 10mm in 1cm)
1in = 25.4mm
96px = 25.4mm
1mm = 96px / 25.4
Millimeters to Pixels Formula:
pixels = millimeters * ( PPI / 25.4 )
"""


## mm to pixels conversion (at a given ppi)
def mm_to_pixel(mm):
    ppi = 300  # ppi is same as dpi
    mm_in_1_inch = 25.4  # 1 inch = 25.4 mm
    mm_to_pixel_conversion_rate = ppi / mm_in_1_inch
    pixels = int(round(mm * (ppi / mm_in_1_inch)))
    return pixels


bg_image = Image.open(r"blank_image.png")

# Adding vertical and horizontal lines (every virtual 10 mm)

# Lines on top
width_generated = 1
height_generated = 20
vertical_line_pil = Image.new(mode="RGB", size=(width_generated, height_generated))
pixels_of_generated_pil_image = vertical_line_pil.load()

for i in range(width_generated):
    for j in range(height_generated):
        pixels_of_generated_pil_image[i, j] = (0, 0, 0)

for i in range(22):
    bg_image.paste(
        vertical_line_pil,
        (mm_to_pixel(i * 10), mm_to_pixel(2.5)),
    )
# Lines on the left
width_generated = 20
height_generated = 1
horizontal_line_pil = Image.new(mode="RGB", size=(width_generated, height_generated))
pixels_of_generated_pil_image = horizontal_line_pil.load()

for i in range(width_generated):
    for j in range(height_generated):
        pixels_of_generated_pil_image[i, j] = (0, 0, 0)

for i in range(30):
    bg_image.paste(
        horizontal_line_pil,
        (mm_to_pixel(2.5), mm_to_pixel(i * 10)),
    )


pasted_img1 = Image.open(r"png-files/MATHURALAL copy 1.png")
print(pasted_img1.size)

width, height = pasted_img1.size
new_height = mm_to_pixel(350)
new_width = int(round(new_height * width / height))
print(new_height)
pasted_img1 = pasted_img1.resize((new_width, new_height))

bg_image.paste(pasted_img1, box=(mm_to_pixel(7), mm_to_pixel(0*70+5)))

pasted_img2 = Image.open(r"png-files/MATHURALAL copy 2.png")
pasted_img3 = Image.open(r"png-files/MATHURALAL copy 3.png")
pasted_img4 = Image.open(r"png-files/MATHURALAL copy 4.png")

pasted_img2 = pasted_img2.resize((new_width, new_height))
bg_image.paste(pasted_img2, box=(mm_to_pixel(7), mm_to_pixel(1*70+5)))
pasted_img3 = pasted_img3.resize((new_width, new_height))
bg_image.paste(pasted_img2, box=(mm_to_pixel(7), mm_to_pixel(2*70+5)))
pasted_img4 = pasted_img4.resize((new_width, new_height))
bg_image.paste(pasted_img3, box=(mm_to_pixel(7), mm_to_pixel(3*70+5)))

bg_image.save("output.png")
