# Cockcroft-Gault CrCl, mL/min = (140 – age) × (weight, kg) × (1.23 for male or 1.04 for female) / (Cr, micromol/L)

age = int(input("Age "))
weight = float(input("Weight (kg) "))
sex = input("Sex (M/F) ").title()
cr = float(input("Serum Cr (micromol/L) "))

if sex == "M":
    constant = 1.23
elif sex == "F":
    constant = 1.04

crcl = (140 - age) * weight * constant / cr
crcl = round(crcl, 2)

print()
print(f'CrCl = {crcl} ml/min')

# Use cases
## Sex is not M or F - is there a way to only select m or f - inquirer
## Age, Weight, Cr are non-numbers
## Add group of renal impairment - dictionary