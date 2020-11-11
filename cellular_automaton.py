grille = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
for _ in range(20):
    grille.append([])
for i in range(1,len(grille)):
    for j in range(35):
        grille[i].append(0)


#liste conditions: 000     001     100     101     010     011     110     111
conditions = [0,1,1,1,1,1,1,0]


def evolution(gd,cond):
    print(max)
    for j in range(0,len(gd)-1):

        for i in range(1,len(gd[j])-1):
            print(i)
            if gd[j][i] == 0:   # <- si la case est vide

                if gd[j][i-1] == 0 and gd[j][i+1] == 0:     # condition 0
                    gd[j+1][i] = cond[0]

                elif gd[j][i-1] == 0 and gd[j][i+1] == 1:   # condition 1
                    gd[j+1][i] = cond[1]
                    
                elif gd[j][i-1] == 1 and gd[j][i+1] == 0:   # condition 2
                    gd[j+1][i] = cond[2]
                    
                elif gd[j][i-1] == 1 and gd[j][i+1] == 1:   # condition 3
                    gd[j+1][i] = cond[3]

            else:                   # <- la case est pleine
                    
                if gd[j][i-1] == 0 and gd[j][i+1] == 0:     # condition 4
                    gd[j+1][i] = cond[4]

                elif gd[j][i-1] == 0 and gd[j][i+1] == 1:   # condition 5
                    gd[j+1][i] = cond[5]
                    
                elif gd[j][i-1] == 1 and gd[j][i+1] == 0:   # condition 6
                    gd[j+1][i] = cond[6]
                    
                elif gd[j][i-1] == 1 and gd[j][i+1] == 1:   # condition 7
                    gd[j+1][i] = cond[7]

evolution(grille, conditions)
for i in range(len(grille)):
    print(grille[i], end= "\n") 






