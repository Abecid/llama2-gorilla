example = """
Prompt:
<<<user>>>: clean up the conda environment. <<<reference>>>: "{
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

Model Answer: 
conda clean 
"""