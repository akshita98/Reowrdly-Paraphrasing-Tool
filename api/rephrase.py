import torch
from transformers import T5ForConditionalGeneration
from transformers import AutoTokenizer

global model
global device
global tokenizer

def loadModel():
    best_model_path = "/Users/sainikhitanayani/Desktop/rewordly/BestModel"
    global model, tokenizer, device
    model = T5ForConditionalGeneration.from_pretrained(best_model_path)
    tokenizer = AutoTokenizer.from_pretrained("s-nlp/t5-paraphrase-paws-msrp-opinosis-paranmt")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    set_seed(42)

def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def rephraseText(sentence):
    text =  "paraphrase: " + sentence + " </s>"
    encoding = tokenizer.encode_plus(text, pad_to_max_length=True, return_tensors="pt")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)

    beam_outputs = model.generate(
        input_ids=input_ids, attention_mask=attention_masks,
        do_sample=True,
        max_length=256,
        top_k=120,
        top_p=0.98,
        early_stopping=True,
        num_return_sequences=1
    )
    final_outputs =[]
    for beam_output in beam_outputs:
        sent = tokenizer.decode(beam_output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
        if sent.lower() != sentence.lower() and sent not in final_outputs:
            return sent