#Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

#E = m * c**2

c : int = 299792458  # The speed of light in m/s

mass_in_kg : float = float(input("Please enter mass in kg : "))

energy_in_joules: float = mass_in_kg * c**2

print(f"Energy in joules: {energy_in_joules}")

Solution
Please enter mass in kg : 34
Energy in joules: 3.0557676077051796e+18
