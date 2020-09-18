#Loop – mata in 5 värden. ”stefan 0709-555555” , splitta
#på mellanslag och lägg i dictionary (namn/telefonnummer
#– OBS: Namn ska vara KEY.
#OBS2: Check if key exists?? Fråga kanske google?)
#Nu ny loop: inmatning av namn om och om igen
#Stefan → Stefan har tel 0709-555 555
#Inmatning av namn som saknas → ”Finns ej i registret

#NÄR ? NÄR INTE?
# Alla typer av algoritmer där man vill jobba med unika värden för ”nyckel” = logiskt
# Inga dubletter
# snabb åtkomst (random access). Konsistent prestanda
# å andra sidan: i datastrukturer och algoritmer får ni se att arrayer (listor) trots allt 
# i praktiken är det enda som behövs ... data locality

telregister = {}
for n in range(0,5):    #stefan 08-11122334
    inp = input("Mata in namn och telefonnummer - spaceseparated")
    parts = inp.split(' ')
    namn = parts[0]
    tel = parts[1]
    telregister[namn] = tel;

while(True):
    namn = input("Mata in namn du vill söka på:")
    if namn in telregister:
        print(f"{namn} har tel {telregister[namn]}")
    else:
        print("Finns ej i registret")


#def HittaLangstaOrdet(arrayOfStrings):
#    longestSoFar = arrayOfStrings[0]
#    for one in arrayOfStrings:
#        if len(one) > len(longestSoFar):
#            longestSoFar = one
#    return longestSoFar

#listan = ["Djurgården", "AIK", "Hammarby", "Brommapojkarna"]
#longestName = HittaLangstaOrdet(listan)
#print(longestName)


#namn -> antal matchjer som som spelat

#för varje tröjnummer ska vi hålla reda på spelarnamnet
#          kontonummer                      saldot     


#DICTIONARY = lista - där facken inte har nummer 0..1..2
#           fack ha ett NAMN/VÄRDE som VI GER DEN
# åtkomst
spelare = {}
while True:
    print("1. Lista spelare")
    print("2. Ny spelare")
    print("3. Finns spelare med nummer?")
    selection = input("Ange val>:")
    if selection == "2":
        number = int(input("Vilket nummer?"))
        namn = input("Namn")
        spelare[number] = namn
    if selection == "3":
        number = int(input("Vilket nummer?"))
        if number in spelare:
            print(spelare[number])
        else:
            print("Hittades inte")
    if selection == "1":
        for key in spelare.keys():
            namn = spelare[key]
            print(f"{key} {namn}")
