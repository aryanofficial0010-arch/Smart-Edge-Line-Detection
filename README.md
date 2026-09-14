# Smart Edge & Line Detection System
 **Live Demo:** [Open the Application](https://smart-edge-line-detection-nvbkfwmixkgvajw5rf85bb.streamlit.app/)
## Overview

The Smart Edge & Line Detection System is a Computer Vision application that detects significant edges and straight lines in images.

The system uses the **Canny Edge Detection algorithm** to identify edges and the **Hough Line Transform** to detect straight lines from the resulting edge image.

A Streamlit-based interface allows users to upload an image and view the original image, detected edges, detected lines, and numerical analysis results.

---

## Problem Statement

Identifying important edges and straight lines is a fundamental task in Computer Vision. Manual identification of these features from images can be time-consuming and difficult, especially when images contain complex structures.

This project provides an automated solution that processes an input image, detects significant edges using Canny Edge Detection, and identifies straight lines using the Hough Line Transform.

---

## Objectives

- Convert input images into a suitable format for image processing.
- Reduce image noise using Gaussian smoothing.
- Detect significant edges using Canny Edge Detection.
- Detect straight lines using the Hough Line Transform.
- Calculate the percentage of edge pixels.
- Count the detected straight lines.
- Provide an easy-to-use graphical interface for image analysis.

---

## Features

- Image upload through a Streamlit interface.
- Grayscale conversion and Gaussian smoothing.
- Canny Edge Detection.
- Probabilistic Hough Line Transform.
- Visualization of detected edges.
- Visualization of detected straight lines.
- Automatic line counting.
- Edge pixel percentage calculation.
- Result messages based on the detected lines.

---

## System Workflow

```text
Input Image
     ↓
Image Loading
     ↓
Grayscale Conversion
     ↓
Gaussian Blur
     ↓
Canny Edge Detection
     ↓
Hough Line Transform
     ↓
Line Detection
     ↓
Result Analysis
     ↓
Visual and Numerical Output