userConversionType = input("1: for Inches to mm 2: for mm to inches")

conversionTypeInt = int(userConversionType)

userNumber = input("What is your number?")
userNumberFloat = float(userNumber)

if conversionTypeInt == 1:
    print("convert Inches to mm")
    convertedNumber = float(userNumber) * 25.4
    convertedString = "{0:.4f} inches is = {1:.4f} mm"


if conversionTypeInt == 2:
    print("convert mm to inches")
    convertedNumber = float(userNumber) / 25.4
    convertedString = "{0:.4f} mm is = {1:.4f} inches"


print (convertedString.format(userNumberFloat, convertedNumber))


