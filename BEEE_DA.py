import math
import cmath

print("\n\n")

# User Specifications

R = float(input("Enter resistor value (in ohms): "))
L = float(input("Enter inductor value (in Henri): "))
C = float(input("Enter capacitor value (in farad): "))
current = float(input("Enter current source (in volts): "))
f = float(input("Enter frequency (in Hertz): "))



# Function to calculate impedance, current, voltage, inductive_reactance and capacitive_reactance

def calculate_impedance(resistor, frequency, inductor, capacitor, current_source):

    xl = 2 * math.pi * frequency * inductor
    xc = 1/(2*math.pi*frequency*capacitor)

    impedance = complex(resistor, (xl-xc))

    current = current_source/impedance

    voltage = current * resistor

    return impedance, current,voltage, xl, xc


# Function to calculate power (apparent, active and reactive)

def calculate_power(voltage, current):
    apparent = abs(voltage) * abs(current)

    phase_angle = math.atan2(current.imag, current.real) - math.atan2(voltage.imag, voltage.real)

    real = abs(voltage) * abs(current) * math.cos(phase_angle)

    reactive =  abs(voltage) * abs(current) * math.sin(phase_angle)

    return apparent, real, reactive



# Main Driver code

def main():

    impedance, current_flow, voltage, XL, XC = calculate_impedance(R, f, L, C, current)
    apparent_power, real_power, reactive_power = calculate_power(voltage, current_flow)

    newline = '\n'

    print("\n\nGeneral Information:\n\n")

    print("\nImpedance:\n\n")
    print(f"Complex Form: {impedance} ohms {newline}Absolute Form: {abs(impedance)} ohms {newline}Polar Form: {cmath.polar(impedance)}")

    print("\n\n")

    print(f"Inductive Reactance (XL): {XL} ohms")
    print(f"Capacitive Reactance (XC): {XC} ohms")

    print("\n\nCurrent:\n\n")
    print(f"Complex: {current_flow} (A) {newline}Absolute: {abs(current_flow)} (A) {newline}Polar: {cmath.polar(current_flow)}")

    print("\n\nVoltage:\n\n")
    print(f"Complex: {voltage} (v) {newline}Absolute: {abs(voltage)} (v) {newline}Polar: {cmath.polar(voltage)}")

    print("\n\nPower Information\n\n")
    print(f"Apparent power: {abs(apparent_power)} VA {newline}Active Power: {abs(real_power)} W {newline}Reactive power: {abs(reactive_power)} VAR")

    print("\n\n")





if __name__ == "__main__":
    main()
