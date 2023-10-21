example = """
<<<user>>>: clean up the conda environment.
<<<reference>>>: "{
        "domain": "Data Science",
        "framework": "conda",
        "functionality": "Removes unused packages and caches in the conda environment.",
        "api_name": "clean",
        "api_call": "conda clean [OPTIONS]",
        "api_arguments": [
          {"-a, --all": "Remove index cache, lock files, unused cache packages, tarballs, and logfiles."},
          {"-i, --index-cache": "Remove index cache."},
          {"-p, --packages": "Remove unused packages from writable package caches."},
          {"-t, --tarballs": "Remove cached package tarballs."},
          {"-f, --force-pkgs-dirs": "Remove all writable package caches."},
          {"-c, --tempfiles": "Remove temporary files."},
          {"-l, --logfiles": "Remove log files."},
          {"--json": "Report all output as json."},
          {"-v, --verbose": "Can be used multiple times. Once for INFO, twice for DEBUG, three times for TRACE."},
          {"-q, --quiet": "Do not display progress bar."},
          {"-d, --dry-run": "Only display what would have been done."},
          {"-y, --yes": "Sets any confirmation values to 'yes' automatically."}
        ],
        "python_environment_requirements": ["conda"],
        "example_code": [],
        "meta_data": {
          "description": "A command line interface function in conda that allows users to remove unnecessary files and packages, clean up caches and manage output and flow control."
        }
    }"
<<<Model Answer>>>: conda clean 
"""

