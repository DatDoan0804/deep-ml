import numpy as np


def zero_pad_image(img, pad_width):
    """
    Add zero padding around a grayscale image.

    Args:
        img: 2D list or numpy array of pixel values
        pad_width: integer number of pixels to pad on each side

    Returns:
        Padded image as 2D list with integer values,
        or -1 if input is invalid
    """
    if not img or pad_width < 0:
        return -1
    # Write your code here
    img = np.array(img)
    if len(img.shape) < 2:
        return -1
    n, m = img.shape
    img = np.hstack((img, np.zeros((n, pad_width))))
    img = np.hstack((np.zeros((n, pad_width)), img))
    img = np.vstack((np.zeros((pad_width, m+pad_width*2)), img))
    img = np.vstack((img, np.zeros((pad_width, m+pad_width*2))))
    return img
