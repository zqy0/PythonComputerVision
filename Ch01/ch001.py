
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# pil_im = Image.open('timg.jpg')
#
# # convert()颜色转换  convert('L')转换成灰度图像
# # pil_im2 = Image.open('timg.jpg').convert('L')
# # pil_im2.save('timg2.jpg')
#
# pil_im3 = pil_im.thumbnail((128,128))
# pil_im3.save('timg3.jpg')


im = np.array(Image.open('I:\python\书籍\Python计算机视觉编程\\timg.jpg'))
plt.imshow(im)
print('Please click 3 points')
x = plt.ginput(3)
print('you clicked:', x)
plt.show()