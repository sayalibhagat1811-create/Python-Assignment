from functools import reduce

def main():
    Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    FData = list(filter(lambda No: No % 2 == 0, Data))
    print("List after filter :", FData)

    MData = list(map(lambda No: No * No, FData))
    print("List after map :", MData)

    Ret = reduce(lambda A, B: A + B, MData)
    print("Output of reduce :", Ret)

if __name__ == "__main__":
    main()