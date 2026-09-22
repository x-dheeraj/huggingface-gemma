from transformers import pipeline

# creating a pipeline
pipe = pipeline("text-generation", model="google/gemma-3-1b-it")

messages = [
    {"role": "user", "content": "Who are you?"},
]


print(pipe(messages))
