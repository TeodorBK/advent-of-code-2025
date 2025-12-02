def solution(inputFile):
    solution_count = 0
    value = 50
    input_data = inputFile.read()

    for line in input_data.splitlines():
        direction = line[:1]
        lineValue = int(line[1:])
        
        if direction == 'R':
            passes = (value + lineValue)//100
            value = (value + lineValue)%100
            
        elif direction == 'L':
            flipped_value = (100-value)%100 
            passes = (flipped_value + lineValue)//100
            value = (value - lineValue)%100
    
        solution_count += passes


    print("Solution:", solution_count)


solution(open("input.txt"))
