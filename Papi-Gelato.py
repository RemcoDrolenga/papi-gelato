def SorryDatSnapIkNiet():
    print("Sorry dat begrijp ik niet, of we hebben die keuze niet.")

print("Welkom bij Papi Gelato.")
TotaalBolletjes = 0
Hoorntjes = 0 
Bakjes = 0

def Stap1():
    HoeveelBolletjes = int(input("Hoeveel bolletjes wilt u? "))
    if HoeveelBolletjes >= 1 and HoeveelBolletjes <=3:
        Stap2(HoeveelBolletjes)
    elif HoeveelBolletjes >= 4 and HoeveelBolletjes <= 8:
        print("Dan krijgt u van mij een bakje met",HoeveelBolletjes,"bolletjes.")
        global Bakjes
        Bakjes += 1
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
               global Hoorntjes
               Hoorntjes += 1
            else:
                BakjeOfHoorntje = "bakje"
                global Bakjes
                Bakjes += 1
            Stap4(BakjeOfHoorntje,HoeveelBolletjes)
        else:
            SorryDatSnapIkNiet()
            Stap3(HoeveelBolletjes)
    else:
        BakjeOfHoorntje = "bakje"
        Stap4(BakjeOfHoorntje,HoeveelBolletjes)

def Stap4(BakjeOfHoorntje,HoeveelBolletjes):
    NogMeer = input("Hier is uw "+BakjeOfHoorntje+" met "+str(HoeveelBolletjes)+" bolletje(s). Wilt u nog meer bestellen? (Y/N) ")
    global TotaalBolletjes
    TotaalBolletjes += HoeveelBolletjes
    if NogMeer == "Y" or NogMeer == "y":
        Stap1()
    elif NogMeer == "N" or NogMeer == "n":
        print("Bedankt en tot ziens!")
        Stap5()
    else:
        SorryDatSnapIkNiet()
        Stap4(BakjeOfHoorntje,HoeveelBolletjes)
        
def Stap5():
    PrijsBol = 1.10
    PrijsHoorntje = 1.25
    PrijsBakje = 0.75
    PrijsBolletjes = "{:.2f}".format(PrijsBol)
    PrijsHoorntjes = "{:.2f}".format(PrijsHoorntje)
    PrijsBakjes = "{:.2f}".format(PrijsBakje)
    TotaalPrijsBol = PrijsBol * TotaalBolletjes
    TotaalPrijsHoorntje = PrijsHoorntje * Hoorntjes
    TotaalPrijsBakje = PrijsBakje * Bakjes
    TotaalPrijs = TotaalPrijsBol + TotaalPrijsHoorntje + TotaalPrijsBakje
    TotaalPrijs2 = "{:.2f}".format(TotaalPrijs)
    TotaalPrijsBolletjes = "{:.2f}".format(TotaalPrijsBol)
    TotaalPrijsHoorntjes = "{:.2f}".format(TotaalPrijsHoorntje)
    TotaalPrijsBakjes = "{:.2f}".format(TotaalPrijsBakje)
    print('---------["Papi Gelato"]---------')
    print("                                 ")
    if TotaalBolletjes > 0:
        print("Bolletjes     ",str(TotaalBolletjes),"x €"+str(PrijsBolletjes),"  = €"+str(TotaalPrijsBolletjes))
    if Hoorntjes > 0:
        print("Hoorntjes     ",str(Hoorntjes),"x €"+str(PrijsHoorntjes),"  = €"+str(TotaalPrijsHoorntjes))
    if Bakjes > 0:
        print("Bakje         ",str(Bakjes),"x €"+str(PrijsBakjes),"  = €"+str(TotaalPrijsBakjes))
    print("                           --------+")
    print("Totaal                     = €"+str(TotaalPrijs2))
    print("                                 ")
    print('---------["Papi Gelato"]---------')

Stap1()
