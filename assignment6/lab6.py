def main():
    value = int(input("Enter a positive integer < 100000: "))
    print(intName(value))

def intName(number):
    part = number 
    name = ""

    if part >= 100000:
        name = digitName(part//100000) + " hundred  "
        part = part % 100000

    if part >= 1000:
        if part // 1000 >= 10:
            name += teenName(part // 1000) + " thousand "
        else:
            name += digitName(part // 1000) + " thousand "
        part = part % 1000
    
    if part >= 100:
        name = name + " " + digitName(part//100) + " hundred "
        part = part % 100

    if part >= 20:
        name = name + " " + tensName(part)
        part = part % 10

    if part >= 10:
        name = name + " " + teenName(part)
        part = 0
    
    if part > 0:
        name += digitName(part) + " "

    return name

def digitName(digit):
    if digit == 1: return "one"
    if digit == 2: return "two"
    if digit == 3: return "three"
    if digit == 4: return "four"
    if digit == 5: return "five"
    if digit == 6: return "six"
    if digit == 7: return "seven"
    if digit == 8: return "eight"
    if digit == 9: return "nine"
    return ""

def tensName(tens):
    if tens >= 20 and tens < 30: return "twenty "
    if tens >= 30 and tens < 40: return "thirty "
    if tens >= 40 and tens < 50: return "forty "
    if tens >= 50 and tens < 60: return "fifty "
    if tens >= 60 and tens < 70: return "sixty "
    if tens >= 70 and tens < 80: return "seventy "
    if tens >= 80 and tens < 90: return "eighty "
    if tens >= 90 and tens < 100: return "ninety "
    return ""

def teenName(teen):
    if teen == 10: return "ten"
    if teen == 11: return "eleven"
    if teen == 12: return "twelve"
    if teen == 13: return "thirteen"
    if teen == 14: return "fourteen"
    if teen == 15: return "fifteen"
    if teen == 16: return "sixteen"
    if teen == 17: return "seventeen"
    if teen == 18: return "eighteen"
    if teen == 19: return "nineteen"
    return ""

if __name__ == "__main__":
    main()