import os 

def get_files_info(working_directory, directory=None):
    abs_working_directory = os.path.abspath(working_directory)
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        dir_list = os.listdir(target_dir)
        res = []
        for dir in dir_list:
            path = os.path.join(target_dir, dir)
            size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            res.append(f'- {dir}: file_size={size} bytes, is_dir={is_dir}')
        return "\n".join(res[:5])
    except Exception as e:
        return f'Error: {str(e)}'
    
    