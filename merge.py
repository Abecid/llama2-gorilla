import json
import os

root_dir = 'output/dataset1'
sub_dirs = [f'{root_dir}/original', f'{root_dir}/additional1', f'{root_dir}/additional2']
filenames = ['aws-cli-2023_09_29_gpt_3_5_turbo_10_08_00_00_cleaned_10_12_20_48_additional_fixed_fixed.json',
             'openai_gcloud-2023Jun13_fixed_10_19_fixed_fixed.json',
             'openai_github-2023Jun13_fixed_10_19_fixed_fixed.json',
             'rapidAPI-api_09_30_gpt_3_5_turbo_10_06_18_53_cleaned_additional_fixed_fixedArguments_fixed.json',
             'rapidAPI-api_09_30_gpt_3_5_turbo_10_06_18_53_cleaned_fixed_fixed.json'
             ]

combined_dir = f'{root_dir}/combined'

# Ensure the combined directory exists
if not os.path.exists(combined_dir):
    os.mkdir(combined_dir)

def main():
    # Loop through each filename
    for filename in filenames:
        combined_data = []

        # Read and combine data from root and subfolders
        for dir in sub_dirs:
            file_path = os.path.join(dir, filename)
            with open(file_path, 'r') as f:
                data = json.load(f)
                combined_data.extend(data)  # extend the list

        # Write the merged data to the combined directory
        combined_path = os.path.join(combined_dir, filename)
        with open(combined_path, 'w') as f:
            json.dump(combined_data, f, indent=4)

if __name__ == "__main__":
    main()