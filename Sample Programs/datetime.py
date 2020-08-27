from datetime import datetime
    def timeanddates():
    x = datetime.now()
    print("start time", x)
    while True:
        try:
            start = int(input("enter the starting value:"))
            while True:
                try:
                    ending = int(input("enter the ending value:"))
                except ValueError as e:
                    print("invalid input ,please enter a integer value ")
                    continue
                else:
                    break
        except ValueError as e:
            print("Invalid input,please enter a integer value ")
            continue
        else:
            break
    list_1 = []
    list_2 = []
    list_3 = []
    dic = {}
    for i in range(start, ending + 1):
        list_1.append(i)
    print(list_1)
    while True:
        try:
            start_1 = int(input("enter the starting value"))

            while True:
                try:
                    ending_1 = int(input("enter the ending value:"))
                except ValueError as e:
                    print("invalid input,please enter a integer value ")
                    continue
                else:
                    break
        except ValueError as e:
            print("invalid input,please enter a integer value ")
            continue
        else:
            break
    if ending >= start_1:
        for j in range(start_1, ending_1):
            list_2.append(j)
        print(list_2)
    else:
        print("the list cant be created")
    for k in list_2:
        list_3 = []
        while k != 0:
            for l in list_1:
                if l // k == l % k:
                    list_3.append(l)
                dic[k] = eval(f"{list_3}")
            k = 0
    print(dic)
    f = open("diction.txt", 'w')
    f.write(f"{list_1, list_2, list_3, dic}")
    print("File created successfully")
    f.close()
    y = datetime.now()
    print("end time", y)
    z = y - x
    print("Difference is", z)
