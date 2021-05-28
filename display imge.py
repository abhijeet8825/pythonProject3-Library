import cv2

img=cv2.imread('C:\\Users\\ABHIJEET KUMAR\\OneDrive\\Pictures\\Baby.jpg',1)
resize_img=cv2.resize(img,(700,660))
cv2.imshow('baby image',resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()