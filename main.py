import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_functions import available_functions, call_function
 
def main():
    print("Hello from ai-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("There's no API Key to be found ...")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model ="gemini-2.5-flash",
        contents = messages,
        config = types.GenerateContentConfig(tools=[available_functions],system_instruction = system_prompt))
    if response.usage_metadata:
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls:
        response_list = []
        for func_call in response.function_calls:
            function_call_result=call_function(func_call)
            if not function_call_result.parts:
                raise Exception
            if not function_call_result.parts[0].function_response:
                raise Exception
            if not function_call_result.parts[0].function_response.response:
                raise Exception
            response_list.append(function_call_result.parts[0])
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
