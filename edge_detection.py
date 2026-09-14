import cv2
import numpy as np


def convert_to_grayscale(image):
    """Convert the input image to grayscale."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


def apply_gaussian_blur(gray_image):
    """Reduce image noise using Gaussian blur."""
    blurred = cv2.GaussianBlur(
        gray_image,
        (5, 5),
        0
    )
    return blurred


def detect_edges(gray_image):
    """Detect edges using the Canny edge detection algorithm."""
    edges = cv2.Canny(
        gray_image,
        50,
        150
    )
    return edges


def detect_lines(edges):
    """Detect straight lines using the Probabilistic Hough Transform."""

    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=50,
        minLineLength=50,
        maxLineGap=10
    )

    if lines is None:
        return []

    return lines


def draw_lines(image, lines):
    """Draw detected lines on the original image."""

    result = image.copy()

    for line in lines:

        x1, y1, x2, y2 = line[0]

        cv2.line(
            result,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            3
        )

    return result