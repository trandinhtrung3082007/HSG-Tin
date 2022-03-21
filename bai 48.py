import random as rd
bot = 1 #rd.randint(1,100)
dem = 0
dem2 = 0

while True:
    people = int(input("Số: "))
    def ss(nguoi, may):
        global dem
        global dem2
        if people > bot:
            print("Số bạn lớn hơn số máy")
            dem += 1
            dem2 += 1
                
        elif people < bot:
            print("Số bạn nhỏ hơn số máy")
            dem += 1
            dem2 += 1

        elif people == bot:
            print("Haha bạn giỏi quá")
            exit()

        if dem == 7:
            print("Bạn đã thua")
    ss(people, bot)

    if dem2 == 7:
        print("Bạn có muốn chơi tiếp không? y/n")
        lc = input()
        if str(lc) == "y":
            ss(people, bot)

        elif str(lc) == "n":
            print("Hẹn gặp lại")
            exit()
        else:
            lc = input("Chọn lại: ")