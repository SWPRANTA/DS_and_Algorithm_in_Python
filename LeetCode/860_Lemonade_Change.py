def lemonadeChange(bills):
    isOk = True
    income = []
    bills.sort()
    print(bills)
    for item in bills:
        if item == 5:
            income.append(item)
        elif item == 10:
            income.append(item)
            if 5 in income:
                income.remove(5)
            else:
                isOk = False
                break
        else:
            if 5 in income and 10 in income:
                income.remove(10)
                income.remove(5)
            elif income.count(5) >= 3:
                print("in")
                income.remove(5)
                income.remove(5)
                income.remove(5)
            else:
                isOk = False
                break
        print(income)
    return isOk

bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
isOk = lemonadeChange(bills)
print(isOk)