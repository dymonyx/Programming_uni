start, result = map(float, input("введите километраж первого и последнего дня: ").split())

def running(start, result):
    now = start
    days = 1
    while result > now:
        now += now/10
        days += 1
    return(days)

print(running(start, result))