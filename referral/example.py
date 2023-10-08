example = """
<<<user>>>: I want to delete a cluster named my-new-cluster on AWS memoryDB. 
<<<reference>>>: "{
        "domain": "Cloud Infrastructure",
        "framework": "aws",
        "functionality": "Deletes a cluster. It also deletes all associated nodes and node endpoints",
        "api_name": "delete-cluster",
        "api_call": "aws memorydb delete-cluster [OPTIONS]",
        "api_arguments": {
            "--cluster-name ": "\nThe name of the cluster to be deleted",
            "--final-snapshot-name ": "\nThe user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward."
        },
        "python_environment_requirements": [
            "aws"
        ],
        "example_code": [
            "aws memorydb delete-cluster     --cluster-name my-new-cluster\n"
        ],
        "output": {
        }
    }}"
<<<Model Answer>>>: aws.memorydb.delete-cluster(cluster-name="my-new-cluster")
"""
rest_example = """
Example 1:
<<<user>>>: I want to check example@gmail.com is a valid email address.
<<<reference>>>: "{
        "domain": "Commerce",
        "framework": "RapidAPI",
        "functionality": "Easily check if a certain e-mail address is valid. Is it a valid domain? Is the e-mail a temporary/disposable e-mail? That\u2019s a common indicator of spamming/trolling, so now there\u2019s an API for you so you can easily block it!",
        "api_name": "Check Disposable Email",
        "api_call": "import requests\n\nurl = 'https://check-disposable-email.p.rapidapi.com/api/disposable'\nquerystring = {\"email\": \"\"}\n\nheaders = {\n            \"X-RapidAPI-Key\": \"TO BE FILLED\",\n            \"X-RapidAPI-Host\": \"https://check-disposable-email.p.rapidapi.com/api/disposable\"\n        }\n\nresponse = requests.get(url, headers=headers, params=querystring)\nprint(response.json())\n",
        "api_arguments": [
            {
                "name": "email",
                "type": "STRING",
                "description": "Email to check disposable.",
                "default": "info@peekdomain.com"
            }
        ],
        "python_environment_requirements": [
            "requests"
        ],
        "example_code": "import requests\n\nurl = \"https://check-disposable-email.p.rapidapi.com/api/disposable\"\nquerystring = {\"email\": \"info@peekdomain.com\"}\n\nheaders = {\n            \"X-RapidAPI-Key\": \"SIGN-UP-FOR-KEY\",\n            \"X-RapidAPI-Host\": \"check-disposable-email.p.rapidapi.com\"\n        }\n\nresponse = requests.get(url, headers=headers, params=querystring)\nprint(response.json())\n",
        "metadata": []
    }"
<<<Model Answer>>>: requests.get("https://check-disposable-email.p.rapidapi.com/api/disposable", headers={"X-RapidAPI-Key": "SIGN-UP-FOR-KEY","X-RapidAPI-Host":"check-disposable-email.p.rapidapi.com", params={"email": "example@gmail.com"})
Example 2:
<<<user>>>: I want check this item ASIN:B09DKV849B on Amazon in U.S. marketplace.
<<<reference>>>: "{
        "domain": "Commerce",
        "framework": "RapidAPI",
        "functionality": "Get Amazon Live Data - Fast and reliable - The best for dropshipping",
        "api_name": "Amazon Live Data",
        "api_call": "import requests\n\nurl = 'https://amazon-live-data.p.rapidapi.com/getasin/us/B07WDSD7G7'\nquerystring = {\"asin\": \"\", \"locale\": \"\"}\n\nheaders = {\n            \"X-RapidAPI-Key\": \"TO BE FILLED\",\n            \"X-RapidAPI-Host\": \"https://amazon-live-data.p.rapidapi.com/getasin/us/B07WDSD7G7\"\n        }\n\nresponse = requests.get(url, headers=headers, params=querystring)\nprint(response.json())\n",
        "api_arguments": [
            {
                "name": "asin",
                "type": "string",
                "description": "",
                "default": "B07WDSD7G7"
            },
            {
                "name": "locale",
                "type": "string",
                "description": "",
                "default": "us"
            }
        ],
        "python_environment_requirements": [
            "requests"
        ],
        "example_code": "import requests\n\nurl = \"https://amazon-live-data.p.rapidapi.com/getasin/us/B07WDSD7G7\"\n\nheaders = {\n            \"X-RapidAPI-Key\": \"SIGN-UP-FOR-KEY\",\n            \"X-RapidAPI-Host\": \"amazon-live-data.p.rapidapi.com\"\n        }\n\nresponse = requests.get(url, headers=headers)\nprint(response.json())\n",
        "metadata": []
    }"
<<<Model Answer>>>: requests.get("https://amazon-live-data.p.rapidapi.com/getasin/us/B07WDSD7G7", headers={"X-RapidAPI-Key": "SIGN-UP-FOR-KEY","X-RapidAPI-Host":"amazon-live-data.p.rapidapi.com", params={"asin": "B09DKV849B", "locale":"en_US"})
"""
azure_example= """
Example 1:
<<<user>>>: I want to create a product named "abc" which relates to service "def" and require approval in Azure API Management.
<<<reference>>>: "{"domain": "Azure", "framework": "az", "functionality": "Create a product in Azure API Management", "api_name": "API Management Product Create", "api_call": "az apim product create --product-name --resource-group --service-name [--approval-required {false, true}] [--description] [--legal-terms] [--no-wait] [--product-id] [--state {notPublished, published}] [--subscription-required {false, true}] [--subscriptions-limit]", "api_arguments": {"required": ["--product-name", "--resource-group", "--service-name"], "optional": ["--approval-required", "--description", "--legal-terms", "--no-wait", "--product-id", "--state", "--subscription-required", "--subscriptions-limit"]}, "python_environment_requirements": [], "example_code": [{"description": "Create a product", "code": "az apim product create --resource-group MyResourceGroup --service-name MyServiceName --product-id MyProductID --product-name MyProductName --description MyDescription --legal-terms MyTerms --subscription-required true --approval-required true --subscriptions-limit 8 --state \"published\""}], "description": "The 'az apim product create' command is used to create a new product in Azure API Management. A product is a packaging of one or more APIs and specifies the terms of usage. The command requires the product name, resource group, and service name. It also accepts optional parameters such as approval required, description, legal terms, no wait, product id, state, subscription required, and subscriptions limit."}"
<<<Model Answer>>>: azure.apim.product.create(product-name="abc",service-name="def",approval-required=True)
Example 2:
<<<user>>>: Create a linked service in Azure Synapse at workspace "workspace name" with name "example" to linked to json file "./path/to/example.json".
<<<reference>>>: "{"domain": "Azure", "framework": "az", "functionality": "Create a linked service in Azure Synapse", "api_name": "Synapse Linked-Service Creation", "api_call": "az synapse linked-service create --workspace-name <workspace_name> --name <linked_service_name> --file <file_path.json>", "api_arguments": {"required": {"--file": "Properties may be supplied from a JSON file using the @{path} syntax or a JSON string.", "--name": "The linked service name.", "--workspace-name": "The workspace name."}, "optional": {"--no-wait": "Do not wait for the long-running operation to finish. Default value: False", "--debug": "Increase logging verbosity to show all debug logs.", "--help": "Show this help message and exit.", "--only-show-errors": "Only show errors, suppressing warnings.", "--output": "Output format.", "--query": "JMESPath query string.", "--subscription": "Name or ID of subscription. You can configure the default subscription using az account set -s NAME_OR_ID.", "--verbose": "Increase logging verbosity. Use --debug for full debug logs."}}, "python_environment_requirements": "Azure CLI", "example_code": [{"description": "Create a linked service. Pay attention to add '@' at the front of the file path as the best practice for complex arguments like JSON string.", "code": "az synapse linked-service create --workspace-name testsynapseworkspace --name testlinkedservice --file @'path/linkedservice.json'"}], "description": "The Azure Synapse Linked-Service Creation API allows users to create a linked service in Azure Synapse. A linked service is a data source or a compute service that allows Azure Synapse to connect to the data within the service. The user needs to provide the workspace name, linked service name, and a JSON file with the properties of the linked service. The command also has several optional parameters that modify the command's output and behavior."}"
<<<Model Answer>>>: azure.synapse.linked-service.create(workspace-name="workspace name", name="example ",file="./path/to/example.json")"
"""
baidu_example= """
Example 1:
<<<user>>>: I had a dream that I jumped from a seven floor building. Can you help me interpret this dream?
<<<reference>>>:"{\n    \"domain\": \"Dream Interpretation\",\n    \"framework\": \"Baidu\",\n    \"functionality\": \"Interpretation of dreams based on keywords\",\n    \"api_name\": \"ZhouGong Dream Interpretation\",\n    \"api_call\": \"import requests\\nif __name__ == '__main__':\\n    url = 'http://gwgp-gjjifhqt3mv.n.bdcloudapi.com/dream/search'\\n    params = {}\\n    params['keyword'] = ''\\n    params['pagenum'] = ''\\n    params['pagesize'] = ''\\n    headers = {\\n        'Content-Type': 'application/json;charset=UTF-8',\\n        'X-Bce-Signature': 'AppCode/YourAppCode'\\n    }\\n    r = requests.request(\\\"GET\\\", url, params=params, headers=headers)\\n    print(r.content)\",\n    \"required_api_arguments\": {\n        \"keyword\": \"\",\n        \"pagenum\": \"\",\n        \"pagesize\": \"\"\n    },\n    \"optional_api_arguments\": {},\n    \"api_arguments_type\": {\n        \"keyword\": \"string\",\n        \"pagenum\": \"integer\",\n        \"pagesize\": \"integer\"\n    },\n    \"python_environment_requirements\": [\"requests\"],\n    \"example_code\": [\n        {\n            \"description\": \"Example of ZhouGong Dream Interpretation API call\",\n            \"code\": \"import requests\\nif __name__ == '__main__':\\n    url = 'http://gwgp-gjjifhqt3mv.n.bdcloudapi.com/dream/search'\\n    params = {}\\n    params['keyword'] = ''\\n    params['pagenum'] = ''\\n    params['pagesize'] = ''\\n    headers = {\\n        'Content-Type': 'application/json;charset=UTF-8',\\n        'X-Bce-Signature': 'AppCode/YourAppCode'\\n    }\\n    r = requests.request(\\\"GET\\\", url, params=params, headers=headers)\\n    print(r.content)\"\n        }\n    ],\n    \"description\": \"The Baidu ZhouGong Dream Interpretation API allows users to search for interpretations of their dreams based on specific keywords. The API returns results in a paginated format.\"\n}"
<<<Model Answer>>>: requests.request("GET", 'http://gwgp-gjjifhqt3mv.n.bdcloudapi.com/dream/search', params={'keyword'="I jumped from a seven floor building",pagenum='1',pagesize='10'}, headers={'Content-Type': 'application/json;charset=UTF-8','X-Bce-Signature': 'AppCode/YourAppAppCode'
    })
Example 2:
"{\n    \"domain\": \"Weather Forecasting Service\",\n    \"framework\": \"Baidu\",\n    \"functionality\": \"Provides real-time weather forecast\",\n    \"api_name\": \"Real-time Weather Forecast\",\n    \"api_call\": \"#!/usr/bin/env python\\n# -*- coding: utf-8 -*-\\n\\nimport requests\\n\\n# Real-time Weather Forecast Python Example Code\\nif __name__ == '__main__':\\n    url = 'http://getweather.api.bdymkt.com/lundear/weather1d'\\n    params = {}\\n    params['areaCn'] = ''\\n    params['areaCode'] = ''\\n    params['ip'] = ''\\n    params['lat'] = ''\\n    params['lng'] = ''\\n    params['need3hour'] = ''\\n    params['needIndex'] = ''\\n    params['needObserve'] = ''\\n    params['needalarm'] = ''\\n    \\n    headers = {\\n        'Content-Type': 'application/json;charset=UTF-8',\\n        'X-Bce-Signature': 'AppCode/YourAppCode'\\n    }\\n    r = requests.request('GET', url, params=params, headers=headers)\\n    print(r.content)\",\n    \"required_api_arguments\": {\n        \"areaCn\": \"\",\n        \"areaCode\": \"\",\n        \"ip\": \"\",\n        \"lat\": \"\",\n        \"lng\": \"\"\n    },\n    \"optional_api_arguments\": {\n        \"need3hour\": \"\",\n        \"needIndex\": \"\",\n        \"needObserve\": \"\",\n        \"needalarm\": \"\"\n    },\n    \"api_arguments_type\": {\n        \"areaCn\": \"String\",\n        \"areaCode\": \"String\",\n        \"ip\": \"String\",\n        \"lat\": \"String\",\n        \"lng\": \"String\",\n        \"need3hour\": \"String\",\n        \"needIndex\": \"String\",\n        \"needObserve\": \"String\",\n        \"needalarm\": \"String\"\n    },\n    \"python_environment_requirements\": {\n        \"requests\": \"2.25.1\"\n    },\n    \"example_code\": [\n        {\n            \"description\": \"Python example code for real-time weather forecast\",\n            \"code\": \"#!/usr/bin/env python\\n# -*- coding: utf-8 -*-\\n\\nimport requests\\n\\n# Real-time Weather Forecast Python Example Code\\nif __name__ == '__main__':\\n    url = 'http://getweather.api.bdymkt.com/lundear/weather1d'\\n    params = {}\\n    params['areaCn'] = ''\\n    params['areaCode'] = ''\\n    params['ip'] = ''\\n    params['lat'] = ''\\n    params['lng'] = ''\\n    params['need3hour'] = ''\\n    params['needIndex'] = ''\\n    params['needObserve'] = ''\\n    params['needalarm'] = ''\\n    \\n    headers = {\\n        'Content-Type': 'application/json;charset=UTF-8',\\n        'X-Bce-Signature': 'AppCode/YourAppCode'\\n    }\\n    r = requests.request('GET', url, params=params, headers=headers)\\n    print(r.content)\"\n        }\n    ],\n    \"description\": \"The Baidu Real-time Weather Forecast API provides real-time weather forecast for a given location. It supports parameters like area name, area code, IP, latitude, longitude, and options to include 3-hour forecast, index, observation, and alarm.\"\n}"

"""