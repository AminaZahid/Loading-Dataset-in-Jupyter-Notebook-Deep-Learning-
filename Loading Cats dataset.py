import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
DATADIR = "C:/Users/zahid/Desktop/kagglecatsanddogs_3367a/PetImages"
CATEGORIES = ["Cat"]
for category in CATEGORIES:
    path = os.path.join(DATADIR,category)            #path to cats dir.
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array, cmap="gray")
        plt.show()
