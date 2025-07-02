import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    if file_path:
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except IOError as e:
        print(f"Error creating file: {e}")

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Replaces content of file if file exists and creates new file with content if file does not exist, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to update or create, path relative to the working directory. If not existing, create new file with and add content.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to put in existing or newly created file.",
            ),
        },
    ),
)