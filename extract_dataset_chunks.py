import os
import shutil 
import random 

base_path = "/home/nova/Lab_individual_works/Daniyal/thesis/Data/ILSVRC_TRAIN"
target_path = "/home/nova/Lab_individual_works/Daniyal/thesis/Data/test_cluster/"


for _ in range(random.randrange(5, 200)):
    
    f = random.choice(os.listdir(base_path))
    dir = os.path.join(base_path, f)
    if os.path.isdir(dir):
    
        try:
    
            os.mkdir(os.path.join(target_path, f))
            for i in range(random.randrange(5, 50)):
                img_name = random.choice(os.listdir(dir))
                src_dir = os.path.join(dir, img_name)
                dest_dir = os.path.join(target_path+f, img_name)
                shutil.copy(src_dir, dest_dir)
    
        except FileExistsError:
            continue

    