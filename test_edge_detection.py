import cv2

from image_processing import load_image, prepare_image
from edge_detection import detect_edges, detect_lines, draw_lines
from result_analysis import count_lines


# Load test image
image = load_image("test.jpg")

# Prepare image
prepared_image = prepare_image(image)

# Detect edges using Canny
edges = detect_edges(prepared_image)

# Detect straight lines using Hough Transform
lines = detect_lines(edges)

# Draw detected lines
result = draw_lines(image, lines)

# Count detected lines
line_count = count_lines(lines)


print("--------------------------------")
print("CANNY + HOUGH LINE DETECTION")
print("--------------------------------")
print("Lines detected:", line_count)
print("--------------------------------")

# Save results
cv2.imwrite("edge_result.jpg", edges)
cv2.imwrite("line_detection_result.jpg", result)

print("Results saved successfully.")