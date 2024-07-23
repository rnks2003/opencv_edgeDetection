import cv2

dirPath = "/Users/rnks/Desktop/scrap/turing/"

frames = []

# turing00+i.jpeg
# turing0+i.jpeg

for i in range(1,30):
    if i<10 : img = cv2.imread(dirPath+f'turing00{i}.jpeg')
    else : img =  cv2.imread(dirPath+f'turing0{i}.jpeg')
    
    frames.append(img)
    

for i in frames:
    cv2.imshow("vid", i)
    cv2.waitKey(500)
    
cv2.destroyAllWindows()