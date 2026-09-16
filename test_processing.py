from image_processing import load_image, resize_image, prepare_image



image = load_image("test.jpg")

print("--------------------------------")
print("IMAGE PROCESSING TEST")
print("--------------------------------")
print("Image loaded successfully.")
print("Image shape:", image.shape)



resized_image = resize_image(image, scale=0.5)

print("Resized image shape:", resized_image.shape)



prepared_image = prepare_image(image)

print("Image preparation successful.")
print("Prepared image shape:", prepared_image.shape)
print("--------------------------------")
