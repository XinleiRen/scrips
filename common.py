import os
import numpy as np

def get_file_list(folder, key_word, wav_list):
# get files which contains key_word from folder recursively
    
    for file in os.listdir(folder):
        file = os.path.join(folder, file)
        if os.path.isdir(file):
            get_file_list(file, key_word, wav_list)
        else:
            if key_word in file:
                wav_list.append(os.path.join(file))

if __name__ == '__main__':
    # demo of get_file_list()
    file_list = []
    get_file_list('/pictures/', '.png', file_list)
    print(file_list)
