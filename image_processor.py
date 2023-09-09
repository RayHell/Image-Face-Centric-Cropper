import os
import face_recognition
from PIL import Image
from PIL import ImageOps
print(dir(Image))

def crop_and_resize(image_path, output_path):
    # Load the image
    image = face_recognition.load_image_file(image_path)
    pil_image = Image.fromarray(image)
    
    # Detect face
    face_locations = face_recognition.face_locations(image)
    if not face_locations:
        print(f"No face detected in the image {image_path}.")
        return

    # Get the top, right, bottom, left coordinates of the detected face
    top, right, bottom, left = face_locations[0]
    
    # Calculate the center of the face
    center_x = (right + left) // 2
    center_y = (top + bottom) // 2

    # Get image dimensions
    img_width, img_height = pil_image.size

    # Determine the dimension to be maximized
    side_length = min(img_width, img_height)
    half_side = side_length // 2

    # Calculate the coordinates of the square to be cropped
    crop_left = center_x - half_side if center_x - half_side >= 0 else 0
    crop_right = crop_left + side_length
    crop_top = center_y - half_side if center_y - half_side >= 0 else 0
    crop_bottom = crop_top + side_length

    # Adjust if necessary to ensure we don't go outside the image bounds
    if crop_right > img_width:
        diff = crop_right - img_width
        crop_right -= diff
        crop_left -= diff

    if crop_bottom > img_height:
        diff = crop_bottom - img_height
        crop_bottom -= diff
        crop_top -= diff

    # Crop the image
    cropped_image = pil_image.crop((crop_left, crop_top, crop_right, crop_bottom))

    # Resize to 1024x1024
    resized_image = cropped_image.resize((1024, 1024), Image.LANCZOS)
    resized_image.save(output_path)



def process_images_in_directory(input_dir="images", output_dir="cropped"):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is a .jpg image
        if filename.lower().endswith('.jpg'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            # Process the image
            try:
                crop_and_resize(input_path, output_path)
                print(f"Processed {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Uncomment the line below to run the function
process_images_in_directory()
