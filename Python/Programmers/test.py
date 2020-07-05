


def test(listVal):

    listVal.append(3)
    print("id In : ", id(listVal))

    listVal = [1,4,5]
    print("id In : ", id(listVal))

    listVal.append(5)
    print("id In : ", id(listVal))

listVal = [1,2,3]

print("id : ", id(listVal))
test(listVal)
print("id : ", id(listVal))
print(listVal)