grille = [
    []
]

def creer_grille(n):
    initialisation = int(n/2)
    for i in range(n):
        if i == initialisation:
            grille[0].append(1)
        else:
            grille[0].append(0)
    for _ in range(n):
        grille.append([])

    for i in range(1,len(grille)):
        for _ in range(n):
            grille[i].append(0)
    return grille


#liste conditions: 000     001     100     101     010     011     110     111
conditions = [0,1,1,1,1,1,1,0]


def evolution(gd,cond):
    for j in range(0,len(gd)-1):

        for i in range(1,len(gd[j])-1):
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
    return grille

grille = evolution(creer_grille(500), conditions)




            


