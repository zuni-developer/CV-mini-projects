import cv2 as cv

#taking input image
image=cv.imread("input.jpeg")
#showing the original image
cv.imshow("Original Image", image)
cv.waitKey(0)
#resizing the image
scale_percent = 25  
height=int(image.shape[0]*scale_percent/100)
width=int(image.shape[1]*scale_percent/100)
resized_image=cv.resize(image,(width,height))  
#showing the resized image
cv.imshow("Resized Image",resized_image)
cv.waitKey(0)
cv.destroyAllWindows()
#saving the resized image to file
cv.imwrite("resized_input.jpeg",resized_image)
#saving the output in another folder
cv.imwrite("C:/test/resized_image.jpeg",resized_image)