# CHANGE INDEX LABEL

import os

def ubah_label_folder(folder_path, label_lama, label_baru):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            ubah_label(file_path, label_lama, label_baru)

def ubah_label(file_path, label_lama, label_baru):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            parts = line.split()
            index_label = parts[0]
            anotasi = ' '.join(parts[1:])
            
            if index_label == str(label_lama):
                index_label = str(label_baru)
            
            new_line = f"{index_label} {anotasi}\n"
            file.write(new_line)

# Gantilah 'path_ke_folder', 992, dan 292 dengan path folder yang sesuai, nilai label lama, dan nilai label baru yang ingin Anda gunakan
ubah_label_folder('E:/PKM/Ubah_Index/github/Baru2/datasets-vod/labels/valid', 992, 304)
print('val done')