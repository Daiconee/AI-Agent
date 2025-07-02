import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python import *


def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    function_name = function_call_part.name
    args = function_call_part.args
    args["working_directory"] = "./calculator"
    if function_name == "get_files_info":
        result = get_files_info(**args)
    elif function_name == "get_file_content":
        result = get_file_content(**args)
    elif function_name == "write_file":
        result = write_file(**args)     
    elif function_name == "run_python_file":
        result = run_python_file(**args)
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result},
            )
        ],
    )




def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    input = sys.argv
    verbose = False

    if "-v" in input: 
        verbose = True
        input.remove("-v")
    elif "--verbose" in input: 
        verbose = True
        input.remove("--verbose")
        

    if len(input) == 1 and verbose:
        print("please give input with optional flag -v")

    input = (" ").join(input[1:])
    client = genai.Client(api_key=api_key)
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file,
        ]
    )

    messages = [types.Content(parts = [types.Part.from_text(text=input)], role="user")]

    response = client.models.generate_content(
        model = 'gemini-2.0-flash-001', 
        contents = messages,
        config = types.GenerateContentConfig(
            tools = [available_functions],
            system_instruction=system_prompt)
    )

    if response.function_calls:
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose)
            if function_call_result.parts[0].function_response.response:
                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
            else:
                raise Exception("fatal error")

    else:    
        print(response.text)
    if verbose:
        print(f"User prompt: {input}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__=="__main__":
    main()