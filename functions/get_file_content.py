def get_file_content(working_directory: str, file_path: str) -> str:
    abs_path: str = os.path.abspath(working_directory)
    full_path: str = os.path.normpath(os.path.join(abs_path, file_path))
    valid_target_dir: bool = os.path.commonpath([abs_path, full_path]) == abs_path
    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(full_path):
        f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        file_details: list[str] = []
        for f in os.listdir(full_path):
            file_details.append(f"- {f}: file_size={os.path.getsize(full_path + "/" + f)} bytes, is_dir={os.path.isdir(full_path + "/" + f)}")
        print(f'Success: "{directory}" is within the working directory')
        return '\n'.join(file_details)
