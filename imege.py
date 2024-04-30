import cv2
import numpy as np

img = cv2.imread('color_text.jpg')
new_img = np.zeros(img.shape, dtype='uint8')

img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.Canny(img, 20, 20)

con1, hir1 = cv2.findContours(img[:160, :736], cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
con2, hir2 = cv2.findContours(img[161:312, :736], cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
con3, hir3 = cv2.findContours(img[313:463, :736], cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(new_img, con1, -1, (0,255,0), 1)
cv2.drawContours(new_img[161:312, :736], con2, -1, (0,0,255), 1)
cv2.drawContours(new_img[313:463, :736], con3, -1, (230,90,70), 1)
cv2.imshow('Result', new_img)
cv2.waitKey(0)