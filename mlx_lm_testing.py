from mlx_lm import load, generate
import time
# model, tokenizer = load("mlx-community/quantized-gemma-7b-it")
model, tokenizer = load("mlx-community/OpenHermes-2.5-Mistral-7B")
t = time.perf_counter()
response = generate(model, tokenizer, prompt="Write me a python function to automatically solve caesar ciphers", verbose=True, max_tokens = 200)
print(time.perf_counter()-t)