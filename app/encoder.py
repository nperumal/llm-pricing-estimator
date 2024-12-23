import torch
from transformers import BertTokenizer, BertModel

# Load pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
model = BertModel.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# Input text
input_text = "Nalla"

# Tokenize input
inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)

# Get encoder outputs (hidden states)
with torch.no_grad():
    outputs = model(**inputs)

# The encoder output consists of hidden states for each token
# outputs[0] contains the last hidden states (a tensor of shape [batch_size, sequence_length, hidden_size])
hidden_states = outputs[0]

# Show hidden states for each token
print(hidden_states.shape)  # Shape: [1, sequence_length, hidden_size]
print(hidden_states)