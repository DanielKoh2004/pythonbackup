print("Tile Description                      Price Per Box")
print("Small black granite                   RM85.80")
print("Medium sunset yellow                  RM55.00")
print("Large oak wood effect                 RM286.00")
print("Extra-large white marble              RM290.00")
#declaring variables
smallblackgranite = sbg = 85.80
mediumsunsetyellow = msy = 55.00
largeoakwoodeffect = lowe = 286.00
extralargewhitemarble = elwm = 290.00

wallheight1 = 0
wallheight2 = 0
wallheight3 = 0
wallheight4 = 0
wallwidth1 = 0
wallwidth2 = 0
wallwidth3 = 0
wallwidth4 = 0


#input first wall data
wallheight1 = int(input("Enter the wall's height : "))
while (wallheight1 < 0): #error handler
    print("Invalid Input, Please Restart the Program")
    exit()
wallwidth1 = int(input("Enter the wall's width : "))
while (wallwidth1 < 0):#error handler
    print("Invalid Input, Please Restart the Program")
    exit()
walltile1 = input("Enter the tile that will be used : (Please use full name without space or short form eg. sbg for small black granite) ")
while walltile1 not in ['smallblackgranite','mediumsunsetyellow','largeoakwoodeffect','extralargewhitemarble','sbg','msy','lowe','elwm']:#error handler
    print("Invalid Input, Please Restart the Program")
    exit()
areaofwall1 = wallheight1 * wallwidth1
print("1 of 4 walls added")
addwall1 = input("Would you like to add another wall? (Yes/No) : ")

#input second wall data
if addwall1 in ['yes','Yes','y']:
    wallheight2 = int(input("Enter the wall's height : "))
    while (wallheight2 < 0):#error handler
        print("Invalid Input, Please Restart the Program")
        exit()
    wallwidth2 = int(input("Enter the wall's width : "))
    while (wallwidth2 < 0):#error handler
        print("Invalid Input, Please Restart the Program")
        exit()
    walltile2 = input("Enter the tile that will be used : (Please use full name without space or short form eg. sbg for small black granite) ")
    while walltile2 not in ['smallblackgranite','mediumsunsetyellow','largeoakwoodeffect','extralargewhitemarble','sbg','msy','lowe','elwm']:#error handler
        print("Invalid Input, Please Restart the Program")
        exit()
    areaofwall2 = wallheight2 * wallwidth2
    print("2 of 4 walls added")
    addwall2 = input("Would you like to add another wall? (Yes/No) : ")
    
    #input third wall data
    if addwall2 in ['yes','Yes','y']:
        wallheight3 = int(input("Enter the wall's height : "))
        while (wallheight3 < 0):#error handler
            print("Invalid Input, Please Restart the Program")
            exit()
        wallwidth3 = int(input("Enter the wall's width : "))
        while (wallwidth3 < 0):#error handler
            print("Invalid Input, Please Restart the Program")
            exit()
        walltile3 = input("Enter the tile that will be used : (Please use full name without space or short form eg. sbg for small black granite) ")
        while walltile3 not in ['smallblackgranite','mediumsunsetyellow','largeoakwoodeffect','extralargewhitemarble','sbg','msy','lowe','elwm']:#error handler
            print("Invalid Input, Please Restart the Program")
            exit()
        areaofwall3 = wallheight3 * wallwidth3
        print("3 of 4 walls added")
        addwall3 = input("Would you like to add another wall? (Yes/No) : ")
    
        #input fourth wall data
        if addwall3 in ['yes','Yes','y']:
            wallheight4 = int(input("Enter the wall's height : "))
            while (wallheight4 < 0):#error handler
                print("Invalid Input, Please Restart the Program")
                exit()
            wallwidth4 = int(input("Enter the wall's width : "))
            while (wallwidth4 < 0):#error handler
                print("Invalid Input, Please Restart the Program")
                exit()
            walltile4 = input("Enter the tile that will be used : (Please use full name without space or short form eg. sbg for small black granite)")
            while walltile4 not in ['smallblackgranite','mediumsunsetyellow','largeoakwoodeffect','extralargewhitemarble','sbg','msy','lowe','elwm']:#error handler
                print("Invalid Input, Please Restart the Program")
                exit()
            areaofwall4 = wallheight4 * wallwidth4
            print("4 of 4 walls added")
        elif addwall3 in ['no','No','n']:
            wallheight4 = 0
            wallwidth4 = 0
            exit
        else:
            print("Invalid Input, Please Restart the Program")#error handler
    elif addwall2 in ['no','No','n']:
        wallheight3 = 0
        wallwidth3 = 0
        wallheight4 = 0
        wallwidth4 = 0
        exit
    else:
        print("Invalid Input, Please Restart the Program")#error handler
