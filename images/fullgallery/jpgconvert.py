import os
from PIL import Image

# Set your image folder path
folder_path = r"C:\Users\souri\Documents\animalwelfare.in\images\fullgallery"

# Supported image formats to convert
valid_extensions = ('.jpeg', '.png', '.webp', '.bmp')

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    name, ext = os.path.splitext(filename)

    # Skip already .jpg files
    if ext.lower() == '.jpg':
        continue

    # Check for valid image formats
    if ext.lower() in valid_extensions:
        try:
            img = Image.open(file_path).convert('RGB')  # Convert to RGB to avoid issues with .png/.webp
            new_filename = os.path.join(folder_path, f"{name}.jpg")
            img.save(new_filename, "JPEG", quality=95)
            img.close()
            os.remove(file_path)  # Remove the original non-jpg file
            print(f"✅ Converted and saved: {filename} → {name}.jpg")
        except Exception as e:
            print(f"❌ Failed to convert {filename}: {e}")
