import os


current_path = os.path.abspath(__file__)
parent_path = os.path.join(current_path, '..', '..')


def get_all_paths(path):
    for i_file in os.listdir(path):
        new_path = os.path.join(path, i_file)
        if os.path.isdir(new_path):
            print('Дирекктория -->', i_file)
            get_all_paths(new_path)
        else:
            print(' -', i_file)


get_all_paths(parent_path)
