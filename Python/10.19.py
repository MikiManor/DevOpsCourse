from collections import deque

items = deque([])
userInput = input(":")
while userInput != "n":
    userInput = input(": ")
    items.append(userInput)
if items:
    print(items.popleft())
