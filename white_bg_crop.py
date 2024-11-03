from PIL import Image
import os

# https://stackoverflow.com/questions/48395434/how-to-crop-or-remove-white-background-from-an-image
def convert_white_pixels_to_transparent(img: Image.Image) -> Image.Image:
    """_summary_
    Converts the PIL image's pure white pixels to transparent ones

    Args:
        img (Image.Image): A PIL image

    Returns:
        Image.Image: A PIL image
    """
    # img = Image.open("png-files/1.png")
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []

    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    # img.save("png-files/New.png", "PNG")
    # print("Successful")
    return img


def crop_out_white_pixels(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Remove blank pixels
    # https://gist.github.com/kitze/f078c38a84f6c9b1f524806fc0e819aa
    for filename in os.listdir(input_folder):
        # print(filename)
        if filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            with Image.open(image_path) as image:
                image = convert_white_pixels_to_transparent(image)

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
                # print(filename)
                # print(bbox)
                if bbox:
                    # Crop the image using the bounding box
                    cropped_image = image.crop(bbox)
                    cropped_image.save(output_path)


if __name__ == "__main__":
    input_folder_global = "png-files/"
    output_folder_global = "cropped-pngs/"
    crop_out_white_pixels(input_folder_global, output_folder_global)
