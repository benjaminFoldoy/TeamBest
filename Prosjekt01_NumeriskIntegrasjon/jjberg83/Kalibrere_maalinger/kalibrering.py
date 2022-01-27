with open('maalinger.txt', 'r', encoding='utf-8') as filen:
    tidspunkt = []
    maalinger = []
    kalibrerte_maalinger = []
    alleLinjer = filen.readlines()
    for indeks, linje in enumerate(alleLinjer):
        if indeks < 4:
            continue
        splitta = linje.split(',')
        tidspunkt.append(float(splitta[0]))
        maalinger.append(float(splitta[1]))
    for entry in maalinger:
        if entry >= 78.0:
            entry = 50.0
            kalibrerte_maalinger.append(entry)
        elif entry >= 65:
            entry = 40.0
            kalibrerte_maalinger.append(entry)
        elif entry >= 53.5:
            entry = 30.0
            kalibrerte_maalinger.append(entry)
        elif entry >= 43.5:
            entry = 20.0
            kalibrerte_maalinger.append(entry)
        elif entry >= 35.0:
            entry = 10.0
            kalibrerte_maalinger.append(entry)
        elif entry >= 26.0:
            entry = 0.0
            kalibrerte_maalinger.append(entry)
        elif entry >= 21.0:
            entry = -10.0
            kalibrerte_maalinger.append(entry)
        elif entry >= 19.0:
            entry = -20.0
            kalibrerte_maalinger.append(entry)
        elif entry >= 17.5:
            entry = -30.0
            kalibrerte_maalinger.append(entry)
        elif entry >= 16.5:
            entry = -40.0
            kalibrerte_maalinger.append(entry)
        else:
            entry = -50.0
            kalibrerte_maalinger.append(entry)
    
    with open('kalibrerte_maalinger.txt', 'w', encoding='utf-8') as ny_fil:
        for i in range(len(tidspunkt)):
            ny_fil.write(f'{tidspunkt[i]},{kalibrerte_maalinger[i]} \n')





'''
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


with open('trykk_og_temperaturlogg.csv', 'r', encoding='UTF8') as les:
    #Her lager og fyller jeg på listene med innholdet fra de forskjellige kolonnene
    tidspunkt_liste = []
    tid_siden_start_liste = []
    absolutt_trykk_liste = []
    temperatur_liste = []
    #unntaks_liste = []
    forste_verdi = -10 #siden første tid i csv fil er 0, vil vi sette denne verdien til -10. Deretter legger vi til nåværende tid til denne variabelen (se linje 37), og neste gang ser vi om neste tid er 10 sek mer enn dette igjen
      
    for linje in les:
        splitta = linje.split(';')
        if splitta[0] == 'Dato og tid': #Alt i øverste rad er strings. Derfor vil ikke int og float i else blokken under funke her, og det ville krasja hvis jeg ikke hoppet over her
            continue
        else:#jeg erstatter diverse tegn og gjør om fra strings til int/floats på direkten, før jeg sender inn
            tidspunkt_liste.append(splitta[0])
            tid_siden_start_liste.append(int(splitta[1]))
            absolutt_trykk_liste.append(float(splitta[3].replace(',','.')))
            temperatur_liste.append(float(splitta[4].replace(',','.').replace('\n','')))
            if int(splitta[1]) != forste_verdi + 10:
                #unntaks_liste.append([splitta[0], int(splitta[1])])
                print(f'Unntak funnet tidspunktet {splitta[0]} og tiden {splitta[1]}.')
            forste_verdi = int(splitta[1])
'''
