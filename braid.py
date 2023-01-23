def left_over_mid(row):
    left = row[0]
    mid = row[4]
    right = row[8]
    
    crossing = [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
 
    crossing[0][1] = left
    crossing[0][3] = mid
    crossing[0][8] = right
    crossing[1][2] = left
    crossing[1][8] = right
    crossing[2][1] = mid
    crossing[2][3] = left
    crossing[2][8] = right
    crossing[3][0] = mid
    crossing[3][4] = left
    crossing[3][8] = right
    
    return crossing

def right_over_mid(row):
    left = row[0]
    mid = row[4]
    right = row[8]
    
    crossing = [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]

    crossing[0][0] = left
    crossing[0][5] = mid
    crossing[0][7] = right
    crossing[1][0] = left
    crossing[1][6] = right
    crossing[2][0] = left
    crossing[2][5] = right
    crossing[2][7] = mid
    crossing[3][0] = left
    crossing[3][4] = right
    crossing[3][8] = mid
    
    return crossing

crossings = int(input())
initial = input()
chars = input()
braid = [[chars[0], ".", ".", ".", chars[1], ".", ".", ".", chars[2]]]
current_crossing = initial
for i in range(crossings):
    latest = braid[-1]
    if current_crossing == "left-over-middle":
        result = left_over_mid(latest)
        braid.extend([result[0], result[1], result[2], result[3]])
        current_crossing = "right-over-middle"
    else:
        result = right_over_mid(latest)
        braid.extend([result[0], result[1], result[2], result[3]])
        current_crossing = "left-over-middle"

braid_strings = ["".join(braid[i]) for i in range(len(braid))]

for i in braid_strings:
    print(i)