def SorryDatSnapIkNiet():
    print("Sorry dat begrijp ik niet, of we hebben die keuze niet.")

print("Welkom bij Papi Gelato.")
TotaalBolletjes = 0
Hoorntjes = 0 
Bakjes = 0

def ZakelijkParticulier():
    ZakelijkOfParticulier = input("Bent u 1) particulier of 2) zakelijk? ")
    if ZakelijkOfParticulier == "1":
        Stap1()
    elif ZakelijkOfParticulier == "2":
        AantalLZakelijk()
    else:
        SorryDatSnapIkNiet()
        ZakelijkParticulier()

def AantalLZakelijk():
    HoeveelLiters = input("Hoeveel liter zou u willen bestellen? ")

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
    global GeenTopping
    global Slagroom
    global Sprinkels
    global CaramelSause
    GeenTopping = 0
    Slagroom = 0
    Sprinkels = 0
    CaramelSause = 0
    Toppings = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ").upper()
    if Toppings == "A":
            GeenTopping += 1
    elif Toppings == "B":
            Slagroom += 1
    elif Toppings == "C":
            Sprinkels += 1
    elif Toppings == "D":
            CaramelSause += 1
    else:
        SorryDatSnapIkNiet()
        Stap4(BakjeOfHoorntje,HoeveelBolletjes)
    Stap5(BakjeOfHoorntje,HoeveelBolletjes)

def Stap5(BakjeOfHoorntje,HoeveelBolletjes):
    NogMeer = input("Hier is uw "+BakjeOfHoorntje+" met "+str(HoeveelBolletjes)+" bolletje(s). Wilt u nog meer bestellen? (Y/N) ")
    global TotaalBolletjes
    TotaalBolletjes += HoeveelBolletjes
    if NogMeer == "Y" or NogMeer == "y":
        Stap1()
    elif NogMeer == "N" or NogMeer == "n":
        print("Bedankt en tot ziens!")
        Stap6()
    else:
        SorryDatSnapIkNiet()
        Stap5(BakjeOfHoorntje,HoeveelBolletjes)

def Stap6():
    PrijsBol = 1.10
    PrijsHoorntje = 1.25
    PrijsBakje = 0.75
    PrijsSlagroom = 0.50
    PrijsSprinkels = 0.30
    if Bakjes > 0:
        PrijsCaramelSause = 0.90
    else:
        PrijsCaramelSause = 0.60
    PrijsToppings = 0
    TPrijsSlagroom = Slagroom * PrijsSlagroom
    TPrijsSprinkels = Sprinkels * PrijsSprinkels
    TPrijsCaramelSause = CaramelSause * PrijsCaramelSause
    if GeenTopping >= 1:
        PrijsToppings == 0
    else:
        PrijsToppings = TPrijsCaramelSause + TPrijsSlagroom + TPrijsSprinkels
    PrijsBolletjes = "{:.2f}".format(PrijsBol)
    PrijsHoorntjes = "{:.2f}".format(PrijsHoorntje)
    PrijsBakjes = "{:.2f}".format(PrijsBakje)
    TotaalPrijsBol = PrijsBol * TotaalBolletjes
    TotaalPrijsHoorntje = PrijsHoorntje * Hoorntjes
    TotaalPrijsBakje = PrijsBakje * Bakjes
    TotaalPrijs = TotaalPrijsBol + TotaalPrijsHoorntje + TotaalPrijsBakje + PrijsToppings
    TotaalPrijs2 = "{:.2f}".format(TotaalPrijs)
    TotaalPrijsBolletjes = "{:.2f}".format(TotaalPrijsBol)
    TotaalPrijsHoorntjes = "{:.2f}".format(TotaalPrijsHoorntje)
    TotaalPrijsBakjes = "{:.2f}".format(TotaalPrijsBakje)
    PrijsTopping = "{:.2f}".format(PrijsToppings)

    print('---------["Papi Gelato"]---------')
    print("                                 ")
    if TotaalBolletjes > 0:
        print("Bolletjes     ",str(TotaalBolletjes),"x €"+str(PrijsBolletjes),"  = €"+str(TotaalPrijsBolletjes))
    if Hoorntjes > 0:
        print("Hoorntjes     ",str(Hoorntjes),"x €"+str(PrijsHoorntjes),"  = €"+str(TotaalPrijsHoorntjes))
    if Bakjes > 0:
        print("Bakje         ",str(Bakjes),"x €"+str(PrijsBakjes),"  = €"+str(TotaalPrijsBakjes))
    if float(PrijsTopping) > 0:
        print("Toppings      ",1,"x €"+str(PrijsTopping),"  = €"+str(PrijsTopping))
    print("                           --------+")
    print("Totaal                     = €"+str(TotaalPrijs2))
    print("                                 ")
    print('---------["Papi Gelato"]---------')
     
Stap1()