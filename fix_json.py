import json

def main(inputs):
    for input in inputs:
        data = []
        with open(f'input/{input}', 'r') as f:
            for line in f:
                try:
                    json_obj = json.loads(line)
                    data.append(json_obj)
                except json.JSONDecodeError:
                    # If there's an error decoding the JSON, simply skip the line
                    print(f"Skipped malformed line: {line.strip()}")
        input = input.replace(".json", "_fixed.json")
        input_path = f"input/{input}"
        with open(f'{input_path}', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

if __name__ == "__main__":
    gcp = "dataset1/openai_gcloud-2023Jun13.json"
    github = "dataset1/openai_github-2023Jun13.json"
    inputs = [gcp, github]
    main(inputs)