import re
popsuta_baza_danych = [{'id': 4033889765, 'pesel': '31040696959', 'plec': 'M', 'data_urodzenia': ()}, {'id': 9220725992, 'pesel': '47031540769', 'plec': 'K', 'data_urodzenia': ()}, {'id': 2958319879, 'pesel': '86110816348', 'plec': 'K', 'data_urodzenia': ()}, {'id': 3338284595, 'pesel': '#######6180', 'plec': 'K', 'data_urodzenia': (1923, 5, 10)}, {'id': 4260200607, 'pesel': '#######3858', 'plec': 'M', 'data_urodzenia': (1933, 3, 12)}, {'id': 7792567513, 'pesel': '#######0624', 'plec': 'K', 'data_urodzenia': (1958, 7, 3)}, {'id': 4343489024, 'pesel': '77051453866', 'plec': 'M', 'data_urodzenia': (1977, 5, 14)}, {'id': 4577782052, 'pesel': '55030729762', 'plec': 'K', 'data_urodzenia': ()}, {'id': 7271210500, 'pesel': '#######2290', 'plec': 'M', 'data_urodzenia': (1929, 3, 13)}]

def validPesel(pesel):
    x = re.search("[0-9]{9}",pesel)
    control_sum = [9, 7, 3, 1]
    temp = list(control_sum)
    sum = 0 
    count = 0
    if x:
        for i in pesel: 
            count += 1 
            if len(pesel) -1 < count  :
                score = sum % (len(pesel)-1)
                if score == int(pesel[len(pesel)-1]):
                    return True
            else:
                if len(temp)< 1:
                    temp = list(control_sum)
                sum += int(i)* temp[0]
                del temp[0]
    return False

def getDate(pesel):
    first = "19" if pesel[0] > "0" else "20" 
    date = first + pesel[0] + pesel[1]
    month = pesel[2] + pesel[3]
    day = pesel[4] + pesel[5]
    return (int(date), int(month), int(day))

def validDate(date):
    return True if len(date) > 0 else False

def getSex(pesel):
    return 'K' if int(pesel[len(pesel)-1]) % 2 else 'M' 

def validSex(plec,pesel):
    return True if getSex(pesel) == plec else False

def getPesel(pesel, data_urodzenia):
    year = str(data_urodzenia[0]) 
    month = str(data_urodzenia[1])
    day = str(data_urodzenia[2])
    year = year[len(year)-2] + year[len(year)-1] 
    month = month if len(month) > 1 else "0"+ str(month)
    day = day if len(day) > 1 else "0"+ day
    date = "%s%s%s" % (year, month, day)
    return pesel.replace("#######",date)

count = 0
for record in popsuta_baza_danych:
    print(str(count)+str(record))
    count += 1

count = 0
for record in popsuta_baza_danych:
    pesel = record["pesel"]
    data_urodzenia = record["data_urodzenia"]
    plec = record["plec"]
    if not validPesel(pesel):
        record["pesel"] = getPesel(pesel,data_urodzenia)
    if not validSex(plec,pesel):
        record["plec"] = getSex(pesel)
    if not validDate(data_urodzenia):
        record["data_urodzenia"] = getDate(pesel)
    print(str(count)+str(record))
    count += 1


