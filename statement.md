# Project Statement

## Project Title

Smart Edge & Line Detection System

---

## Problem Statement

Edge and line detection are fundamental tasks in Computer Vision and are widely used to identify structural information in images.

Manually identifying important edges and straight lines from an image can be difficult and time-consuming. Therefore, an automated Computer Vision system is required to detect significant edges and straight lines efficiently.

This project develops a system that applies **Canny Edge Detection** to identify edges and the **Hough Line Transform** to detect straight lines from an input image.

---

## Project Scope

The project focuses on processing static images and extracting important structural features from them.

The system includes:

- Image input and validation
- Grayscale conversion
- Gaussian noise reduction
- Canny Edge Detection
- Hough Line Transform
- Straight-line detection
- Edge percentage calculation
- Line counting
- Visualization of processing results

The current scope is limited to image-based processing and does not include real-time video processing.

---

## Target Users

The system can be useful for:

- Computer Vision students
- Researchers learning image processing techniques
- Developers working with basic image analysis
- Students studying edge and line detection
- Users who need basic structural feature extraction from images

---

## High-Level Features

### 1. Image Input

The system accepts JPG, JPEG, and PNG images through the Streamlit interface.

### 2. Image Preprocessing

The input image is converted to grayscale and Gaussian smoothing is applied to reduce noise before edge detection.

### 3. Edge Detection

The system applies the **Canny Edge Detection algorithm** to identify significant edges in the image.

### 4. Line Detection

The detected edges are processed using the **Probabilistic Hough Line Transform** to identify straight lines.

### 5. Result Visualization

The system displays:

- Original image
- Canny edge image
- Image with detected lines

### 6. Result Analysis

The system calculates:

- Number of detected straight lines
- Percentage of edge pixels
- A descriptive result message

---

## Expected Outcome

The expected outcome is a functional Computer Vision application capable of automatically detecting significant edges and straight lines from uploaded images and presenting the results in an understandable visual and numerical format.sets.