def citeste_tranzitii(fisier):
    tranzitii = {}
    stari_finale = []
    with open(fisier, 'r') as file:
        lines = file.readlines()
        ok = 0
        for line in lines:
            linie = line.strip().split()
            if ok <=len(lines)-2 :
                stare1, cifra, stare2 = linie[0], linie[1], linie[2]
                if stare1 not in tranzitii:
                    tranzitii[stare1] = {}
                if cifra not in tranzitii[stare1]:
                    tranzitii[stare1][cifra] = set()
                tranzitii[stare1][cifra].add(stare2)
                ok+=1
            else:
                if ok == len(lines)-1:
                    for l in line.strip().split():
                        stari_finale.append(l)
    return tranzitii, stari_finale

def DFA(input, tranzitii, stare_initiala, stari_finale):
    stari_curente = {stare_initiala}
    drum = [stare_initiala]
    for cifra in input:
        stari_noi = set()
        for stare in stari_curente:
            if stare in tranzitii and cifra in tranzitii[stare]:
                stari_noi.update(tranzitii[stare][cifra])
            if None in tranzitii and cifra in tranzitii[None]:
                stari_noi.update(tranzitii[None][cifra])
        stari_curente = stari_noi
        drum.extend(stari_curente)
    return any(stare in stari_finale for stare in stari_curente), drum

tranzitii, stari_finale = citeste_tranzitii('transitions.txt')
stare_initiala = 'q0'
input = input("Enter a string over the alphabet {0,1}: ")
DFA, drum = DFA(input, tranzitii, stare_initiala, stari_finale)
if DFA:
    print("Acceptat.")
    print("Drum: ", drum)
else:
    print("Neacceptat.")



