# einstein.py

def calculate_energy_equivalence(mass):
    # Speed of light in meters per second
    speed_of_light = 300000000
    if mass < 0:
        raise ValueError("Mass cannot be negative")   

    # E = mc^2 formula
    energy_equivalence = mass * speed_of_light ** 2
    return energy_equivalence



if __name__ == "__main__":
    # Prompt the user for mass input
    mass = int(input("Enter mass (in kilograms): "))

    # Calculate and output the equivalent energy
    energy_equivalence = calculate_energy_equivalence(mass)
    print(f"The equivalent energy is: {energy_equivalence} Joules")


