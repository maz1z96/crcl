# Cockcroft-Gault CrCl, mL/min = (140 – age) × (weight, kg) × (1.23 for male or 1.04 for female) / (Cr, micromol/L)
def main():
    parameters = {
        "Age": int,
        "Weight (kg)": float,
        "Creatinine (micromol/L)": float,
        }

    small_para = {}
    for parameter in parameters:
        parameter_name = parameter.split("(")[0].strip().casefold()
        small_para[parameter_name] = get_parameter(parameter, parameters[parameter])

    constant = get_constant()

    crcl = (140 - small_para["age"]) * small_para["weight"] * constant / small_para["creatinine"]

    crcl = round(crcl, 2)
    reading = renal_function(crcl)

    print()
    print(f'CrCl = {crcl} ml/min')
    print(f'Renal function = {reading}')

def get_parameter(prompt, cast_type, min=0):
    while True:
        try:
            number = cast_type(input(f'{prompt}: '))
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
        (90, float('inf')): "Normal renal function",
        (60, 90): "Mild renal function",
        (45, 60): "Mild-moderate renal function",
        (30, 45): "Moderate-severe renal function",
        (15, 30): "Severe reduction",
        (0, 15): "Kidney Failure"
    }

    for gfr_range, description in categories.items():
        if gfr_range[0] <= result < gfr_range[1]:
            return description
# Execution
if __name__ == "__main__":
    main()
