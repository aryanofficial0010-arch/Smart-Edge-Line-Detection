import cv2
import os


def load_image(image_path):
    """Load an image from the project folder."""

    if not os.path.isabs(image_path):
        project_folder = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(project_folder, image_path)

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Could not load the image.")

    return image


def resize_image(image, scale=1):
    """Resize the image if required."""

    if scale == 1:
        return image

    resized = cv2.resize(
        image,
        None,
        fx=scale,
        fy=scale,
        interpolation=cv2.INTER_CUBIC
    )

    return resized


def prepare_image(image):
    """Prepare image for edge detection."""

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    blurred = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    return blurred