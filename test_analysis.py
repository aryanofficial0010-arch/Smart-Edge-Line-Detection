import numpy as np

from result_analysis import (
    count_lines,
    calculate_edge_percentage,
    generate_result_message
)


print("********************************")
print("RESULT ANALYSIS TEST")
print("********************************")


# Test line counting
test_lines = [
    [[10, 10, 100, 10]],
    [[20, 20, 20, 100]],
    [[30, 30, 120, 80]]
]

line_count = count_lines(test_lines)

print("Lines counted:", line_count)


# Test edge percentage calculation
test_edges = np.zeros((100, 100), dtype=np.uint8)

# Mark 1000 pixels as edges
test_edges[:10, :] = 255

edge_percentage = calculate_edge_percentage(test_edges)

print("Edge percentage:", f"{edge_percentage:.2f}%")


# Test result message
message = generate_result_message(line_count)

print("Result message:", message)

print("********************************")
print("Analysis tests completed successfully.")
print("********************************)
