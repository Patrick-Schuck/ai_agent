from google.genai import types
from functions.get_file_content import schema_get_files_info

available_functions = types.Tool(
    function_declarations=[schema_get_files_info],
)