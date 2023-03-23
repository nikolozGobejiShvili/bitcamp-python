import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        numbers=(generate_integer(level), generate_integer(level))
        print(numbers[0] , "+", numbers[1], "=",  end= "")

        try:
            r=int(input(""))
            if r == sum(numbers):
                score += 1
            elif r != sum(numbers):
                print("EEE")
        except:
            print("EEE")            


    print("score: "  + str(score))

def get_level():
    while True:
        try:
            n=int(input("level: "))
            if n > 0 and 4 > n:
                break
        except:
            pass

        return n


def generate_integer(level):
    level=random.randint(0,9)
    return level


if __name__ == "__main__":
    main()