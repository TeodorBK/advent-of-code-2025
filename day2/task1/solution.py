def solution(inputFile):
    ids = inputFile.read().split(",")

    solution = 0

    for id in ids:
        start = id.split("-")[0]
        end = id.split("-")[1]
        
        for i in range(int(start), int(end) + 1):
            string = str(i)
            list = [char for char in string]
            
            if len(list) % 2 == 0:
                if list[:len(list)//2] == list[len(list)//2:]:
                    solution = solution + int(string)
                    
    print("solution: ", solution)


solution(open("input.txt"))
