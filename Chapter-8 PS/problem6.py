def inch_to_cms(inch):
    return inch * 2.54


n = int(input("Enter the measure in inches: "))

print(f"The corresponding measure in cms is: {inch_to_cms(n)}")
