from collections import deque

items = deque([])
while True:
    userInput = input(": ")
    if userInput == "n":
        if items:
            print("The first user is : {}".format(items.popleft()))
            continue
        else:
            print("Empty Queue")
            continue
    items.append(userInput)
    print("user {} added".format(userInput))
