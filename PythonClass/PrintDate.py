while True:
    day=input("What date you purchased the toy? ")
    month=input("What month did you purchase the toy? ")
    month=month.lower()
    if month=="january":
        month='01'
    elif month=="february":
        month='02'
    elif month=="march":
        month='03'
    elif month=="april":
        month='04'
    elif month=="may":
        month='05'
    elif month=="june":
        month='06'
    elif month=="july":
        month='07'
    elif month=="august":
        month='08'
    elif month=="september":
        month='09'
    elif month=="october":
        month='10'
    elif month=="november":
        month='11'
    elif month=="december":
        month='12'
    else:
        print("That's not a valid month!")
        break
    year=input("What year did you purchase the toy? ")
    dop=year+'/'+month+'/'+day
    print(dop)
