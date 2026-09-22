import streamlit as st
import cv2
import numpy as np

from edge_detection import (
    detect_edges,
    detect_lines,
    draw_lines
)

from result_analysis import (
    count_lines,
    calculate_edge_percentage,
    generate_result_message
)



st.set_page_config(
    page_title="Smart Edge & Line Detection",
    page_icon="📐",
    layout="wide"
)




st.title(" Smart Edge & Line Detection System")

st.write(
    "Upload an image to detect edges using the Canny Edge "
    "Detection algorithm and identify straight lines using "
    "the Hough Line Transform."
)



uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)




if uploaded_file is not None:

    # Read uploaded image
    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    # Convert uploaded data into an OpenCV image
    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    # Check image
    if image is None:

        st.error("Could not read the uploaded image.")

    else:

        

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        blurred = cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )


       
        edges = detect_edges(
            blurred
        )


     

        lines = detect_lines(
            edges
        )



        result = draw_lines(
            image,
            lines
        )


 

        line_count = count_lines(
            lines
        )

        edge_percentage = calculate_edge_percentage(
            edges
        )

        message = generate_result_message(
            line_count
        )


        

        st.subheader("Image Processing Results")

        col1, col2, col3 = st.columns(3)


        with col1:

            st.write("### Original Image")

            st.image(
                cv2.cvtColor(
                    image,
                    cv2.COLOR_BGR2RGB
                ),
                use_container_width=True
            )


        with col2:

            st.write("### Canny Edges")

            st.image(
                edges,
                use_container_width=True
            )


        with col3:

            st.write("### Detected Lines")

            st.image(
                cv2.cvtColor(
                    result,
                    cv2.COLOR_BGR2RGB
                ),
                use_container_width=True
            )



        st.subheader(" Detection Results")

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Lines Detected",
                line_count
            )


        with col2:

            st.metric(
                "Edge Pixels",
                f"{edge_percentage:.2f}%"
            )


        with col3:

            st.success(
                message
            )


     

        st.divider()

        st.info(
            "Canny Edge Detection is used to identify "
            "significant edges, followed by the Hough Line "
            "Transform to detect straight lines."
        )
