# pentru o gramatica regulata, genereaza toate cuvintele de o lungime n
f = open("tranzitii.txt", "r")
n = int(f.readline())
grm = {}  # retine gramatica

for line in f:
    line = line.strip().split()
    if line[0] not in grm:
        grm[line[0]] = line[1:]

# S = start
words = []  
start = 0
for i in range(n):
    # daca deja am inceput prelucrarea, se creeaza o lista temporara in care stocam noile cuvinte formate. Daca urmatoarea stare este una care poate fi prelucrabila, se preiau din dictionar starile
    # pentru fiecare stare preluata, formez noul cuvant, pe care il adaug in lista temporara. La final actualizez lista cu noile cuvinte
    if start != 0:
        cuv = []  
        for cuvant in words:
            if cuvant[-1] != "Lambda" and (cuvant[-1] >= "A" and cuvant[-1] <= "Z"):
                lista = grm[cuvant[-1]]
            else:
                continue
            for stare in lista:  
                cuvant2 = cuvant[:-1] + stare  
                cuv.append(cuvant2)  
        words = cuv
    # daca nu am inceput prelucrarea si daca nu a fost accesat Start, adaug elementele din lista (care contin cuvintele pentru Start)
    if start == 0: 
        lista = grm["S"]
        for stare in lista:
            words.append(stare)
        start = 1
final = []  # lista finala, dupa validare

for word in words:
    if word[-1] == "Lambda":  # daca a ajuns intr-o stare finala - lambda
        if len(word) - 1 == n:  # daca are lungimea necesara
            final.append(word)
    if word[-1] >= "a" and word[-1] <= "z":  # daca a ajuns intr-o stare finala          #pana la Z ca sa fie pe caz general (in exemplu, starile merg pana la E, dar pot fi si altele)
        final.append(word)
    elif word[-1] >= "A" and word[-1] <= "Z": # daca a ajuns intr-o stare potential finalas
        list = grm[word[-1]]
        if "Lambda" in list:  # daca lambda este printre stari, cuvantul este valid
            final.append(word[:-1])

print(final)
