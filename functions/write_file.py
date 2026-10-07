import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_path: str = os.path.abspath(working_directory)
    full_path: str = os.path.normpath(os.path.join(abs_path, file_path))
    if os.path.commonpath([abs_path, full_path]) != abs_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(full_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

