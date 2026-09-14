def count_lines(lines):
    """Count the number of detected straight lines."""
    return len(lines)


def calculate_edge_percentage(edges):
    """Calculate the percentage of pixels identified as edges."""
    total_pixels = edges.shape[0] * edges.shape[1]

    if total_pixels == 0:
        return 0

    edge_pixels = (edges > 0).sum()

    percentage = (edge_pixels / total_pixels) * 100

    return percentage


def generate_result_message(line_count):
    """Generate a message based on the number of detected lines."""
    if line_count == 0:
        return "No straight lines were detected."
    elif line_count == 1:
        return "One straight line was detected."
    else:
        return f"{line_count} straight lines were detected."