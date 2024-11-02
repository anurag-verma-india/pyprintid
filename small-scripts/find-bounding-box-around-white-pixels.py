import numpy as np
from PIL import Image
import os

image = Image.open(os.path.join("png-files", os.listdir("png-files")[0]))
# print(os.path.join("png-files", os.listdir("png-files")[0]))

image_array = np.array(image)

# print(image_array[0][0])
print(image_array.shape)

# nparr = np.array(
#     [
#         [[0, 1, 2, 3], [12, 3, 2, 2]],
#         [[4, 4, 4, 4], [5, 5, 5, 5]],
#         [[2, 3, 4, 5], [2, 4, 4, 2]],
#     ]
# )
# print(nparr.shape)

print(np.where(image_array == (255,255,255)))