import os
from PIL import Image
import numpy as np

def get_imlist(path):
    """返回目录中所有JPG图像的文件列表"""
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im, sz):
    pil_im = Image.fromarray(np.uint8(im))

    return np.array(pil_im.resize(sz))