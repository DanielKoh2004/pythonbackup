def start():
    print("Tile Description                        Price Per Box")
    print("Small black granite (sbg)                     RM85.80")
    print("Medium sunset yellow (msy)                    RM55.00")
    print("Large oak wood effect (lowe)                 RM286.00")
    print("Extra-large white marble (elwm)              RM290.00")
    wallheight2=0
    wallheight3=0
    wallheight4=0
    wallwidth2=0
    wallwidth3=0
    wallwidth4=0
    sbg = 85.80
    msy = 55.00
    lowe = 286.00
    elwm = 290.00
    wallheight1 = float(input("Enter the wall's height : "))
    wallwidth1 = float(input("Enter the wall's width : "))
    walltile1 = eval(input("Enter the tile that will be used : (Please use short form eg. sbg for small black granite) "))
    print("1 of 4 walls added")
    addwall1 = input("Would you like to add another wall? (Yes/No) : ")
    if addwall1 in ['yes','Yes','y']:
        wallheight2 = float(input("Enter the wall's height : "))
        wallwidth2 = float(input("Enter the wall's width : "))
        walltile2 = eval(input("Enter the tile that will be used : (Please use short form eg. sbg for small black granite) "))
        print("2 of 4 walls added")
        addwall2 = input("Would you like to add another wall? (Yes/No) : ")
        if addwall2 in ['yes','Yes','y']:
            wallheight3 = float(input("Enter the wall's height : "))
            wallwidth3 = float(input("Enter the wall's width : "))
            walltile3 = eval(input("Enter the tile that will be used : (Please use short form eg. sbg for small black granite) "))
            print("3 of 4 walls added")
            addwall3 = input("Would you like to add another wall? (Yes/No) : ")
            if addwall3 in ['yes','Yes','y']:
                wallheight4 = float(input("Enter the wall's height : "))
                wallwidth4 = float(input("Enter the wall's width : "))
                walltile4 = eval(input("Enter the tile that will be used : (Please use short form eg. sbg for small black granite) "))
                print("4 of 4 walls added")
            elif addwall3 in ['no','No','n']:
                walltile4 = 0
                exit          
            else:
                print ("Invalid input")
                exit
        elif addwall2 in ['no','No','n']:  
            walltile3 = 0
            walltile4 = 0  
            exit
        else:
            print ("Invalid input")
            exit
    elif addwall1 in ['no','No','n']:
        walltile2 = 0
        walltile3 = 0
        walltile4 = 0
        exit
    else:
        print ("Invalid input")
        exit
    area1 = wallheight1 * wallwidth1    
    area2 = wallheight2 * wallwidth2
    area3 = wallheight3 * wallwidth3
    area4 = wallheight4 * wallwidth4
    numberofbox1 = area1
    numberofbox2 = area2
    numberofbox3 = area3
    numberofbox4 = area4
    pricewall1 = numberofbox1 * walltile1
    pricewall2 = numberofbox2 * walltile2
    pricewall3 = numberofbox3 * walltile3
    pricewall4 = numberofbox4 * walltile4
    totalprice = pricewall1 + pricewall2 + pricewall3 + pricewall4
    if area1 > 0:
        print()
        print("The area of the first wall is " , area1, "m²")
        print("The number of boxes needed for first wall is", numberofbox1)
        print("The total price of first wall is RM" "%.2f"%pricewall1)
        print()
    else:
        print("Invalid output")
        exit
    if area2 > 0:
        print("The area of the second wall is " , area2, "m²")
        print("The number of boxes needed for second wall is", numberofbox2)
        print("The total price of second wall is RM" "%.2f"%pricewall2)
        print()
    else:
        exit
    if area3 > 0:
        print("The area of the third wall is " , area3, "m²")
        print("The number of boxes needed for third wall is", numberofbox3)
        print("The total price of third wall is RM" "%.2f"%pricewall3)
        print()
    else:
        exit
    if area4 > 0:
        print("The area of the forth wall is " , area4, "m²")
        print("The number of boxes needed for forth wall is", numberofbox4)
        print("The total price of forth wall is RM" "%.2f"%pricewall4)
        print ()
    else:
        exit
    if totalprice >0:
        print ("The total price is: ""%.2f"% totalprice)
        print()
    else:
        print ("Invalid input")
        exit()
    startover = input("Do you want to perform another calculation? (yes/no) ")
    if (startover in ['yes','Yes','y']):
        start()
    elif startover in ['no','No','N']:
        print("Thanks for using this program!")
        exit()
start()