import json

try:
    with open("data.json", "r") as file:
        text_data = json.load(file)
        for words in text_data:
            text_data[words] = {count: int(c) for count, c in text_data[words].items()}
except FileNotFoundError:
    text_data = {}

while True:
    print("Type Exit to leave the chat!")
    user = input("Enter Text: ").lower()
    words = user.split()

    if user == "exit":
        break
    else:
        for i in range(len(words) - 2):
            context = words[i] + " " + words[i+1]
            next_word = words[i + 2]
            if context not in text_data:
                text_data[context] = {}
            if next_word not in text_data[words[i]]:
                text_data[context][next_word] = 0
            text_data[context][next_word] += 1

with open("data.json", "w") as file:
    json.dump(text_data, file, indent=4)