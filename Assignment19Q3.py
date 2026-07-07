from functools import reduce

def main():
    Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    FData = list(filter(lambda No: No >= 70 and No <= 90, Data))
    print("List after filter :", FData)

    MData = list(map(lambda No: No + 10, FData))
    print("List after map :", MData)

    Ret = reduce(lambda A, B: A * B, MData)
    print("Output of reduce :", Ret)

if __name__ == "__main__":
    main()