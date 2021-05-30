def analyzeCoverCross(lsst):
    encode = {"I": 0, "S": 1, "E": 2, "M": 3}
    state = lsst[1][1:5]
    transition = lsst[1][11]
    lst = [None, None, None, None, None, None]

    lst[0] = encode[state[3]]
    lst[1] = encode[state[2]]
    lst[2] = encode[state[1]]
    lst[3] = encode[state[0]]
    lst[4] = int(transition)//2
    lst[5] = int(transition) - lst[4]*2

    return lst



def cleanList(lst):
    lsst = []
    for elemnt in lst:
        if elemnt != "":
            lsst.append(elemnt)
    return lsst


def getCoveredCrosses():
    c = 0
    covered = []
    # cnt = 0
    with open("fcover_report.txt", "r") as f:
        contents = f.read().split("\n")
        cnt = 0
        for line in contents:
            # print(line)
            if line[0:len("            b")] == "            b":
                # print(line)
                c += 1
                ls = line.split(" ")
                lsst = cleanList(ls)
                # cnt += 1



                if(lsst[5] == "Covered"):
                    # print(f"{lsst} {analyzeCoverCross(lsst)}")
                    covered.append(analyzeCoverCross(lsst))
                    # cnt += 1
            else:
                if c > 1:
                    break
        # print(cnt)
    return covered

# print(getCoveredCrosses())
