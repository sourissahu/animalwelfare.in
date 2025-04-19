import os

# Set your folder path
folder_path = r"C:\Users\souri\Documents\animalwelfare.in\images\fullgallery"

# Get all image files
image_extensions = ('.jpg', '.jpeg', '.png')
files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
files.sort()  # optional: sort alphabetically

# First pass: Rename to temp names to avoid collisions
for idx, filename in enumerate(files):
    ext = os.path.splitext(filename)[1].lower()
    temp_name = f"temp_{idx}{ext}"
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, temp_name))

# Second pass: Rename to final names
temp_files = [f for f in os.listdir(folder_path) if f.startswith("temp_")]
temp_files.sort()  # ensure ordering

for i, filename in enumerate(temp_files, start=1):
    ext = os.path.splitext(filename)[1].lower()
    new_name = f"img{i}{ext}"
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))

print("✅ All images renamed sequentially as img1.jpeg, img2.jpeg, ...")
