import cv2
import numpy as np
def swap_pixels(image, x1, y1, x2, y2):
    image[x1, y1], image[x2, y2] = image[x2, y2], image[x1, y1]

def encrypt_image(image, key=10):
    encrypted_image = np.clip(image.astype(int) + key, 0, 255).astype(np.uint8)
    return encrypted_image

def decrypt_image(encrypted_image, key=10):
    decrypted_image = np.clip(encrypted_image.astype(int) - key, 0, 255).astype(np.uint8)
    return decrypted_image
original_image = cv2.imread('your_image.jpg')
swap_pixels(original_image, 100, 200, 300, 400)
encrypted_image = encrypt_image(original_image)

decrypted_image = decrypt_image(encrypted_image)

cv2.imwrite('encrypted.jpg', encrypted_image)
cv2.imwrite('decrypted.jpg', decrypted_image)

print("Image encryption and decryption completed.")
