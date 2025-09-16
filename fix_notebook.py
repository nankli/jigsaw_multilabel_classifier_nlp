import json

with open('fixed_Jigsaw_multilabels_BERT.ipynb', 'r') as f:
    notebook = json.load(f)

if 'widgets' in notebook.get('metadata', {}):
    del notebook['metadata']['widgets']

for cell in notebook.get('cells', []):
    if 'widgets' in cell.get('metadata', {}):
        del cell['metadata']['widgets']

with open('fixed_Jigsaw_multilabels_BERT_cleaned.ipynb', 'w') as f:
    json.dump(notebook, f, indent=2)
