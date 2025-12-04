def countVisible(arr):
    count = 0
    for i in arr:
        if i == "@":
            count += 1
    return count



def solution(inputFile): 
    solution = 0
    lines = inputFile.read()
    lineLen = len(lines.splitlines())
    arr = list(lines)
    
    for i in arr:
        if i == '\n':
            arr.remove(i)

    loop = 0
    start = []
    end = []
    for i in arr:
        if loop % lineLen == 0:
            start.append(loop)
        elif loop % lineLen == lineLen - 1:
            end.append(loop)
        loop += 1

    loop = 0
    for i in arr:
        idx = loop
        left = ""
        right = ""
        top = ""
        bottom = ""
        topLeft = ""
        topRight = ""
        bottomLeft = ""
        bottomRight = ""
        
        if idx not in start:
            left = arr[idx - 1]
        if idx not in end:
            right = arr[idx + 1]
        if idx - lineLen >= 0 and idx not in start:
            topLeft = arr[idx - lineLen - 1]
        if idx - lineLen >= 0:
            top = arr[idx - lineLen]
        if idx - lineLen >= 0 and idx not in end:
            topRight = arr[idx - lineLen + 1]
        if idx + lineLen < len(arr) and idx not in start:
            bottomLeft = arr[idx + lineLen - 1]
        if idx + lineLen < len(arr):
            bottom = arr[idx + lineLen]
        if idx + lineLen < len(arr) and idx not in end:
            bottomRight = arr[idx + lineLen + 1]

        if arr[idx] == "@":
            count = countVisible([left, right, top, bottom, topLeft, topRight, bottomLeft, bottomRight])
        else:
            count = 4

        if count < 4:
            print(loop)
            solution += 1
        loop += 1    

    print("solution: ", solution)


solution(open("input.txt"))