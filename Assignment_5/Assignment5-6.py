#Celsius to Fahrenheit Converter.

def TempConvert(Value):
    fahren = (Value * 9/5)+32
    return fahren

def main():
    temp = int(input("Enter temperature in celsius : "))

    ret = TempConvert(temp)

    print("Temperature in Fahrenheit:", ret, "°F")

if __name__ == "__main__":
    main()

'''
Enter temperature in celsius : 25
Temperature in Fahrenheit: 77.0 °F
'''