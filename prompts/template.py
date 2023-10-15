template = """
Create an example user query that requires the use of the provided API and also create the corresponding correct command (or function call) given the following example

Example:
{}

API:
{}

Rules
1. The user query must include the required arguments for the API (Especially the filepaths, if they are required for the API. And make these arguments/filepaths as realistic as possible)
2. The user query and correct command should be only separated by one newline ("User query: <Query>\nCorrect Command: <Command>")

Output the user query and the corresponding correct command for the api in the following format (each in one line and separated by one newline):
User query: <Query>
Correct Command: <Command>

-----\n
"""

multi_output_template = """
Create an example user query that requires the use of the provided API and also create the corresponding correct command (or function call) given the following example

Example:
{}

API:
{}

Rules
1. The user query must include the required arguments for the API. Especially the filepaths and filenames, if they are required for the API. And make these arguments/filepaths are as realistic as possible. For example, 
2. The user query and correct command should be only separated by one newline ("User query: <Query>\nCorrect Command: <Command>")
3. Generate {} different user queries that are each different and the corresponding correct commands for each just separated by one newline ("User query1: <Query>\nCorrect Command1: <Command>\n\nUser query2: <Query>\nCorrect Command2: <Command>\n...")

Output the user query and the corresponding correct command for the api in the following format (each in one line and separated by one newline):
User query1: <Query>
Correct Command1: <Command>

User query2: <Query>
Correct Command2: <Command>

-----\n
"""

selfcheck_template = """
The rules
1. Query should include the required arguments
2. The output should be separated by one newline

API

Results

Do the results match the rules?
If not fix them and try again
"""

fix_template = """
Extract the url (string), headers (valid json format) and params (valid json format) from the following API call

Examples:
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



<API call>
<<<EXAMPLE_APU_CALL>>>
<Response>
"""

fix_template_2 = """
Return the name of the function that is being called and the arguments that are being passed in (the name of the argument and the value separated by a ';') each separated by one newline like the following examples
This format (<Response>)
function_name
parameter_name; parameter_value; parameter_description

Examples:
<<<EXAMPLES>>>

<API call>
<<<EXAMPLE_API_CALL>>>
<Response>
"""

fix_response_to_python = """
Return the given API Call (terminal command/function call) in the correct Python function calling format with the correct Python syntax given the following example:

Examples:
<<<EXAMPLES>>>

<API Call>
<<<EXAMPLE_API_CALL>>>
<Response>
"""

create_additional_queries = """
Refer to the following examples and create another realistic query that can be accomplished by executing the python function (api_name) using different argument permutations and argument values (But you can not use arguments not mentioned in the json! But feel free to use any arguments in api_arguments_original accordingly while adhering to its description and mention the used arguments in key:value format). The generated model_answer should be a one-line, valid execution of a python function, with correct python syntax that calls the API correctly, aligned with the query. 

<Examples>
<<<EXAMPLES>>>

<Dict>
<<<DICT>>>
<New Query>
"""