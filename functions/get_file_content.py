from config import MAX_CHARS
import os

def get_file_content(working_directory: str, file_path: str) -> str:
    abs_path: str = os.path.abspath(working_directory)
    full_path: str = os.path.normpath(os.path.join(abs_path, file_path))
    valid_target_dir: bool = os.path.commonpath([abs_path, full_path]) == abs_path
    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(full_path, "r", encoding="utf-8") as f:
        content: str = f.read(MAX_CHARS)
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
