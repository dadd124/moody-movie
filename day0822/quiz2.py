
run = 0

i = 0
while run < 10:
    run = run + 1
    i = i + 1
    print(f"{i}바퀴")

    if run == 5:
        print("절반")

    elif run == 9:
        print("마지막")
    elif run == 10:
        
        print("완주")
    else:
        print("돈다.")