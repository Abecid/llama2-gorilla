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
1. The user query must include the required arguments for the API (Especially the filepaths, if they are required for the API. And make these arguments/filepaths as realistic as possible)
2. The user query and correct command should be only separated by one newline ("User query: <Query>\nCorrect Command: <Command>")
3. Generate {} different user queries that are each different and the corresponding correct commands for each just separated by one newline ("User query1: <Query>\nCorrect Command1: <Command>\n\nUser query2: <Query>\nCorrect Command2: <Command>\n...")

Output the user query and the corresponding correct command for the api in the following format (each in one line and separated by one newline):
User query1: <Query>
Correct Command1: <Command>

User query2: <Query>
Correct Command2: <Command>

-----\n
"""