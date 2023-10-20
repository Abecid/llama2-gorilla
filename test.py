import re
import json
import ast

def check_aws():
    string = "aws.docdb.describe_engine_default_cluster_parameters(db_parameter_group_family=\"docdb3.6\", max_records=50)"
    string = "aws.apigateway.get_domain_name(domain_name=\"my-api.example.com\")"
    string = "aws.sso_admin.provision_permission_set(instance_arn=\"arn:aws:sso::123456789012:instance/MyInstance\", permission_set_arn=\"arn:aws:sso::123456789012:permissionSet/MyPermissionSet\", target_id=\"987654321098\", target_type=\"AWS_ACCOUNT\")"
    string = "aws.ec2.associate_enclave_certificate_iam_role(certificate_arn=\"arn:aws:acm:us_west_2:123456789012:certificate/12345678_1234_1234_1234_123456789012\", role_arn=\"arn:aws:iam::123456789012:role/NitroEnclaveRole\")"
    pattern = re.compile(r'(\w+)=["\']?([^"\']+)["\']?')
    # Finding all matches
    matches = pattern.findall(string)

    # Extracting to dictionary
    parameters = {key: value for key, value in matches}
    print(parameters)
    
    example_dict = {
        "api_arguments": [
                {
                    "name": "certificate-arn",
                    "enum": [
                        "arn"
                    ],
                    "description": "\nThe ARN of the ACM certificate with which to associate the IAM role."
                },
                {
                    "name": "role-arn",
                    "enum": [
                        "arn"
                    ],
                    "description": "\nThe ARN of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certificate."
                }
            ]
    }
    
    skip = False
    for api_argument in example_dict['api_arguments']:
        found = False
        for parameter_key in parameters.keys():
            if api_argument['name'].replace('-', '_') in parameter_key:
                api_argument['enum'] = [parameters[parameter_key].replace(')', '')]
                found = True
                break
        if found == False:
            print(f"Could not find {api_argument['name']} ")
            skip = True

def check_rapid():
    string = "requests.get(\"https://check-disposable-email.p.rapidapi.com/api/disposable\", headers={\"X-RapidAPI-Key\": \"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"check-disposable-email.p.rapidapi.com\"}, params={\"email\": \"test@example.com\"})"
    pattern = re.compile(r'requests\.get\("(.*?)", headers=(\{.*?\}), params=(\{.*?\})\)')

    # Extract the relevant sections of the string
    match = pattern.search(string)
    url, headers, params = match.groups()
    
    api_arguments = [
        {"name": "url", "type": "string", "description": "The endpoint URL to which the API request is made. It specifies the location of the resource on the server.", "enum": [url]},
        {"name": "headers", "type": "Dict", "description": "Contains metadata sent with the API request. Headers can include authentication tokens, client information, and other key-value pairs to provide context or directives for the request.", "enum": [json.loads(headers)]},
        {"name": "params", "type": "Dict", "description": "Parameters passed with the API request, typically used to filter or customize the response. They are included in the URL after a question mark (?).", "enum": [json.loads(params)]}
    ]
    print(api_arguments)
    print('\n')
    
    pattern = re.compile(r'requests\.get\("(.*?)", headers=(\{.*?\}), params=(\{.*?\})\)')

    # Extract the relevant sections of the string
    match = pattern.search(string)
    if match is None:
        print(f"No match found in model answer: {string}")
    url, headers, params = match.groups()

    api_arguments = [
        {"name": "url", "type": "string", "description": "The endpoint URL to which the API request is made. It specifies the location of the resource on the server.", "enum": [url]},
        {"name": "headers", "type": "Dict", "description": "Contains metadata sent with the API request. Headers can include authentication tokens, client information, and other key-value pairs to provide context or directives for the request.", "enum": [json.loads(headers)]},
        {"name": "params", "type": "Dict", "description": "Parameters passed with the API request, typically used to filter or customize the response. They are included in the URL after a question mark (?).", "enum": [json.loads(params)]}
    ]
    print(api_arguments)

def len_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
        print(len(data))

def check_ast():
    ex1 = "requests.get(\"https://check-disposable-email.p.rapidapi.com/api/disposable\", headers={\"X-RapidAPI-Key\" \"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"check-disposable-email.p.rapidapi.com\"}, params={\"email\" \"example@gmail.com\"})User query: I want to check the item with ASIN:B09DKV849B on Amazon in the U.S. marketplace.Correct Command: requests.get(\"https://amazon-live-data.p.rapidapi.com/getasin/us/B07WDSD7G7\", headers={\"X-RapidAPI-Key\": \"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"amazon-live-data.p.rapidapi.com\"}, params={\"asin\": \"B09DKV849B\", \"locale\":\"us\"})User query: I want to call the test pg prod API.Correct Command: requests.get(\"https://test-pg-prod.p.rapidapi.com/\", headers={\"X-RapidAPI-Key\": \"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"test-pg-prod.p.rapidapi.com\"}, params={})"
    ex2 = "requests.get(\"https://uk-postcode.p.rapidapi.com/search\", headers={\"X-RapidAPI-Key\" \"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"uk-postcode.p.rapidapi.com\"}, params={\"q\" \"123 Main Street\", \"limit\" 5})"
    ex3 = "aws.chime-sdk-voice.update-voice-profile-domain(voice-profile-domain-id=1234, name=\"New Name\", description=\"New Description\")"
    ast.parse(ex3)
    

def main():
    # check_rapid()
    # check_ast()
    len_json("output/aws-cli-2023_09_29_gpt_3_5_turbo_10_08_00_00_cleaned_10_12_20_48_additional_fixed_fixed.json")

if __name__ == "__main__":
    main()