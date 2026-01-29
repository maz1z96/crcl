# Cockcroft-Gault CrCl, mL/min = (140 – age) × (weight, kg) × (1.23 for male or 1.04 for female) / (Cr, micromol/L)
def main():
    age = get_parameter("Age", int)
    weight = get_parameter("Weight (kg)", float)
    cr = get_parameter("Serum Creatinine (micromol/L)", float)
    constant = get_constant()

    crcl = (140 - age) * weight * constant / cr
    crcl = round(crcl, 2)
    reading = renal_function(crcl)

    print()
    print(f'CrCl = {crcl} ml/min')
    print(f'Renal function = {reading}')

def get_parameter(prompt, type, min=0):
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

def get_constant():
    while True:
        sex = input("Sex (M/F) ").title()

        if sex == "M":
            constant = 1.23
            return constant
        elif sex == "F":
            constant = 1.04
            return constant
        else:
            print("Please enter either M or F")
            print()

def renal_function(result):
    categories = {
        range(90, 5000): "Normal renal function",
        range(60, 90): "Mild renal function",
        range(45, 60): "Mild-moderate renal function",
        range(30, 45): "Moderate-severe renal function",
        range(15, 30): "Severe reduction",
        range(0, 15): "Kidney Failure"
    }

    int_result = int(result)

    for gfr in categories:
        if int_result in gfr:
            return categories[gfr]
# Execution
if __name__ == "__main__":
    main()
