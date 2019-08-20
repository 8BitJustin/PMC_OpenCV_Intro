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

# new variable resizing the img object
resized_image = cv2.resize(img, (1000, 500))

# displays image in window
cv2.imshow("Galaxy", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()