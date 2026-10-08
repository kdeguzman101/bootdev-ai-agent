import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_path: str = os.path.abspath(working_directory)
    full_path: str = os.path.normpath(os.path.join(abs_path, file_path))
    if os.path.commonpath([abs_path, full_path]) != abs_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(full_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    os.makedirs(abs_path, exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes specified content to a file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path of the file we want to write to",
                },
                "content": {
                    "type": "string",
                    "description": "This is the content that we want to write into the file",
                },
            },
        },
        "required": ["file_path", "content"],
    },
}
