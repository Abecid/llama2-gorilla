import json
import csv
from tqdm import tqdm

from prompts import template, example as example_prompt
import openai_api

conda = "openai_conda-2023Jun12.json"
linux = "openai_linux-2023Jun13.json"

inputs = [linux]

model = "gpt-3.5-turbo"
model = "gpt-4"

OpenAI_API = openai_api.OpenAI_API(model=model)
example_api = example_prompt.example

def generate_queries_for_file(data, clean_input_name):
    print(f"Length of data: {len(data)}")
    
    output_data = []
    
    for index, example in enumerate(tqdm(data)):
        if index == 5:
            break
        print(f"Example {index+1}/{len(data)}")
        example_str = json.dumps(example)
        
        domain = example['domain']
        framework = example['framework']
        functionality = example['functionality']
        name = example['api_name']
        call = example['api_call']
        arguments = example['api_arguments']
        # metadata = json.dumps(example['meta_data'])
        
        prompt = template.template.format(example, example_str)
        
        response = OpenAI_API.chatgpt(prompt)
        print(response)
        
        user_query = response.split("\n")[0].split(": ")[1].strip()
        model_answer = response.split("\n")[1].split(": ")[1].strip()
        
        sample_dict = {
            # 'api_name': name,
            'query': user_query,
            'model_answer': model_answer,
            'original': example
        }
        
        output_data.append(sample_dict)
    
    with open(f'output/{clean_input_name}.json', 'w') as jsonfile:
        json.dump(output_data, jsonfile, indent=4)

def main():
    for input_file in inputs:
        data = json.load(open(f'input/{input_file}'))
        clean_input_name = input_file.split(".")[0]
        generate_queries_for_file(data, clean_input_name)


if __name__ == "__main__":
    main()