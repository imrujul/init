with open('alice.txt',encoding='utf-8') as f:
    alice = f.read()

print(type(alice))
alice = alice.replace("Alice","sumit")
alice = alice.replace('”','')
alice = alice.capitalize()

alice = alice.upper()
alice = alice.lower()

print(alice)
# sentences = alice.split('.')

# for sentence in sentences:
#     print(sentence)