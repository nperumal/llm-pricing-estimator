from pydantic import BaseModel

class TextInput(BaseModel):
    text: str
    model_name: str

class ModelNameInput(BaseModel):
    model_name: str
