
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread("./test.png")

# 이미지 사이즈 변경
dst = cv.resize(img2, dsize=(1000,1000), interpolation=cv.INTER_LINEAR)

plt.imshow(dst)
plt.show()

# 리니어보다 큐빅이 더 나음
dst2 = cv.resize(img2, dsize=(1000,1000), interpolation=cv.INTER_CUBIC)

plt.imshow(dst2)
plt.show()

# 이미지의 일부분을 따내는 것  ROI
rol = img2[50:300, 30:280]

plt.imshow(rol)
plt.show()