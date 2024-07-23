import cv2

inputPath = "../assets/hello.jpeg"
colorSpace = 0

img = cv2.imread(inputPath,colorSpace)

windowName = 'Image'
cv2.imshow(windowName,img)
cv2.waitKey(0)
cv2.destroyAllWindows()





















"""
outputPath = '../assets/new.jpeg'
cv2.imwrite(outputPath,img)
"""