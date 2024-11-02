import os 

png_files = os.listdir("png-files/")
# for file in png_files:
#     path_to_file = os.path.join("png-files/",file)
#     os.system(f"firefox {path_to_file}")

print(len(png_files))

if os.path.isfile("blank_image.png"):
    
    print("File exists")


def mm_to_pixel(mm):
    ppi = 300  # ppi is same as dpi
    mm_in_1_inch = 25.4  # 1 inch = 25.4 mm
    mm_to_pixel_conversion_rate = ppi / mm_in_1_inch
    pixels = int(round(mm * (ppi / mm_in_1_inch)))
    return pixels


print()

print(mm_to_pixel(210))
print(mm_to_pixel(297))
print(mm_to_pixel(350))