REST_EXAMPLE = """
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

REST_FIX_EXAMPLE = """
{
    "query": "Can you find the UK postal addresses for the query \"123 Main Street\" and limit the results to 5?",
    "model_answer": "requests.get(\"https://uk-postcode.p.rapidapi.com/search\", headers={\"X-RapidAPI-Key\" \"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"uk-postcode.p.rapidapi.com\"}, params={\"q\" \"123 Main Street\", \"limit\" 5})",
    "original": {
        "domain": "Location",
        "framework": "RapidAPI",
        "functionality": "Integrate this API with your website's address form to quickly and accurately auto-fill UK postal addresses or find locations of addresses. This API contains a database of almost 1.7 million UK postcodes, along with address and location information.\n\nFor a simple demo, visit https://tomwimmenhove.com/ukpostcode/",
        "api_name": "UK Postcode",
        "api_call": "import requests\n\nurl = 'https://uk-postcode.p.rapidapi.com/search'\nquerystring = {\"q\": \"\", \"limit\": \"\"}\n\nheaders = {\n            \"X-RapidAPI-Key\": \"TO BE FILLED\",\n            \"X-RapidAPI-Host\": \"https://uk-postcode.p.rapidapi.com/search\"\n        }\n\nresponse = requests.get(url, headers=headers, params=querystring)\nprint(response.json())\n",
        "api_arguments": [
            {
                "name": "q",
                "type": "STRING",
                "description": "The query string",
                "default": "Downing Street London"
            },
            {
                "name": "limit",
                "type": "NUMBER",
                "description": "The maximum number of results of the query (May be artificially limited)",
                "default": "10"
            }
        ],
        "python_environment_requirements": [
            "requests"
        ],
        "example_code": "import requests\n\nurl = \"https://uk-postcode.p.rapidapi.com/search\"\nquerystring = {\"q\": \"Downing Street London\", \"limit\": \"10\"}\n\nheaders = {\n            \"X-RapidAPI-Key\": \"SIGN-UP-FOR-KEY\",\n            \"X-RapidAPI-Host\": \"uk-postcode.p.rapidapi.com\"\n        }\n\nresponse = requests.get(url, headers=headers, params=querystring)\nprint(response.json())\n",
        "metadata": []
    }
}
<<Model Response>>
URL: https://uk-postcode.p.rapidapi.com/search
Headers: {"X-RapidAPI-Key": "SIGN-UP-FOR-KEY","X-RapidAPI-Host":"uk-postcode.p.rapidapi.com/search"}
Parameters: {"q": "123 Main Street", "limit": 5}
"""

RAPID_FIX_EXAMPLES = """
<API call>
requests.get(\"https://company-consultation-reportero-industrial-mexicano-api.p.rapidapi.com/products/search\", headers={\"X-RapidAPI-Key\" \"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"company-consultation-reportero-industrial-mexicano-api.p.rapidapi.com\"}, params={\"name\" \"computer\"})
<Response>
URL: https://company-consultation-reportero-industrial-mexicano-api.p.rapidapi.com/products/search\
Headers: {\"X-RapidAPI-Key\":\"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"company-consultation-reportero-industrial-mexicano-api.p.rapidapi.com\"}
Params: {\"name\":\"computer\"}
<API call>
requests.get(\"https://youtoosound.p.rapidapi.com/\", headers={\"X-RapidAPI-Key\" \"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"youtoosound.p.rapidapi.com\"})
<Response>
URL: https://youtoosound.p.rapidapi.com/
Headers: {\"X-RapidAPI-Key\":\"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"youtoosound.p.rapidapi.com\"}
Params: None
<API call>
requests.get(\"https://numberstoletters.p.rapidapi.com/convert\", headers={\"X-RapidAPI-Key\" \"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"numberstoletters.p.rapidapi.com\", params={\"moneda\" \"PESOS\", \"monto\":\"1000\"})
<Response>
URL: https://numberstoletters.p.rapidapi.com/convert
Headers: {\"X-RapidAPI-Key\":\"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"numberstoletters.p.rapidapi.com\"}
Params: {\"moneda\":\"PESOS\",\"monto\":\"1000\"}
<API call>
requests.get(\"https://numberstoletters.p.rapidapi.com/convert\", headers={\"X-RapidAPI-Key\" \"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"numberstoletters.p.rapidapi.com\", params={\"moneda\" \"PESOS\", \"monto\":\"1000\"})
<Response>
URL: https://numberstoletters.p.rapidapi.com/convert
Headers: {\"X-RapidAPI-Key\":\"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"numberstoletters.p.rapidapi.com\"}
Params: {\"moneda\":\"PESOS\",\"monto\":\"1000\"}
<API call>
requests.get(\"https://changenow-crypto-exchange.p.rapidapi.com/v1/exchange-range/fixed-rate/btc_eth\", headers={\"X-RapidAPI-Key\" \"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"changenow-crypto-exchange.p.rapidapi.com\", params={\"from_to\" \"btc_eth\", \"api_key\":\"your_api_key\", \"useRateId\":\"true\"})
<Response>
URL: https://changenow-crypto-exchange.p.rapidapi.com/v1/exchange-range/fixed-rate/btc_eth
Headers: {\"X-RapidAPI-Key\":\"SIGN-UP-FOR-KEY\",\"X-RapidAPI-Host\":\"changenow-crypto-exchange.p.rapidapi.com\"}
Params: {\"from_to\":\"btc_eth\",\"api_key\":\"your_api_key\",\"useRateId\":\"true\"}
"""


AWS_FIX_EXAMPLES = """
<API call>
aws.mediaconnect.list_entitlements()
<Response>
aws.mediaconnect.list_entitlements
<API call>
aws.ecs.put_account_setting(name=serviceLongArnFormat, value = \"enabled\")
<Response>
aws.ecs.put_account_setting
name; serviceLongArnFormat
value; enabled
<API call>
aws.kinesis.describe-stream-summary(stream-name=samplestream)
<Response>
aws.kinesis.describe-stream-summary
stream-name; samplestream
"""

FIX_RESPONSE_TO_PYTHON = """
<API call>
aws.lambda.list-code-signing-configs
<Response>
aws.lambda.list_code_signing_configs()
<API call>
aws.emr-containers.list-job-runs --virtual-cluster-id VC-123 --created-after 2022-01-01 --states COMPLETED
<Response>
aws.emr_containers.list_job-runs(virtual_cluster_id="VC-123", created_after="2022-01-01", states="COMPLETED")
<API call>
import requests\n\nurl = \"https://check-disposable-email.p.rapidapi.com/api/disposable\"\nquerystring = {\"email\": \"example@gmail.com\"}\n\nheaders = {\n            \"X-RapidAPI-Key\": \"SIGN-UP-FOR-KEY\",\n            \"X-RapidAPI-Host\": \"makeup.p.rapidapi.com\"\n        }\n\nresponse = requests.get(url, headers=headers, params=querystring)\nprint(response.json())\n
<Response>
requests.get(\"https://check-disposable-email.p.rapidapi.com/api/disposable\", headers={\"X-RapidAPI-Key\": \"SIGN-UP-FOR-KEY\", \"X-RapidAPI-Host\": \"check-disposable-email.p.rapidapi.com\"}, params={\"email\": \"example@gmail.com\"})
<API call>
gcloud.ai.endpoints.raw_predict(ENDPOINT="123", --region="us-central1", --request="@input.json")
<Response>
gcloud.ai.endpoints.raw_predict(ENDPOINT="123", region="us-central1", request="@input.json")
"""

SYNTHETIC_REQUEST_GENERATION = """
<DICT1>
{
    "query": "I want to create a new user with the name John Doe in an organization with the ID org1234 in AWS WorkMail.",
    "model_answer": "aws.workmail.create_user(organization_id=\"org1234\", name=\"John Doe\", display_name=\"John Doe\", password=\"abcd1234\")",
    "original": {
        "domain": "Cloud Infrastructure",
        "framework": "aws",
        "functionality": "Creates a user who can be used in WorkMail by calling the  RegisterToWorkMail operation.",
        "api_name": "aws.workmail.create-user",
        "api_call": "aws workmail create-user [OPTIONS]",
        "api_arguments": [
            {
                "name": "organization-id",
                "description": "\nThe identifier of the organization for which the user is created.",
                "enum": [
                    "org1234"
                ]
            },
            {
                "name": "name",
                "description": "\nThe name for the new user. WorkMail directory user names have a maximum length of 64. All others have a maximum length of 20.",
                "enum": [
                    "John Doe"
                ]
            },
            {
                "name": "display-name",
                "description": "\nThe display name for the new user.",
                "enum": [
                    "John Doe"
                ]
            },
            {
                "name": "password",
                "description": "\nThe password for the new user.",
                "enum": [
                    "abcd1234"
                ]
            }
        ],
        "python_environment_requirements": [
            "aws"
        ],
        "example_code": [
            "aws workmail create-user     --organization-id m-d281d0a2fd824be5b6cd3d3ce909fd27     --name exampleName     --display-name exampleDisplayName     --password examplePa$$w0rd\n"
        ],
        "output": {
            "UserId -> (string)": "\nThe identifier for the new user."
        },
        "api_name_original": "create-user",
        "api_arguments_original": {
            "--organization-id ": "\nThe identifier of the organization for which the user is created.",
            "--name ": "\nThe name for the new user. WorkMail directory user names have a maximum length of 64. All others have a maximum length of 20.",
            "--display-name ": "\nThe display name for the new user.",
            "--password ": "\nThe password for the new user."
        }
    }
}
<New Query>
I want to create a new user with the name Jane Smith, a display name of Jane S, in an organization with the ID org5678, and set the password to 'securePass123' in AWS WorkMail."
<New Model Answer>
aws.workmail.create_user(organization_id="org5678", name="Jane Smith", display_name="Jane S", password="securePass123")

<DICT2>
{
    "query": "I want to list all the entitlements for my AWS account.",
    "model_answer": "aws.mediaconnect.list_entitlements()",
    "original": {
        "domain": "Cloud Infrastructure",
        "framework": "aws",
        "functionality": "Displays a list of all entitlements that have been granted to this account. This request returns 20 results per page.list-entitlements is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the --no-paginate argument.",
        "api_name": "aws.mediaconnect.list_entitlements",
        "api_call": "aws mediaconnect list-entitlements [OPTIONS]",
        "api_arguments": [],
        "python_environment_requirements": [
            "aws"
        ],
        "example_code": [
            "aws mediaconnect list-entitlements\n"
        ],
        "output": {
            "Entitlements -> (list)": "\nA list of entitlements that have been granted to you from other AWS accounts.\n(structure)\n\nAn entitlement that has been granted to you from other AWS accounts.\nDataTransferSubscriberFeePercent -> (integer)\n\nPercentage from 0-100 of the data transfer cost to be billed to the subscriber.\nEntitlementArn -> (string)\n\nThe ARN of the entitlement.\nEntitlementName -> (string)\n\nThe name of the entitlement.\n\n",
            "NextToken -> (string)": "\nThe token that identifies which batch of results that you want to see. For example, you submit a ListEntitlements request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListEntitlements request a second time and specify the NextToken value."
        },
        "api_name_original": "list-entitlements",
        "api_arguments_original": {
            "--starting-token ": "\nA token to specify where to start paginating. This is the NextToken from a previously truncated response.\nFor usage examples, see Pagination in the AWS Command Line Interface User Guide .\n",
            "--page-size ": "\nThe size of each page to get in the AWS service call. This does not affect the number of items returned in the command\u00e2\u0080\u0099s output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.\nFor usage examples, see Pagination in the AWS Command Line Interface User Guide .\n"
        }
    }
}
<New Query>
I want to list the entitlements for my AWS account but retrieve the results in smaller pages of 5 items each.
<New Model Answer>
aws.mediaconnect.list_entitlements(page_size=5)

<DICT3>
{
    "query": "What are the available powers for an Amazon Lightsail container service?",
    "model_answer": "aws.lightsail.get_container_service_powers()",
    "original": {
        "domain": "Cloud Infrastructure",
        "framework": "aws",
        "functionality": "Returns the list of powers that can be specified for your Amazon Lightsail container services.See also: AWS API Documentation\n",
        "api_name": "aws.lightsail.get-container-service-powers",
        "api_call": "aws lightsail get-container-service-powers [OPTIONS]",
        "api_arguments": [],
        "python_environment_requirements": [
            "aws"
        ],
        "example_code": [],
        "output": {
            "powers -> (list)": "\nAn array of objects that describe the powers that can be specified for a container service.\n(structure)\n\nDescribes the powers that can be specified for an Amazon Lightsail container service.\nThe power specifies the amount of RAM, the number of vCPUs, and the base price of the container service.\npowerId -> (string)\n\nThe ID of the power (e.g., nano-1 ).\nprice -> (float)\n\nThe monthly price of the power in USD.\ncpuCount -> (float)\n\nThe number of vCPUs included in the power.\nramSizeInGb -> (float)\n\nThe amount of RAM (in GB) of the power.\nname -> (string)\n\nThe friendly name of the power (e.g., nano ).\nisActive -> (boolean)\n\nA Boolean value indicating whether the power is active and can be specified for container services.\n\n"
        },
        "api_name_original": "get-container-service-powers",
        "api_arguments_original": {}
    }
}
<New Query>
Can you provide a Python function call to obtain the available power options for Lightsail container services and log the output, considering that we might want to automate a monthly check and get notified about possible updates or changes in the power options?
<New Model Answer>
aws.lightsail.get_container_service_powers()
"""

GCP_EXAMPLE = """
<API1>
{
    "domain": "Cloud Infrastructure",
    "framework": "aws",
    "functionality": "Displays a list of all entitlements that have been granted to this account. This request returns 20 results per page.list-entitlements is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the --no-paginate argument.",
    "api_name": "aws.mediaconnect.list_entitlements",
    "api_call": "aws mediaconnect list-entitlements [OPTIONS]",
    "api_arguments": [
        {
            "name": "page-size",
            "enum": [
                "10"
            ],
            "description": "\nThe size of each page to get in the AWS service call. This does not affect the number of items returned in the command\u00e2\u0080\u0099s output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.\nFor usage examples, see Pagination in the AWS Command Line Interface User Guide .\n"
        }
    ],
    "python_environment_requirements": [
        "aws"
    ],
    "example_code": [
        "aws mediaconnect list-entitlements\n"
    ],
    "output": {
        "Entitlements -> (list)": "\nA list of entitlements that have been granted to you from other AWS accounts.\n(structure)\n\nAn entitlement that has been granted to you from other AWS accounts.\nDataTransferSubscriberFeePercent -> (integer)\n\nPercentage from 0-100 of the data transfer cost to be billed to the subscriber.\nEntitlementArn -> (string)\n\nThe ARN of the entitlement.\nEntitlementName -> (string)\n\nThe name of the entitlement.\n\n",
        "NextToken -> (string)": "\nThe token that identifies which batch of results that you want to see. For example, you submit a ListEntitlements request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListEntitlements request a second time and specify the NextToken value."
    },
    "api_name_original": "list-entitlements",
    "api_arguments_original": {
        "--starting-token ": "\nA token to specify where to start paginating. This is the NextToken from a previously truncated response.\nFor usage examples, see Pagination in the AWS Command Line Interface User Guide .\n",
        "--page-size ": "\nThe size of each page to get in the AWS service call. This does not affect the number of items returned in the command\u00e2\u0080\u0099s output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.\nFor usage examples, see Pagination in the AWS Command Line Interface User Guide .\n",
        "--max-items ": "\nThe total number of items to return in the command\u00e2\u0080\u0099s output. If the total number of items available is more than the value specified, a NextToken is provided in the command\u00e2\u0080\u0099s output. To resume pagination, provide the NextToken value in the starting-token argument of a subsequent command. Do not use the NextToken response element directly outside of the AWS CLI.\nFor usage examples, see Pagination in the AWS Command Line Interface User Guide .\n"
    }
}
<Query1>
I want to list the entitlements for my AWS account, but only retrieve the first 10 results.
<API Python Call1>
aws.mediaconnect.list_entitlements(page_size=10)

<API2>
{
    "domain": "Cloud Infrastructure",
    "framework": "aws",
    "functionality": "Get detailed data for a service instance. A service instance is an instantiation of service template and it runs in a specific environment.",
    "api_name": "aws.proton.get-service-instance",
    "api_call": "aws proton get-service-instance [OPTIONS]",
    "api_arguments": [
        {
            "name": "name",
            "enum": [
                "instance-two"
            ],
            "description": "\nThe name of a service instance that you want to get the detailed data for."
        },
        {
            "name": "service-name",
            "enum": [
                "simple-svc"
            ],
            "description": "\nThe name of the service that you want the service instance input for."
        }
    ],
    "python_environment_requirements": [
        "aws"
    ],
    "example_code": [
        "aws proton get-service-instance     --name \"instance-one\"     --service-name \"simple-svc\"\n"
    ],
    "output": {
        "serviceInstance -> (structure)": "\nThe detailed data of the requested service instance.\narn -> (string)\n\nThe Amazon Resource Name (ARN) of the service instance.\ncreatedAt -> (timestamp)\n\nThe time when the service instance was created.\ndeploymentStatus -> (string)\n\nThe service instance deployment status.\ndeploymentStatusMessage -> (string)\n\nThe message associated with the service instance deployment status.\nenvironmentName -> (string)\n\nThe name of the environment that the service instance was deployed into.\nlastAttemptedDeploymentId -> (string)\n\nThe ID of the last attempted deployment of this service instance.\nlastClientRequestToken -> (string)\n\nThe last client request token received.\nlastDeploymentAttemptedAt -> (timestamp)\n\nThe time when a deployment of the service instance was last attempted.\nlastDeploymentSucceededAt -> (timestamp)\n\nThe time when the service instance was last deployed successfully.\nlastSucceededDeploymentId -> (string)\n\nThe ID of the last successful deployment of this service instance.\nname -> (string)\n\nThe name of the service instance.\nserviceName -> (string)\n\nThe name of the service that the service instance belongs to.\nspec -> (string)\n\nThe service spec that was used to create the service instance.\ntemplateMajorVersion -> (string)\n\nThe major version of the service template that was used to create the service instance.\ntemplateMinorVersion -> (string)\n\nThe minor version of the service template that was used to create the service instance.\ntemplateName -> (string)\n\nThe name of the service template that was used to create the service instance.\n"
    },
    "api_name_original": "get-service-instance",
    "api_arguments_original": {
        "--name ": "\nThe name of a service instance that you want to get the detailed data for.",
        "--service-name ": "\nThe name of the service that you want the service instance input for."
    }
}
<Query2>
I want to get the detailed data for a service instance named instance-two for the service simple-svc on AWS Proton.
<API Python Call2>
aws.proton.get_service_instance(name=\"instance-two\", service_name=\"simple-svc\")
"""