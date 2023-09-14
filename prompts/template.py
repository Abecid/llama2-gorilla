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