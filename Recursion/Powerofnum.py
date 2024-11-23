def powerofnum(base,power):
    if power!=0:
        return base*powerofnum(base,power-1)
    else:
        return 1

if __name__=='__main__':
    base=3
    power=3
    print(powerofnum(base,power))