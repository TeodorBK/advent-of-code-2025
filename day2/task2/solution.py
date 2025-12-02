def solution(inputFile):
    ids = inputFile.read().split(",")

    total = 0

    for id in ids:
        start = id.split("-")[0]
        end = id.split("-")[1]

        for i in range(int(start), int(end) + 1):
            string = str(i)
            length = len(string)

            for block in range(1, length):
                if length % block != 0:
                    continue

                repeat_count = length // block
                if repeat_count < 2:
                    continue

                pattern = string[:block]
                if pattern * repeat_count == string:
                    total += i
                    break

    print("solution:", total)


solution(open("input.txt"))
