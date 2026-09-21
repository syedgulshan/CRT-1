import tiktoken
text="generative-AI can create amazing appliacations"
encoding=tiktoken.get_encoding("cl100k_base")
tokens=encoding.encode(text)
print("original Text:")
print(text)
print("\nToken IDs:")
print(tokens)
print("\nNumber of tokens:")
print(len(tokens))
print("\nDecoded tokens")
for token_id in tokens:
    token_text=encoding.decode([token_id])
    print(token_id, "->", repr(token_text))