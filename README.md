# Punctuation API 

## Installation
 
```shell
git lfs install
git clone https://github.com/eleldar/Punctuation.git
cd Punctuation
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
cd models
git clone https://huggingface.co/eleldar/rubert-base-cased-sentence
git clone https://huggingface.co/eleldar/repunct-model_ft repunct-model_ft/weights/ 
```

## Usage

```shell
(venv)$ python main.py
```
open http://127.0.0.1:8000/docs in browser!

## How it works

Before inserting raw text into model it should be tokenized. Library handle it with [`BaseDataset.parse_tokens`](https://github.com/sviperm/neuro-comma/blob/fc89b977b5e3caf866f54f9e2a0d9503869a8a57/src/neuro_comma/dataset.py#L63)

[Model architecture](https://github.com/sviperm/neuro-comma/blob/fc89b977b5e3caf866f54f9e2a0d9503869a8a57/src/neuro_comma/model.py#L15) is pretty easy and straight forward:
 - BERT layer - [DeepPavlov/rubert-base-cased-sentence](https://huggingface.co/DeepPavlov/rubert-base-cased-sentence) language model
 - Bi-LSTM layer - to reduce demsions
 - Linear layer - final layer to predict what symbol should go after token

## Links

[Article on habr.ru](https://habr.com/ru/company/barsgroup/blog/563854/)

This repository contains code (which was edited for production purposes) from [xashru/punctuation-restoration](https://github.com/xashru/punctuation-restoration).
