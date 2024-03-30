import cv2
import numpy as np

"""
this function takes a photo and returns saved image path as a tuple
"""
def take_photo():
  cap = cv2.VideoCapture(1)
  while True:

    if not cap.isOpened():
      print("Unable to open the camera")
      return

    ret, frame = cap.read()

    if not ret:
      print("Failed to capture frame")
      return
    
    cv2.imshow("camera view", frame)

    if cv2.waitKey(1) == ord('q'):
      cv2.imwrite("photo.jpg", frame)

      cap.release()
      cv2.destroyAllWindows()

      print("Photo captured successfully")

      return ("photo.jpg", )
    

"""
this function takes a grayscale mask and returns a colored mask
"""
def color_mask(mask):
    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    non_black_mask = np.any(mask_rgb != 0, axis=2)
    mask_rgb[non_black_mask] = [0, 0, 255]
    return mask_rgb
