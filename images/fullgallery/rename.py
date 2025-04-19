import os

folder_path = r"C:\Users\souri\Documents\animalwelfare.in\images\fullgallery"
files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))])

for i, filename in enumerate(files, start=1):
    new_name = f"img{i}.jpeg"
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    if not os.path.exists(dst):
        os.rename(src, dst)
    else:
        print(f"Skipped: {dst} already exists")

print("Renaming completed.")
