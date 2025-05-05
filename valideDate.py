from leapYear import isLeapYear

def validateDate(day, month, year):
    month31s = [ 1, 3, 5, 7, 8, 10, 12]
    month30s = [ 4, 6, 9, 11]

    
    if ( month in month31s and day < 32 and day > 0) or (month in month30s and day < 31 and day > 0) or (month == 2 and isLeapYear(year) and day < 30 and day > 0) or ( month == 2 and isLeapYear(year) == False and day < 29 and day > 0):
        return True
    else:
        return False

def main():
    day   = int(input("Gib ein Tag ein: "))
    month = int(input("Gib ein Monat ein: "))
    year  = int(input("Gib ein Jahr ein: "))
    print(validateDate(day, month, year))

if __name__ == "__main__":
    main()
