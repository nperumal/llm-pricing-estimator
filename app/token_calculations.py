import tiktoken

encoders = {
    "encoder" : tiktoken.get_encoding('cl100k_base')
    # "gpt-3.5": tiktoken.encoding_for_model("gpt-3.5-turbo"),
    #"gpt-4": tiktoken.encoding_for_model("gpt-4"),
    # "gpt2": tiktoken.get_encoding("gpt2"),
}

def calculate_text_tokens(text: str, model_name: str) -> int:
    if model_name not in encoders:
        raise ValueError("Unsupported model")
    print(text)
    encoder = encoders[model_name]
    tokens = encoder.encode(text)
    return len(tokens)

def calculate_audio_tokens(audio_file):
    raise NotImplementedError("Audio token calculation is not supported in this environment.")

def calculate_image_tokens(image_file):
    raise NotImplementedError("Image token calculation is not supported in this environment.")
