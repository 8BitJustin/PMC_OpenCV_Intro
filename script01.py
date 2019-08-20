import cv2

img = cv2.imread("galaxy.jpg", 0)

# prints type
print(type(img))

# prints image
print(img)

# prints resolution
print(img.shape)

# prints dimensions
print(img.ndim)

# new variable resizing the img object and .shape tuple
# can also use normal preset res - .resize(img, (500, 1000)
resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

# displays image in window
cv2.imshow("Galaxy", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()