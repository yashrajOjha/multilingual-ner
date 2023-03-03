from transformers import AutoTokenizer
xlmr_tokenizer = AutoTokenizer.from_pretrained("cfilt/HiNER-original-xlm-roberta-large")
xlmr_tokenizer.save_pretrained("./tokenizer/")