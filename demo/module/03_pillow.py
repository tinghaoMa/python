#!/user/bin/python3
#  -*- coding: utf-8 -*-
'''
    pip install pillow
'''
from PIL import Image, ImageFilter

im = Image.open('demo/resources/9-1FPGH525.jpg')
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))
# 把缩放后的图像用jpeg格式保存:
im.save('demo/resources/thumbnail.jpg', 'jpeg')

# 模糊效果
im = Image.open('demo/resources/9-1FPGH525.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('demo/resources/blur.jpg', 'jpeg')
