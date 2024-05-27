with open("input.txt", "r") as gets:
    procentils = []
    gets_arr = gets.readlines()
    for get in gets_arr:
        get_arr = list(get.split())
        if int(get_arr[6]) < 500:
            procentils.append(get_arr[8])
    procentils = sorted(procentils)
    print(procentils[int(len(procentils)*0.75)-1])