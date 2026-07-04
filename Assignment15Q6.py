from functools import reduce

Minimum = lambda A, B: A if A < B else B

def main():
    Data = [10,20,50,40,30]

    print("Input Data is :", Data)

    Ans = reduce(Minimum, Data)
    print("Minimum is :", Ans)

if __name__ == "__main__":
    main()