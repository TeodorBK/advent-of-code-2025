def solution(inputFile):
    solution = 0

    lines = inputFile.readlines()
    lines = [line.strip() for line in lines]
    split = lines.index("")

    ranges = []
    for line in lines[:split]:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    ranges.sort()

    merged = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end
    
    merged.append((current_start, current_end))

    solution = sum(end - start + 1 for start, end in merged)
    print("solution:", solution)

solution(open("./input.txt"))