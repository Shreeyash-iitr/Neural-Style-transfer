#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:49:33 2018

@author: shreeyash
"""

import cv2
import numpy as np
from keras.applications import vgg19

# ====== Load pretrained keras model for VGG19=========
model = vgg19.VGG19()

# ======= Preprocessing Input images ===================
content_img = cv2.imread('content.jpg')
content_img = cv2.resize(content_img, (224,224))
content_img = content_img.astype(np.float32)
content_img = np.expand_dims(content_img, axis = 0)

style_img = cv2.imread('style.jpg')
style_img = cv2.resize(style_img, (224,224))
style_img = style_img.astype(np.float32)
style_img = np.expand_dims(style_img, axis = 0)

generated_img = np.random.randint()



