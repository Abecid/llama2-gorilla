# llama2-gorilla
Generate question-answer pairs that use API calls

## 1. Install requirements
```
pip install -r requirements.txt
```

## 2. Add and set input file
1. Add json file of API calls in the "input" folder
2. Set the input filename in generate.py
```python
input_filename = "openai_conda-2023Jun12.json"
```

## 3. Run
```
python generate.py
```