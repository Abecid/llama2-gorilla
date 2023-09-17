import json
import csv
from tqdm import tqdm
from datetime import datetime
import re

from prompts import template, example as example_prompt
import openai_api

conda = "openai_conda-2023Jun12.json"
linux = "openai_linux-2023Jun13.json"

inputs = [conda, linux]

model = "gpt-3.5-turbo"
# model = "gpt-4"

model_clean_name = model.replace(".", "-").replace("/", "_").replace(" ", "_").replace("-", "_")

OpenAI_API = openai_api.OpenAI_API(model=model)
example_api = example_prompt.example

MAX_PER_FILE = 150
MULTI_OUTPUT = 3

def generate_queries_for_file(data, clean_input_name):
    print(f"Length of data: {len(data)}")
    
    output_data = []
    
    for index, example in enumerate(tqdm(data)):
        if index == MAX_PER_FILE:
            break
        print(f"Example {index+1}/{len(data)}")
        
        try:
            example_str = json.dumps(example)
            
            domain = example['domain']
            framework = example['framework']
            functionality = example['functionality']
            name = example['api_name']
            call = example['api_call']
            arguments = example['api_arguments']
            # metadata = json.dumps(example['meta_data'])
            
            prompt = template.template.format(example, example_str)
            if MULTI_OUTPUT > 1:
                prompt = template.multi_output_template.format(example, example_str, MULTI_OUTPUT)
            
            response = OpenAI_API.chatgpt(prompt)
            print(response)
            
            if MULTI_OUTPUT > 1:
                # Find the start positions of each "User query<n>"
                positions = [match.start() for match in re.finditer(r'User query\d+', response)]
                # Extract substrings based on these start positions
                responses = [response[positions[i]:positions[i+1]] if i < len(positions) - 1 else response[positions[i]:] for i in range(len(positions))]
                # responses = response.split("\n\n")
                
                for i in range(len(responses)):
                    response = responses[i]
                    user_query = response.split("\n")[0].split(": ")[1].strip()
                    model_answer_part = response[response.find("Correct Command"):]
                    model_answer = model_answer_part.split("\n")[0].split(": ")
                    if len(model_answer) > 1: model_answer = model_answer[1].strip()
                    else: model_answer = ""
                    if len(model_answer_part.split("\n")) > 2:
                        # model_answer2 = "\n".join(model_answer_part.split("\n")[1:])
                        model_answer2 = model_answer_part[model_answer_part.find("\n")+1:]
                        model_answer = f"{model_answer}\n{model_answer2}".strip()
                        # if len(model_answer) == 0:
                        #     model_answer = model_answer2
                        # else:
                        #     model_answer = model_answer + "\n" + model_answer2
                        
                    
                    sample_dict = {
                        # 'api_name': name,
                        'query': user_query,
                        'model_answer': model_answer,
                        'original': example
                    }
                    
                    output_data.append(sample_dict)
            else:
                user_query = response.split("\n")[0].split(": ")[1].strip()
                model_answer = response.split("\n")[1].split(": ")[1].strip()
                
                sample_dict = {
                    # 'api_name': name,
                    'query': user_query,
                    'model_answer': model_answer,
                    'original': example
                }
                
                output_data.append(sample_dict)
        except Exception as e:
            print(e)
            continue
    now = datetime.now()
    # Convert to string format
    date_string = now.strftime('%m_%d')
    
    with open(f'output/{clean_input_name}_{date_string}_{model_clean_name}.json', 'w') as jsonfile:
        json.dump(output_data, jsonfile, indent=4)

def main():
    for input_file in inputs:
        data = json.load(open(f'input/{input_file}'))
        clean_input_name = input_file.split(".")[0]
        generate_queries_for_file(data, clean_input_name)


if __name__ == "__main__":
    main()