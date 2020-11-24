grid = [
    []
]

def create_grid(n):
    start = int(n/2)
    for i in range(n):
        if i == start:
            grid[0].append(1)
        else:
            grid[0].append(0)
    for _ in range(n):
        grid.append([])

    for i in range(1,len(grid)):
        for _ in range(n):
            grid[i].append(0)
    return grid


#111 / 110 / 101 / 100 / 011 / 010 / 001 / 000

rules = [1,1,1,1,1,0,1,0]   # <- Change here to change rules
                            # remarkable rules https://mathworld.wolfram.com/ElementaryCellularAutomaton.html


def evolution(gd,rule):
    for j in range(0,len(gd)-1):

        for i in range(1,len(gd[j])-1):
            if gd[j][i] == 0:   # <- if cell is empty

                if gd[j][i-1] == 0 and gd[j][i+1] == 0:     # 2 around empty
                    gd[j+1][i] = rule[7]

                elif gd[j][i-1] == 0 and gd[j][i+1] == 1:   # left empty, right full
                    gd[j+1][i] = rule[6]
                    
                elif gd[j][i-1] == 1 and gd[j][i+1] == 0:   # left full, right empty
                    gd[j+1][i] = rule[3]
                    
                elif gd[j][i-1] == 1 and gd[j][i+1] == 1:   # 2 around full
                    gd[j+1][i] = rule[2]

            else:                   # <- cell is full
                    
                if gd[j][i-1] == 0 and gd[j][i+1] == 0:     # 2 around empty
                    gd[j+1][i] = rule[5]

                elif gd[j][i-1] == 0 and gd[j][i+1] == 1:   # left empty, right full
                    gd[j+1][i] = rule[4]
                    
                elif gd[j][i-1] == 1 and gd[j][i+1] == 0:   # left full, right empty
                    gd[j+1][i] = rule[1]
                    
                elif gd[j][i-1] == 1 and gd[j][i+1] == 1:   # 2 around full
                    gd[j+1][i] = rule[0]
    return gd

grid = evolution(create_grid(400), rules)




            


