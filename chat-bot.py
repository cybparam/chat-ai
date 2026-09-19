import time

def reply():
    prediction = text_data[user]
    prediction = max(prediction, key=prediction.get)
    return prediction

text_data = {}

print("Starting Training mode")
time.sleep(1)
while True:
    print("Type Exit to leave the chat!")
    user = input("Enter Text: ").lower()
    words = user.split()

    if user == "exit":
        time.sleep(1)
        break
    else:
        for i in range(len(words) - 1):
            if words[i] not in text_data:
                text_data[words[i]] = {}
            if words[i + 1] not in text_data[words[i]]:
                text_data[words[i]][words[i + 1]] = 0
            text_data[words[i]][words[i + 1]] += 1

print("In Chatting Mode")
time.sleep(1)
while True:
    print("Type Exit to leave the chat!")
    user = input("Enter Text: ").lower()

    if user == "exit":
        break
    else:
        bot = reply()
        print("AI: ", bot)