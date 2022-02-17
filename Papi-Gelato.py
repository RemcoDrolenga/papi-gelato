def SorryDatSnapIkNiet():
    print("Sorry dat begrijp ik niet, of we hebben die keuze niet.")

print("Welkom bij Papi Gelato.")

def Stap1():
    HoeveelBolletjes = int(input("Hoeveel bolletjes wilt u? "))
    if HoeveelBolletjes >= 1 and HoeveelBolletjes <=3:
        Stap2(HoeveelBolletjes)
    elif HoeveelBolletjes >= 4 and HoeveelBolletjes <= 8:
        print("Dan krijgt u van mij een bakje met",HoeveelBolletjes,"bolletjes.")
        Stap2(HoeveelBolletjes)
    elif HoeveelBolletjes >= 8:
        print("Sorry, zulke grote bakken hebben we niet.")
        Stap1()
    else:
        SorryDatSnapIkNiet()
        Stap1()

def Stap2(HoeveelBolletjes):
    Aardbei = 0
    Chocolade = 0
    Munt = 0
    Vanille = 0
    for i in range(1,HoeveelBolletjes+1):
        Smaken = input("Welke smaak wilt u voor bolletje nummer "+str(i)+" ? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ").upper()
        if Smaken == "A":
            Aardbei += 1
        elif Smaken == "C":
            Chocolade += 1
        elif Smaken == "M":
            Munt += 1
        elif Smaken == "V":
            Vanille += 1
        else:
            SorryDatSnapIkNiet()
            Stap2(HoeveelBolletjes)
    Stap3(HoeveelBolletjes)

def Stap3(HoeveelBolletjes):
    if HoeveelBolletjes <= 3:
        BakjeOfHoorntje = input("Wilt u deze "+str(HoeveelBolletjes)+" bolletje(s) in A) een hoorntje of B) een bakje? ").upper()
        if BakjeOfHoorntje == "A" or BakjeOfHoorntje == "B":
            if BakjeOfHoorntje == "A":
               BakjeOfHoorntje = "hoorntje"
            else:
                BakjeOfHoorntje = "bakje"
            Stap4(BakjeOfHoorntje,HoeveelBolletjes)
        else:
            SorryDatSnapIkNiet()
            Stap3()
    else:
        BakjeOfHoorntje = "bakje"
        Stap4(BakjeOfHoorntje,HoeveelBolletjes)

def Stap4(BakjeOfHoorntje,HoeveelBolletjes):
    NogMeer = input("Hier is uw "+BakjeOfHoorntje+" met "+str(HoeveelBolletjes)+" bolletje(s). Wilt u nog meer bestellen? (Y/N) ")
    if NogMeer == "Y" or NogMeer == "y":
        Stap1()
    elif NogMeer == "N" or NogMeer == "n":
        print("Bedankt en tot ziens!")
    else:
        SorryDatSnapIkNiet()
        Stap4()

Stap1()
