#CauanKMS, 20171116
#Battleship game!

j1 = open("jogador1.txt", "r")
j2 = open("jogador2.txt", "r")
resultado = open("resultado.txt", "w")

table = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15','B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15','C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15','D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15','E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15','F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15','G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15','H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15','I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15','J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15','L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L13', 'L14', 'L15','M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15','N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15','O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10', 'O11', 'O12', 'O13', 'O14', 'O15','P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15']

#EXTRACT ANY ITEM FROM THE PLAYERS FILES
def extractFromPlayerFile(player, letter):
    player.seek(0)
    for x in player.readlines():
        if x.startswith(letter):
            return x.strip(letter + ';')

#ERROR_NR_PARTS_VALIDATION - TORPEDOS
def errornrpartsvalidation(plyr):
    pRounder = extractFromPlayerFile(plyr, 'T')
    p_R = pRounder.split('|')
    if len(p_R) < 20 or len(p_R) > 20:
        return False
    else:
        return True

#WIDE ROUNDS WILL WIDE THE PLAYER SHIP POSITIONS SO WE CAN CHECK IF THERE ARE OVERWRITTEN POSITIONS
def widerounds(player, tabl):
    ships = []
    for x in range(4):
        ships.append(extractFromPlayerFile(player, str(x + 1)).strip('\n'))

    marked = []
    for y in range(len(ships)):
        shippart = ships[y].split('|')
        for z in shippart:
            #CODE 1 - 2 Pieces - 4 POSITIONs EACH
            if y == 0:
                if z.find('H') != -1:
                    try:
                        for q in range(int(z[1]) + int(z[2]), int(z[1]) + int(z[2]) + 4):
                            marked.append(z[0] + str(q))

                    except:
                        for q in range(int(z[1]), int(z[1]) + 4):
                            marked.append(z[0] + str(q))

                elif z.find('V') != -1:
                    try:
                        ipos = tabl.index(z[0] + z[1] + z[2])
                        for q in range(4):
                            marked.append(tabl[ipos])
                            ipos += 15
                    except:
                        ipos = tabl.index(z[0] + z[1])
                        for q in range(4):
                            marked.append(tabl[ipos])
                            ipos += 15

            #CODE 2 - 2 Pieces - 5 POSITIONs EACH
            elif y == 1:
                if z.find('H') != -1:
                    try:
                        for q in range(int(z[1]) + int(z[2]), int(z[1]) + int(z[2]) + 5):
                            marked.append(z[0] + str(q))

                    except:
                        for q in range(int(z[1]), int(z[1]) + 5):
                            marked.append(z[0] + str(q))

                elif z.find('V') != -1:
                    try:
                        ipos = tabl.index(z[0] + z[1] + z[2])
                        for q in range(5):
                            marked.append(tabl[ipos])
                            ipos += 15
                    except:
                        ipos = tabl.index(z[0] + z[1])
                        for q in range(5):
                            marked.append(tabl[ipos])
                            ipos += 15

            #CODE 3 - 5 Pieces - 1 POSITION EACH
            elif y == 2:
                marked.append(z)

            #CODE 4 - 4 Pieces - 2 POSITIONs EACH
            elif y == 3:
                if z.find('H') != -1:
                    try:
                        for q in range(int(z[1] + z[2]), int(z[1] + z[2]) + 2):
                            marked.append(z[0] + str(q))

                    except:
                        for q in range(int(z[1]), int(z[1]) + 2):
                            marked.append(z[0] + str(q))

                elif z.find('V') != -1:
                   try:
                        ipos = tabl.index(z[0] + z[1] + z[2])
                        for q in range(2):
                            marked.append(tabl[ipos])
                            ipos += 15
                   except:
                       ipos = tabl.index(z[0] + z[1])
                       for q in range(2):
                           marked.append(tabl[ipos])
                           ipos += 15

    return marked

#ERROR_OVERWRITE_PIECES_VALIDATION - RETURNS TRUE IF NOT OVERWRITTEN
def errorovewritepiecesvalidation(rounds):
    duplicated = set()
    return not any(q in duplicated or duplicated.add(q) for q in rounds)

def errornrpartsvalidation_rounds(rounds):
    return not len(rounds) != 31

#ERROR_POSITION_NONEXISTENT_VALIDATION
def errorpositionnonexexistentvalidation(rounds, tab):
    if set(rounds).issubset(tab) == False:
        return False
    else:
        return True

pTorp1 = extractFromPlayerFile(j1, 'T')
pTorpR1 = pTorp1.split('|')

pTorp2 = extractFromPlayerFile(j2, 'T')
pTorpR2 = pTorp2.split('|')

#HERE'S THE VALIDATION
if errorovewritepiecesvalidation(widerounds(j1, table)) == False:
    resultado.write('J1 ERROR_OVERWRITE_PIECES_VALIDATION')

elif errorovewritepiecesvalidation(widerounds(j2, table)) == False:
    resultado.write('J2 ERROR_OVERWRITE_PIECES_VALIDATION')

elif errornrpartsvalidation_rounds(widerounds(j1, table)) == False:
    resultado.write('J1 ERROR_NR_PARTS_VALIDATION')

elif errornrpartsvalidation_rounds(widerounds(j2, table)) == False:
    resultado.write('J2 ERROR_NR_PARTS_VALIDATION')

elif errornrpartsvalidation(j1) == False:
    resultado.write('J1 ERROR_NR_PARTS_VALIDATION')

elif errornrpartsvalidation(j2) == False:
    resultado.write('J2 ERROR_NR_PARTS_VALIDATION')

elif errorpositionnonexexistentvalidation(widerounds(j1,table),table) == False:
   resultado.write('J1 ERROR_POSITION_NONEXISTENT_VALIDATION')

elif errorpositionnonexexistentvalidation(widerounds(j2, table), table) == False:
   resultado.write('J2 ERROR_POSITION_NONEXISTENT_VALIDATION')

elif errorpositionnonexexistentvalidation(pTorpR1, table) == False:
   resultado.write('J1 ERROR_POSITION_NONEXISTENT_VALIDATION')

elif errorpositionnonexexistentvalidation(pTorpR2, table) == False:
   resultado.write('J2 ERROR_POSITION_NONEXISTENT_VALIDATION')

j1.close()
j2.close()
resultado.close()
