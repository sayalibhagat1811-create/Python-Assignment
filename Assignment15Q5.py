from functools import reduce

Maximum = lambda A, B: A if A > B else B

def main():
    Data = [10,20,50,40,30]

    print("Input Data is :", Data)

    Ans = reduce(Maximum, Data)
    print("Maximum is :", Ans)

if __name__ == "__main__":
    main()