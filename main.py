import cv2
import numpy as np

img = cv2.imread('dataset/face7.jpg')

#  BGR2HLS
in_bgr2HLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
im_data_HLS = np.asarray(in_bgr2HLS, dtype='float32')
H1 = im_data_HLS[:,:,0]

#  BGR2HVS
in_rgb2HVS = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
im_data_HVS = np.asarray(in_rgb2HVS, dtype='float32')
H2 = im_data_HVS[:,:,0]

n = 0
for i in range(np.size(im_data_HLS, 0)):
    for j in range(np.size(im_data_HLS, 1)):
        # print(H1[i][j], H2[i][j])
        # if H1[i][j] != H2[i][j]:
        #     print(H1[i][j], H2[i][j])
        #     n = n + 1


        if H2[i][j] > 179:
           # if H1[i][j] != H2[i][j]:
           #      print(H1[i][j], H2[i][j])
                n = n+1

print(n)
