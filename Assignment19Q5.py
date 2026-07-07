from functools import reduce

def CheckPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def main():
    Data = [2, 70, 11, 10, 17, 23, 31, 77]

    FData = list(filter(CheckPrime, Data))
    print("List after filter :", FData)

    MData = list(map(lambda No: No * 2, FData))
    print("List after map :", MData)

    Ret = reduce(lambda A, B: A if A > B else B, MData)
    print("Output of reduce :", Ret)

if __name__ == "__main__":
    main()