def getBattery(line, batterySize):
    digits = list(map(int, line))
    
    result = []
    n = len(digits)
    
    for i in range(n):

        while result and digits[i] > result[-1] and len(result) + (n - i) > batterySize:
            result.pop()
        if len(result) < batterySize:
            result.append(digits[i])
    
    battery = int(''.join(map(str, result)))
    return battery


def solution(inputFile):
    input_data = inputFile.read()
    solution = 0

    for line in input_data.splitlines():
        battery = getBattery(line, 12)
        solution += battery
        
    print("Solution: ", solution)


# Run with your input file
solution(open("input.txt"))
