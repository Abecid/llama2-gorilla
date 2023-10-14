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
"""