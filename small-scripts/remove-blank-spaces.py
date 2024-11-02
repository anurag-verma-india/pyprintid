from PIL import Image
import os

input_folder = "png-files"
output_folder = "cropped-pngs"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        image_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        with Image.open(image_path) as image:
            # Convert the image to RGBA mode if necessary
            if image.mode != "RGBA":
                image = image.convert("RGBA")
            # Check if the alpha channel exists
            if "A" not in image.getbands():
                continue
            # Separate the RGBA channels
            r, g, b, a = image.split()
            # Find the bounding box of the non-blank pixels in the alpha channel
            bbox = a.getbbox()
            # print(bbox)
            if bbox:
                # Crop the image using the bounding box
                cropped_image = image.crop(bbox)
                cropped_image.save(output_path)
