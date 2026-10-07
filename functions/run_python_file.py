import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_path: str = os.path.abspath(working_directory)
        full_path: str = os.path.normpath(os.path.join(abs_path, file_path))
        if os.path.commonpath([abs_path, full_path]) != abs_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not full_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command: list[str] = ["python", full_path]
        if args:
            command.extend(args)
        process = subprocess.run(
            command,
            capture_output=True,
            timeout=30,
            text=True,
            cwd=abs_path,
        )
        output: list[str] = []
        if process.returncode != 0:
            output.append(f'Process exited with code {process.returncode}')
        if not process.stdout and not process.stderr:
            output.append(f'No output produced')
        if process.stdout:
            output.append(f'STDOUT: {process.stdout}')
        if process.stderr:
            output.append(f'STDERR: {process.stderr}')
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
