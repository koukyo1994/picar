import cv2


CAMERA = cv2.VideoCapture(0)
CAMERA.set(3, 320)
CAMERA.set(4, 240)
CAMERA.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cv2.setUseOptimized(True)


def get_frame():
    """Return the current camera frame."""
    _, frame = CAMERA.read()
    return frame
