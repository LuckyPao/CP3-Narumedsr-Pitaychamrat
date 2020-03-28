userInput = int(input("Number Line : "))
for i in range(userInput):
    text = ""
    for o in range(1):
        space = userInput - (i+1)
        star = "*"*((2*i)+1)
        text = text + space*" " + star + space*" "
    print(text)
      