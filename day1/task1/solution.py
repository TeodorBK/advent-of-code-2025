def solution(inputFile):
    solution = 0
    value = 50
    input_data = inputFile.read()

    for line in input_data.splitlines():
        direction = line[:1]
        lineValue = int(line[1:])

        if direction == "R":
            value = (value + lineValue) % 100
        elif direction == "L":
            value = (value - lineValue) % 100

        if value == 0:
            print(solution)
            solution += 1

    print("solution: ", solution)


solution(open("input.txt"))
