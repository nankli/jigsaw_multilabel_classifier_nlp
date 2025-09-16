# Jigsaw Multilabel Classification with BERT & T5

This repository explores **multi-label text classification** on the [Jigsaw Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge) using **BERT** and **T5**.  

The goal is to classify online comments into overlapping categories:
- Toxic  
- Severe Toxic  
- Obscene  
- Threat  
- Insult  
- Identity Hate  

---

## Models
- **BERT (base-uncased)**  
  Fine-tuned for multi-label classification using a sigmoid output layer.  

- **T5 (Text-to-Text Transfer Transformer)**  
  Reformulated as a text-to-text task (input: comment → output: labels).  

---

## Evaluation
Metrics used:
- **Hamming Loss** (fraction of incorrect labels)  
- **F1-Score** (macro & micro)  
- **ROC-AUC** per label  

---

## Results
| Model | Hamming Loss   | Macro F1   | Micro F1  |
|-------|----------------|------------|------------|
| BERT  | 0.0150         | 0.68       | 0.79       |
| T5    | 0.0021         | 0.47       | 0.73       |

---

## Notes
- **BERT** is efficient and works well for classification.  
- **T5** offers flexibility by framing the task as sequence-to-sequence.   

---

## Nextsteps
- Add RoBERTa and DeBERTa experiments  
- Hyperparameter tuning  
- Data augmentation experiments  

