table = [["-1"] * 50 for _ in range(50)]
merged = []

def merged_check(r,c):
    for merge in merged:
        if merge[0] <= r <= merge[2] and merge[1] <= c <= merge[3]:
            return merge
    return [-1, -1, -1, -1]

def update_1(r, c, value):
    r1, c1, r2, c2 = merged_check(r,c)
    if r1 == -1:
        table[r][c] = value
    else:
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                table[i][j] = value

def update_2(value_1,value_2):
    for t in table:
        for i in t:
            i.replace(value_1, value_2)

def merge(r1, c1, r2, c2):
    if table[r1][c1] is not None:
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                table[i][j] = table[r1][c1]
    elif table[r2][c2] is not None:
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                table[i][j] = table[r1][c1]
    merged.append([r1,c1,r2,c2])
    return

def unmerge(r,c):
    r1, c1, r2, c2 = merged_check(r,c)
    if r1 == -1:
        return
    tmp = table[r][c]
    merged.pop([r1, c1, r2, c2])
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            table[i][j] = '-1'
    table[r][c] = tmp

def print_table(r,c):
    if table[r][c] != '-1':
        print(table[r][c])
    else:
        print("EMPTY")

def solution(commands):
    answer = []
    # print(table)
    for com in commands:
        # for t in table:
        #     print(t, end = "\n")
        # print("\n")
        target = com.split(" ")
        # print(target)
        if target[0] == 'UPDATE':
            if len(target) == 4:
                update_1(int(target[1])-1, int(target[2])-1, target[3])
            else:
                update_2(target[1], target[2])
        elif target[0] == 'MERGE':
            merge(int(target[1])-1, int(target[2])-1, int(target[3])-1, int(target[4])-1)
        elif target[0] == 'UNMERGE':
            for t in table:
                print(t, end = "\n")
            print("\n")
            unmerge(int(target[1])-1, int(target[2])-1)
            for t in table:
                print(t, end = "\n")
            print("\n")
        elif target[0] == 'PRINT':
            print_table(int(target[1])-1, int(target[2])-1)
    # for t in table:
    #     print(t, end = "\n")
    # print("\n")
    table[2:][:1] = 'a'
    return answer

asdf = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]

solution(asdf)
