text=input("enter your name:")
tokens=text.split()
print("original text:")
print(text)
print("Tokens:")
for i, token in enumerate(tokens):
    print(i, "--------------",token)
print("total tokens:", len(tokens))