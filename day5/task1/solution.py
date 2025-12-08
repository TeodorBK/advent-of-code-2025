def solution(inputFile): 
    solution = 0

    lines = inputFile.readlines()
    lines = [line.strip() for line in lines]
    split = lines.index("")

    ranges = lines[:split]
    ingredients = lines[split+1:]
    
    ranges = [r.split("-") for r in ranges]

    for ingredient in ingredients:
        for r in ranges:
            start = int(r[0])
            end = int(r[1])

            if int(ingredient) >= start and int(ingredient) <= end:
                solution += 1
                break

            
    
    print("solution: ", solution)


solution(open("input.txt"))