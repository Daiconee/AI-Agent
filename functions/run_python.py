import os 
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    abs_working_directory = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File "{file_path}" not found.'
    try:
        result = subprocess.run(["python3", target_file], timeout=30)
        
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        if result.returncode != 0:
            print("Process exited with code", result.returncode)
        return
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, path relative to the working directory. If not provided, or nonexistent, gives error.",
            ),
        },
    ),
)