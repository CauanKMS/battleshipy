#CauanKMS, 20171116
#Battleship game!

j1 = open("jogador1.txt", "r")
j2 = open("jogador2.txt", "r")
resultado = open("resultado.txt", "w")

table = []

for i in range(14):
    tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'F', 'J', 'L', 'M', 'N', 'O', 'P']
    for l in range(len(tab) - 1):
        table.append(str(tab[i] + str(l + 1)))

#print(table)

#Extract any item from any player file
def extractFromPlayerFile(player, letter):
    player.seek(0)
    for x in player.readlines():
        if x.startswith(letter):
            return x.strip(letter + ';')

#def validations():
#    return True

#ERROR_NR_PARTS_VALIDATION
def errornrpartsvalidation(plyr):
    pRounder = extractFromPlayerFile(plyr, 'T')
    p_R = pRounder.split('|')
    if len(p_R) < 20 or len(p_R) > 20:
        return False
    else:
        return True

#print(errornrpartsvalidation(j2))

if errornrpartsvalidation(j1) == False:
    resultado.write('J1 ERROR_NR_PARTS_VALIDATION')
    #print('FOI J1')
    j1.close()
    j2.close()
    resultado.close()
elif errornrpartsvalidation(j2) == False:
    resultado.write('J2 ERROR_NR_PARTS_VALIDATION')
    #print('FOI J2')
    j1.close()
    j2.close()
    resultado.close()

#ERROR_OVERWRITE_PIECES_VALIDATION
def erroroverwritepiecesvalidation(player, tabl):
    ships = []
    for x in range(4):
        ships.append(extractFromPlayerFile(player, str(x + 1)).strip('\n'))

    marked = []
    for y in range(len(ships)):
        shippart = ships[y].split('|')
        for z in shippart:
            #CODE 1 - 2 Pieces - 4 POSITIONs EACH
            if y == 0:
                realz = []
                if z.find('H') != -1:
                    for q in range(int(z[1]), int(z[1]) + 4):
                        realz.append(z[0] + str(q))

                    marked.append(realz)

                #elif z[3] == 'H':
                #    realz.append(z[0] + q for q in range(int(z[1] + z[2])))

                #elif z[2] == 'V':

                #elif z[3] == 'V':

            #CODE 2 - 2 Pieces - 5 POSITIONs EACH
            #elif y == 1:

            #CODE 3 - 5 Pieces - 1 POSITION EACH
            elif y == 2:
                marked.append(z)

            #CODE 4 - 4 Pieces - 2 POSITIONs EACH
            #elif y == 3:

    return marked

j1.close()
j2.close()
resultado.close()
