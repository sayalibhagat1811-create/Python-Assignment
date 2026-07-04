
from functools import reduce

Addition = lambda A, B: A + B

def main():
    Data = [10,20,30,40]

    print("Input Data is :", Data)

    Ans = reduce(Addition, Data)
    print("Addition is :", Ans)

if __name__ == "__main__":
    main()