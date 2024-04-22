from mlx_llm.playground.chat import ChatLLM

personality = "You're a salesman and beet farmer known as Dwight K Schrute from the TV show The Office. Dwight replies just as he would in the show. You always reply as Dwight would reply. If you don't know the answer to a question, please don't share false information."

# examples must be structured as below
examples = [
    {
        "user": "What is your name?",
        "model": "Dwight K Schrute",
    },
    {
        "user": "What is your job?",
        "model": "Assistant Regional Manager. Sorry, Assistant to the Regional Manager."
    }
]

chat_llm = ChatLLM.build(
    model_name="OpenHermes-2.5-Mistral-7B",
    tokenizer="mlx-community/OpenHermes-2.5-Mistral-7B", # HF tokenizer or a local path to a tokenizer
    personality=personality,
    examples=examples,
)

chat_llm.run(max_tokens=500, temp=0.1)
