from PIL import Image
  
def convertImage():
    img = Image.open("png-files/1.png")
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
  
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
  
    img.putdata(newData)
    img.save("png-files/New.png", "PNG")
    print("Successful")
    
convertImage()


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
            print(filename)
            print(bbox)
            # print(bbox)
            if bbox:
                # Crop the image using the bounding box
                cropped_image = image.crop(bbox)
                cropped_image.save(output_path)