elif addwall1 in ['no','No','n']:
    wallheight2 = 0
    wallwidth2 = 0
    wallheight3 = 0
    wallwidth3 = 0
    wallheight4 = 0
    wallwidth4 = 0
    exit
else:
    print("Invalid Input, Please Restart the Program")#error handler

#calculation part

#calculation for the first wall
    if walltile1 in ['smallblackgranite','sbg']:
        costoftile1 = smallblackgranite * areaofwall1
    elif walltile1 in ['mediumsunsetyellow','msy']:
        costoftile1 = mediumsunsetyellow * areaofwall1
    elif walltile1 in ['largeoakwoodeffect','lowe']:
        costoftile1 = largeoakwoodeffect * areaofwall1
    else:
        while(walltile1 in ['extralargewhitemarble','elwm']):
            costoftile1 = extralargewhitemarble * areaofwall1
#calculation for the second wall
    if walltile2 in ['smallblackgranite','sbg']:
        costoftile2 = smallblackgranite * areaofwall2
    elif walltile2 in ['mediumsunsetyellow','msy']:
        costoftile2 = mediumsunsetyellow * areaofwall2
    elif walltile2 in ['largeoakwoodeffect','lowe']:
        costoftile2 = largeoakwoodeffect * areaofwall2
    else:
        while(walltile2 in ['extralargewhitemarble','elwm']):
            costoftile2 = extralargewhitemarble * areaofwall2
#calculation for the third wall
    if walltile3 in ['smallblackgranite','sbg']:
        costoftile3 = smallblackgranite * areaofwall3
    elif walltile3 in ['mediumsunsetyellow','msy']:
        costoftile3 = mediumsunsetyellow * areaofwall3
    elif walltile3 in ['largeoakwoodeffect','lowe']:
        costoftile3 = largeoakwoodeffect * areaofwall3
    else:
        while(walltile3 in ['extralargewhitemarble','elwm']):
            costoftile3 = extralargewhitemarble * areaofwall3

#calculation for the fourth wall
    if walltile4 in ['smallblackgranite','sbg']:
        costoftile4 = smallblackgranite * areaofwall4
    elif walltile4 in ['mediumsunsetyellow','msy']:
        costoftile4 = mediumsunsetyellow * areaofwall4
    elif walltile4 in ['largeoakwoodeffect','lowe']:
        costoftile4 = largeoakwoodeffect * areaofwall4
    else:
        while(walltile4 in ['extralargewhitemarble','elwm']):
            costoftile4 = extralargewhitemarble * areaofwall4

total = costoftile1 + costoftile2 + costoftile3 + costoftile4

#printing the output

while(areaofwall4 > 0):
    print("The area for the fourth wall is",format(areaofwall4,".2f"),"m²")
    print("The amount of box of tile needed for the fourth is ",format(areaofwall4,".0f"),"piece")
    print("Cost of the tile need needed for the fourth wall is","RM",format(costoftile4,".2f"))
    print('')
while(areaofwall3 > 0):
    print("The area for the third wall is",format(areaofwall3,".2f"),"m²")
    print("The amount of box of tile needed for the third is ",format(areaofwall3,".0f"),"piece")
    print("Cost of the tile need needed for the third wall is","RM",format(costoftile3,".2f"))
    print('')
while(areaofwall2 > 0):
    print("The area for the second wall is",format(areaofwall2,".2f"),"m²")
    print("The amount of box of tile needed for the second wall is ",format(areaofwall2,".0f"),"piece")
    print("Cost of the tile need needed for the second wall is","RM",format(costoftile2,".2f"))
    print('')
while (areaofwall1 > 0):
    print("The area for the wall is",format(areaofwall1,".2f"),"m²")
    print("The amount of box of tile needed for the wall is ",format(areaofwall1,".0f"),"piece")
    print("Cost of the tile need needed for the wall is","RM",format(costoftile1,".2f"))
    print('')
print("The grand total for the price of the tiles needed is, RM",total)
print('')
startover = input("Do you want to enter another transaction?")
if startover in ['yes','Yes','y']
    start()
    
