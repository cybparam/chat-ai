import time
import random
import json

try:
    with open("data.json", "r") as file:
        text_data = json.load(file)
        for words in text_data:
            text_data[words] = {count: int(c) for count, c in text_data[words].items()}
except FileNotFoundError:
    text_data = {}

def reply():
    prediction = text_data[word]
    r = random.random()
    probability = {}
    total, cumulative = 0, 0
    for w in prediction:
        total += prediction[w]
    for w in prediction:
        probability[w] = prediction[w] / total
        cumulative += probability[w]
        if r <= cumulative:
            return w

print("Starting Training mode")
time.sleep(1)

print("In Chatting Mode")
time.sleep(1)
while True:
    print("Type Exit to leave the chat!")
    user = input("Enter Text: ").lower()
    words = user.split()
    if user == "exit":
        break
    else:
        word = words[-1]
        bot = reply()
        print("bot: ", bot)