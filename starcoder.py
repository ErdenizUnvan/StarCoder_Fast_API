import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from text_generation import Client

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder/"
hf_apikey = 'Write Your Hugging Face API KEY'

#HF_TOKEN = os.environ.get(hf_apikey, None)
headers = {"Authorization": f"Bearer {hf_apikey}"}
client = Client(API_URL, headers=headers)

class GenerateRequest(BaseModel):
    prompt: str
    temperature: float = 0.9
    max_new_tokens: int = 1024  # Increase the value here
    top_p: float = 0.95
    repetition_penalty: float = 1.0
    version: str = 'StarCoder'

@app.post('/generate')
def generate(request: GenerateRequest):
    prompt = request.prompt
    temperature = request.temperature
    max_new_tokens = request.max_new_tokens
    top_p = request.top_p
    repetition_penalty = request.repetition_penalty
    version = request.version

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=42,
    )

    response = []
    for output in client.generate(prompt, **generate_kwargs):
        response.append(output)

    return response

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
