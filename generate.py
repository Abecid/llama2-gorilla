import json
import csv
from tqdm import tqdm
from datetime import datetime
import re

from prompts import template, example as example_prompt
import openai_api

conda = "openai_conda-2023Jun12.json"
linux = "openai_linux-2023Jun13.json"
gcp = "dataset1/openai_gcloud-2023Jun13_fixed.json"
github = "dataset1/openai_github-2023Jun13_fixed.json"

inputs = [gcp, github]

model = "gpt-3.5-turbo"
# model = "gpt-4"

model_clean_name = model.replace(".", "-").replace("/", "_").replace(" ", "_").replace("-", "_")

OpenAI_API = openai_api.OpenAI_API(model=model)
example_api = example_prompt.example

MAX_PER_FILE = 1000
MULTI_OUTPUT = 1

def prase_response(model_reseponse):
    function_call_index = model_reseponse.find("<API Python Call>")
    query = model_reseponse[:function_call_index].replace("<Query>", "").strip()
    function_call = model_reseponse[function_call_index+len("<API Python Call>"):].strip()
    
    return query, function_call
    

def generate_queries_for_file(data, clean_input_name, max_per_file=MAX_PER_FILE, multi_output=MULTI_OUTPUT):
    print(f"Length of data: {len(data)}")
    
    output_data = []
    
    for index, example in enumerate(tqdm(data)):
        if index == max_per_file:
            break
        # print(f"Example {index+1}/{len(data)}")
        
        try:
            example_str = json.dumps(example)
            
            domain = example['domain']
            framework = example['framework']
            functionality = example['functionality']
            name = example['api_name']
            call = example['api_call']
            arguments = example['api_arguments']
            # metadata = json.dumps(example['meta_data'])
            
            # prompt = template.template.format(example, example_str)
            prompt = template.gcp_template.replace("<<EXAMPLES>>", example_prompt.GCP_EXAMPLE).replace("<<API>>", example_str)
            if MULTI_OUTPUT > 1:
                prompt = template.multi_output_template.format(example, example_str, MULTI_OUTPUT)
            
            response = OpenAI_API.chatgpt(prompt)
            # print(response)
            
            if MULTI_OUTPUT > 1:
                # Find the start positions of each "User query<n>"
                positions = [match.start() for match in re.finditer(r'User query', response)]
                # Extract substrings based on these start positions
                responses = [response[positions[i]:positions[i+1]] if i < len(positions) - 1 else response[positions[i]:] for i in range(len(positions))]
                # responses = response.split("\n\n")
                
                for i in range(len(responses)):
                    response = responses[i]
                    user_query_part = response[:response.find("Correct Command")]
                    user_query = user_query_part.split(":")[1].strip()
                    # user_query = response.split("\n")[0].split(": ")[1].strip()
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
                # user_query = response.split("\n")[0].split(": ")[1].strip()
                # model_answer = response.split("\n")[1].split(": ")[1].strip()
                
                user_query, model_answer = prase_response(response)
                
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
    date_string = now.strftime('%m_%d_%H_%M_%S')
    
    with open(f'output/{clean_input_name}_{date_string}.json', 'w') as jsonfile:
        json.dump(output_data, jsonfile, indent=4)

def main():
    for input_file in inputs:
        data = json.load(open(f'input/{input_file}'))
        clean_input_name = input_file.split(".")[0]
        if '/' in clean_input_name:
            clean_input_name = clean_input_name.split('/')[1]
        generate_queries_for_file(data, clean_input_name)


if __name__ == "__main__":
    main()