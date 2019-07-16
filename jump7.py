for a in range(0,11):
    for b in range(0,10):
        c = 10 * a + b
        if a == 7 or b == 7:
            continue
        elif c % 7 == 0:
            continue
        elif c > 100 or c ==0:
            break
        else:
            print(c)
