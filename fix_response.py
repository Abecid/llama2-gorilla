import json
import csv
from tqdm import tqdm
from datetime import datetime
import re

from prompts import template
from prompts import example as prompt_examples
import openai_api
import check

conda = "openai_conda-2023Jun12.json"
linux = "openai_linux-2023Jun13.json"
rapidAPI = "rapidAPI-api_09_30_gpt_3_5_turbo.json"
aws = "aws-cli-2023_09_29_gpt_3_5_turbo.json"
output_aws = "aws-cli-2023_09_29_gpt_3_5_turbo_10_08_00_00_cleaned.json"

inputs = [conda, linux]

model = "gpt-3.5-turbo"
model = "gpt-4"

model_clean_name = model.replace(".", "-").replace("/", "_").replace(" ", "_").replace("-", "_")

OpenAI_API = openai_api.OpenAI_API(model=model)

# Function to convert string representation of dict to actual dict
def string_to_dict(s):
    s = "{" + s + "}"
    return json.loads(s.replace("\\", "").replace("'", "\""))

def get_fixed_python_response(model_answer):
    prompt = template.fix_response_to_python.replace("<<<EXAMPLE_API_CALL>>>", model_answer).replace("<<<EXAMPLES>>>", prompt_examples.FIX_RESPONSE_TO_PYTHON)
            
    response = OpenAI_API.chatgpt(prompt).strip()
    return response

def get_fixed_response(model_answer, index):
    i = 0
    while not check.is_parsable(model_answer):
        if i >= 1:
            print(f"{index}-{i+1}. Model Answer Not Parsable: {model_answer}")
        model_answer = get_fixed_python_response(model_answer)
        i += 1
        if i > 2:
            return False, model_answer
    return True, model_answer
            

def fix_python_parsable(data, clean_input_name):
    new_data = []
    skipped_data = []
    for index, json_object in enumerate(tqdm(data)):
        json_object['model_answer'] = json_object['model_answer'].replace("-", "_")
        no_error, json_object['model_answer'] = get_fixed_response(json_object['model_answer'], index)
        
        if no_error is False:
            skipped_data.append(json_object)
        else:
            new_data.append(json_object)
    
    print(f"Number of skipped examples: {len(skipped_data)}/{len(data)}")
    now = datetime.now()
    # Convert to string format
    date_string = now.strftime('%m_%d_%H_%M')
    
    with open(f'output/{clean_input_name}_{date_string}.json', 'w') as jsonfile:
        json.dump(new_data, jsonfile, indent=4)
        
    with open(f'output/{clean_input_name}_{date_string}_skipped.json', 'w') as jsonfile:
        json.dump(skipped_data, jsonfile, indent=4)

def fix_aws(data, clean_input_name, max=-1):
    output_data = []
    
    errors_in_a_row = 0
    errors_dicts = {}
    
    for index, example in enumerate(tqdm(data)):
        # print(f"Example {index+1}/{len(data)}")
        
        if max != -1:
            if len(output_data) >= max:
                break
        
        try:
            original_json = example['original']
            
            name = original_json['api_name']
            arguments = original_json['api_arguments']
            model_answer = example['model_answer']

            original_json['api_name_original'] = name
            original_json['api_arguments_original'] = arguments
            
            argument_descriptions = []
            
            api_name = None
            
            prompt = template.fix_template_2.replace("<<<EXAMPLE_API_CALL>>>", model_answer).replace("<<<EXAMPLES>>>", prompt_examples.AWS_FIX_EXAMPLES)
            
            response = OpenAI_API.chatgpt(prompt)
            
            responses = [r for r in response.split("\n") if len(r) > 0]
            
            if len(responses) == 0:
                continue
            
            api_arguments = []
            
            for response_index, response in enumerate(responses):
                if response_index == 0:
                    api_name = response
                else:
                    if ";" not in response:
                        print(f"; not in Response: {index+1}/{len(data)}")
                        print(f"Response: {response}")
                        continue
                    argument_name = response.split(";")[0].strip()
                    argument_value = response.split(";")[1].strip()
                    argument_description = ""
                    
                    for key, value in original_json['api_arguments_original'].items():
                        if argument_name in key and len(key) - len(argument_name) <= 3:
                            argument_description = value
                            
                    if len(argument_description) == 0:
                        print(f"Argument Description Not Found: {index+1}/{len(data)}")
                        print(f"Argument Name: {argument_name}")
                        api_argument_original = original_json['api_arguments_original']
                        print(f"Original Arguments: {api_argument_original}")
                        continue
                    
                    api_arguments.append({
                        "name": argument_name,
                        "value": argument_value,
                        "description": argument_description
                    })
                            
            original_json['api_name'] = api_name
            original_json['api_arguments'] = api_arguments
            
            example['original'] = original_json
            output_data.append(example)
            
        except Exception as e:
            print(f"Error: {index+1}/{len(data)}")
            print(e)
            if e in errors_dicts:
                errors_dicts[e] += 1
            else:
                errors_dicts[e] = 1
            
            print(f"\n<Response>\n{response}\n")
            errors_in_a_row += 1
            print(f"Errors: {errors_in_a_row}")
            print(f"{errors_dicts}")
            continue
        
    now = datetime.now()
    # Convert to string format
    date_string = now.strftime('%m_%d_%H_%M')
    
    with open(f'output/{clean_input_name}_{date_string}_cleaned.json', 'w') as jsonfile:
        json.dump(output_data, jsonfile, indent=4)

