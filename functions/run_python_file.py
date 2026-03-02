import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(working_dir_abs,file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs,absolute_file_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(absolute_file_path):
            return  f'Error: "{file_path}" does not exist or is not a regular file'
        if not absolute_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'  
        command = ["python", absolute_file_path]
        if args:
            command.extend(args)  
        completed = subprocess.run(command, cwd=working_dir_abs, capture_output = True,text = True, timeout = 30)
        
        output_lines = []
        if completed.returncode != 0:
            output_lines.append(f"Process exited with code {completed.returncode}")
        if not completed.stdout and not completed.stderr:
            output_lines.append("No output produced")
        if completed.stdout:
            output_lines.append(f"STDOUT:\n{completed.stdout}")
        if completed.stderr:
            output_lines.append(f"STDERR:\n{completed.stderr}")
        return "\n".join(output_lines)
        
    except Exception as e:
        return f"Error: executing Python file: {e}"