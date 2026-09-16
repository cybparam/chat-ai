print("Welcome! :) ")
print("Enter Quit to exit")
while True:
    user = input("Enter Text: ")
    user = user.lower()

    if "quit" in user:
        break

    if "hello" in user:
        bot = "Hello! Greetings :)"
        print("bot:", bot)
    elif "hows going" in user:
        bot = "Great Here Whats good?"
        print("bot:", bot)
    elif "hows going" in user:
        bot = "Great Here Whats good?"
        print("bot:", bot)
    else:
        bot = user
        print("bot:", bot)

print("Thanks For Chatting <3")