def fix_file(data, clean_input_name):
    output_data = []
    
    errors_in_a_row = 0
    errors_dicts = {}
    
    for index, example in enumerate(tqdm(data)):
        # print(f"Example {index+1}/{len(data)}")
        
        try:
            # example_str = json.dumps(example)
            
            # domain = example['domain']
            # framework = example['framework']
            # functionality = example['functionality']
            
            original_json = example['original']
            
            name = original_json['api_name']
            arguments = original_json['api_arguments']
            model_answer = example['model_answer']
            
            original_json['api_name'] = 'requests.get'
            original_json['api_name_original'] = name
            original_json['api_arguments_original'] = arguments
            
            url_template = {
                "name": "url",
                "type": "string",
                "description": "The endpoint URL to which the API request is made. It specifies the location of the resource on the server.",
                # "default": "Downing Street London"
            }
            
            headers_template = {
                "name": "headers",
                "type": "Dict",
                "description": "Contains metadata sent with the API request. Headers can include authentication tokens, client information, and other key-value pairs to provide context or directives for the request.",
                # "default": "Downing Street London"
            }
            
            params_template = {
                "name": "params",
                "type": "Dict",
                "description": "Parameters passed with the API request, typically used to filter or customize the response. They are included in the URL after a question mark (?).",
                # "default": "Downing Street London"
            }
            
            # # Regular expression patterns
            # url_pattern = r'requests\.get\(\"(.*?)\"'
            # headers_pattern = r'headers=\{(.*?)\}'
            # params_pattern = r'params=\{(.*?)\}'

            # # Extracting URL, headers and params
            # url = re.search(url_pattern, model_answer).group(1)
            # headers_string = re.search(headers_pattern, model_answer).group(1)
            # params_string = re.search(params_pattern, model_answer).group(1)
            
            # headers = string_to_dict(headers_string)
            # params = string_to_dict(params_string)
            
            # prompt = template.fix_template.format(model_answer)
            prompt = template.fix_template.replace("<<<EXAMPLE_APU_CALL>>>", model_answer)
            
            response = OpenAI_API.chatgpt(prompt)
            
            # print(f"\n<Response>\n{response}\n")
            
            lines = response.split("\n")
            if len(lines) < 3:
                print(f"Response Too Short Error: {index+1}/{len(data)}")
                print(f"\n<Response>\n{response}\n")
                continue
            
            # Extract URL
            url = ""
            if "URL" in response:
                # url_section = response[:response.find("Headers")]
                url = response.split('\n')[0].split(":",1)[1].strip()
            else:
                print(f"URL Not Found Error: {index+1}/{len(data)}")
                print(f"<Response>\n{response}\n")
                continue

            # Extract Headers
            headers = {}
            if "Headers" in response:
                headers_section = response[response.find("Headers"):]
                headers_str = headers_section.split('\n')[0].split(":",1)[1].strip()
                if (headers_str[0] != "{" or headers_str[-1] != "}") and "None" not in headers_str:
                    print(f"Headers Not Found Error: {index+1}/{len(data)}")
                    print(f"<Reader>\n{headers_str}\n")
                    continue
                headers = json.loads(headers_str) if headers_str and "None" not in headers_str else {}
            else:
                continue

            # Extract Params
            params = {}
            if "Params" in response:
                params_section = response[response.find("Params"):]
                params_str = params_section.split('\n')[0].split(":",1)[1].strip()
                if (params_str[0] != "{" or params_str[-1] != "}") and "None" not in params_str:
                    print(f"Params Not Found Error: {index+1}/{len(data)}")
                    print(f"<Reader>\n{params_str}\n")
                    continue
                params = json.loads(params_str) if params_str and "None" not in params_str else {}
            else:
                continue

            # # try:
            # url = response.split("\n")[0].split(": ", 1)[1].strip()
            # headers = response.split("\n")[1].split(":", 1)[1].strip()
            # if "None" in headers: headers = {}
            # else:
            #     headers = json.loads(headers)
            # params = response.split("\n")[2].split(":", 1)[1].strip()
            # if "None" in params: params = {}
            # else:
            #     params = json.loads(params)
                
            # print(f"URL: {url}")
            # print(f"Headers: {headers}")
            # print(f"Params: {params}")
            
            url_template['value'] = url
            headers_template['value'] = headers
            params_template['value'] = params
            
            original_json['api_arguments'] = [url_template, headers_template, params_template]
            example['original'] = original_json
            sample_dict = example
            
            output_data.append(sample_dict)
        except Exception as e:
            # print(e)
            print(f"Error: {index+1}/{len(data)}")
            print(e)
            if e in errors_dicts:
                errors_dicts[e] += 1
            else:
                errors_dicts[e] = 1
            
            print(f"\n<Response>\n{response}\n")
            errors_in_a_row += 1
            print(f"Errors in a row: {errors_in_a_row}")
            # if errors_in_a_row > 10:
            #     print("Too many errors in a row. Stopping.")
            #     break
            continue
    now = datetime.now()
    # Convert to string format
    date_string = now.strftime('%m_%d_%H_%M')
    
    with open(f'output/{clean_input_name}_{date_string}_cleaned.json', 'w') as jsonfile:
        json.dump(output_data, jsonfile, indent=4)

def main():
    # input_file = rapidAPI
    # input_file = aws
    # data = json.load(open(f'input/{input_file}'))
    # clean_input_name = input_file.split(".")[0]
    # fix_file(data, clean_input_name)
    # fix_aws(data, clean_input_name)
    
    data = json.load(open(f'output/{output_aws}'))
    clean_input_name = output_aws.split(".")[0]
    fix_python_parsable(data, clean_input_name)
    

if __name__ == "__main__":
    main()