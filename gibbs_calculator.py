# Gibbs Free Energy Calculator
def calculate_gibbs_free_energy(enthalpy, entropy, temperature):
    """
    Calculate the Gibbs free energy using the formula: ΔG = ΔH - T * ΔS
    where ΔH is the change in enthalpy, ΔS is the change in entropy,
    and T is the temperature in Kelvin.
    
    Returns:
    fload: Gibbs free energy in kJ/mol
    
    """
    # Calculating Gibbs free energy
    gibbs_free_energy = enthalpy - (temperature * entropy)
    return gibbs_free_energy

def main():
    print ("Gibbs Free Energy Calculator")
    print("=============================")

    try:
        # Taking inputs
        enthalpy = float(input("Enter the change in enthalpy (ΔH) (kJ/mol): "))
        entropy = float(input("Enter the change in entropy (ΔS) (J/mol*K): "))  
        temperature = float(input("Enter the temperature (T) in Kelvin: "))

        #Validate inputs
        if enthalpy < 0:
            print("Error: Enthalphy must be greater than 0 Kelvin. ")
            return
        elif entropy < 0:
            print("Error: Entropy must be greater than 0 J/mol*K. ")
            return
        elif temperature < 0:
            print("Error: Temperature must be greater than 0 Kelvin. ")
            return
        
        # Calculate Gibbs free energy
        gibbs_energy = calculate_gibbs_free_energy(enthalpy, entropy, temperature)
        
        #Display Results
        print(f"Gibbs Free Energy (ΔG) = {gibbs_energy:.2f} kJ/mol")
        print("=================================")

    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

