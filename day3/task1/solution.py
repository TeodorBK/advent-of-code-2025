def solution(inputFile):
    input_data = inputFile.read()
    solution = 0

    for line in input_data.splitlines():
        first = 0

        newLine = ""
        second = 0
        for char in line:
            num = int(char)
            if num > first and int(line.index(char)) != len(line) - 1:
                first = num
        
        newLine = line[int(line.index(str(first))) + 1:]

        for char in newLine:
            num = int(char)
            if num > second:
                second = num
        
        battery = str(first) + str(second)
        solution += int(battery)        
    
    print("solution: ", solution)


solution(open("input.txt"))
