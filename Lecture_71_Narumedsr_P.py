menuList = []
menuLsPrice = []

def showBill():
    print("----LuckyPao Restaurant----")
    for number in range(len(menuList)):
        print(menuList[number],menuLsPrice[number])

def totalCaculate():
    for i in range(len(menuList)):
        i += i
    print("Total Price :",i)

while True:
    menuName = input("Please Enter your Menu : ")
    if (menuName.lower() == "exit") :
        break
    else:
        menuPrice = input("Enter Price : ")
        menuList.append(menuName)
        menuLsPrice.append(menuPrice)
showBill()
totalCaculate()
