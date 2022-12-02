import os
import random
import shutil

def create_directory(path):
    if not os.path.exists(path):    
        # Create a new directory because it does not exist 
        os.makedirs(path)
        print("The new directory is created!")

images_directory = "/Users/MrBS/Desktop/dr-final/diabetic-retinopathy/Images"

all_images_path = os.path.join(images_directory, "all")
test_images_path = os.path.join(images_directory, "test")
train_images_path = os.path.join(images_directory, "train")

create_directory(test_images_path)
create_directory(train_images_path)

train_ratio, test_ratio = 0.8, 0.2
for label in os.listdir(all_images_path):
    if label not in ['.DS_Store']:                
        labeled_image_path = os.path.join(all_images_path, label)

        labeled_images = [os.path.join(labeled_image_path, image) for image in os.listdir(labeled_image_path)]
        random.shuffle(labeled_images)

        total_images = len(labeled_images)
        train_images = labeled_images[:int(total_images * train_ratio)]
        test_images = labeled_images[int(total_images * train_ratio):]

        test_images_label_path = os.path.join(test_images_path, label)
        train_images_label_path = os.path.join(train_images_path, label)
        create_directory(test_images_label_path)
        create_directory(train_images_label_path)
        
        for img in train_images:
            shutil.copy(img, train_images_label_path)
        
        for img in test_images:
            shutil.copy(img, test_images_label_path)        
