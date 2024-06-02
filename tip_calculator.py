def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    convert_to_float = float(d.replace("$", ""))
    rounded_float = round(convert_to_float, 1)
    return rounded_float


def percent_to_float(p):
    convert_to_float = float(p.replace("%",""))
    percent_to_multi = convert_to_float * 0.01
    return percent_to_multi


main()
