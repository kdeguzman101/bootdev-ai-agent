import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    abs_path: str = os.path.abspath(working_directory)
    full_path: str = os.path.normpath(os.path.join(abs_path, directory))
    print(f"working dir: {directory}\nfull_path: {full_path}")
    valid_target_dir: bool = os.path.commonpath([abs_path, full_path]) == abs_path
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    else:
        file_details: list[str] = []
        for f in os.listdir(full_path):
            file_details.append(f"- {f}: file_size={os.path.getsize(full_path + "/" + f)} bytes, is_dir={os.path.isdir(full_path + "/" + f)}")
        print(f'Success: "{directory}" is within the working directory')
        return '\n'.join(file_details)
