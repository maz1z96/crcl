# Cockcroft-Gault CrCl, mL/min = (140 – age) × (weight, kg) × (1.23 for male or 1.04 for female) / (Cr, micromol/L)
def main():
    age = get_positive_number("Age", int)
    weight = get_positive_number("Weight (kg)", float)
    cr = get_positive_number("Serum Creatinine (micromol/L)", float)
    sex = input("Sex (M/F) ").title()

    if sex == "M":
        constant = 1.23
    elif sex == "F":
        constant = 1.04

    crcl = (140 - age) * weight * constant / cr
    crcl = round(crcl, 2)

    print()
    print(f'CrCl = {crcl} ml/min')

def get_positive_number(prompt, type, min=0):
    while True:
        try:
            number = type(input(f'{prompt}: '))
        except ValueError:
            print("Please enter a valid number")
            print()
        else:
            if number < min:
                print("Number cannot be negative. Please try again")
                print()
            else:
                break
    return number

main()
