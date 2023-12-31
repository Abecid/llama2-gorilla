import json
import ast
import os

filename = "aws-cli-2023_09_29_gpt_3_5_turbo_10_08_00_00_cleaned_10_12_20_48.json"

def check_string(code_str):
    """Check if a string has correct Python syntax."""
    parsable = is_parsable(code_str)
    print(f"{code_str}: {parsable}")

def is_parsable(code_str):
    """Check if a string has correct Python syntax."""
    try:
        ast.parse(code_str)
        return True
    except SyntaxError:
        return False

def count_non_parsable_apis(data):
    """Count the number of APIs in the JSON file with incorrect Python syntax."""
    non_parsable_count = 0

    for obj in data:
        model_answer = obj.get('model_answer', '')
        model_answer = model_answer.replace('-', '_')
        if not is_parsable(model_answer):
            non_parsable_count += 1

    return non_parsable_count

def check_json_length(input):
    """Check the length of the JSON file."""
    with open(input, 'r') as f:
        data = json.load(f)
    # print(len(data))
    return len(data)

def check_jsons_length(inputs):
    if isinstance(inputs, str):
        path = inputs
        inputs = []
        for filename in os.listdir(path):
            if filename.endswith('.json'):
                file_path = os.path.join(path, filename)
                inputs.append(file_path)
    
    total = 0
    for input in inputs:
        total += check_json_length(input)
    print(total)

def main():
    # Path to your JSON file
    # file_path = f'output/{filename}'
    # with open(file_path, 'r') as f:
    #     data = json.load(f)
    # num_errors = count_non_parsable_apis(data)
    # print(f"Number of APIs with incorrect syntax: {num_errors}/{len(data)}")
    
    check_jsons_length('/Users/abecid/Downloads/Berkeley/BAIR/Tianjun/data/train_dataset1')

if __name__ == "__main__":
    main()
    # test_str = "aws.kinesis.describe-stream-summary(stream-name=samplestream)"
    # test_str = "aws.kinesis.describe_stream_summary(stream-name=samplestream)"
    # test_str = "aws.kinesis.describe_stream_summary(stream_name=samplestream)"
    # test_str = "aws.ecs.put_account_setting(name=serviceLongArnFormat, value = \"enabled\")"
    # test_str = "aws.list_code_signing_configs()"
    # check_string(test_str)