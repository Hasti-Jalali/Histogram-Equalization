import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

COLOR_LEVEL = 256

#### Phase 1
img = Image.open("image.png")
x, y = img.size
imgGray = []
max = 0
if(img.mode == 'RGBA' or img.mode == 'RGB'):
    for j in range(y):
        row = []
        for i in range(x):
            p = img.getpixel((i,j))
            row.append(round(0.2989 * p[0] + 0.5870 * p[1] + 0.1140 * p[2]))
            # row.append(round((p[0]+p[1]+p[2])/3))
        imgGray.append(row)
else :
    for j in range(y):
        row = []
        for i in range(x):
            row.append(img.getpixel((i,j)))
            # row.append(round((p[0]+p[1]+p[2])/3))
        imgGray.append(row)

# plt.imshow(imgGray, cmap='gray')
# plt.show()

#### Phase 2
counter = [0 for i in range(COLOR_LEVEL)]
for i in range(len(imgGray)):
    for j in range(len(imgGray[0])):
        counter[imgGray[i][j]] += 1

# plt.plot(counter)
# plt.show()

#### Phase 3
for i in range(1, COLOR_LEVEL): 
    counter[i] += counter[i-1]
# plt.plot(counter)
# plt.show()

#### Phase 4
mappedCounter = [round(((COLOR_LEVEL - 1) * counter[i]) / (x * y)) 
                for i in range(COLOR_LEVEL)]

#### Phase 5
for i in range(len(imgGray)):
    for j in range(len(imgGray[0])):
        index = imgGray[i][j]
        imgGray[i][j] = mappedCounter[index]

array = np.array(imgGray, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save('changed.png')
print('done!')

