import matplotlib.pyplot as plt

# Power budgeting calculator for UAV/aircraft
#Tool created by, SADIQ ALI MIR (UG Aerospace Engineering student RVCE), under the guidance of 
#Prof. BENJAMIN ROHIT (Department of Aerospace Engineering RVCE)

# Define input parameters
battery_voltage = float(input("Enter battery voltage (V): "))
battery_capacity = float(input("Enter battery capacity (mAh): "))
flight_time = float(input("Enter desired flight time (minutes): "))
motor_efficiency = float(input("Enter motor efficiency (%): "))
propeller_efficiency = float(input("Enter propeller efficiency (%): "))
system_efficiency = float(input("Enter system efficiency (%): "))
avg_power_consumption = float(input("Enter average power consumption (W): "))
reserve_factor = float(input("Enter reserve factor (%): "))
safety_factor = float(input("Enter safety factor (%): "))
lighting_power = float(input("Enter power consumption by lighting system (W): "))
avionics_power = float(input("Enter power consumption by avionics system (W): "))
communication_power = float(input("Enter power consumption by communication system (W): "))

# Convert battery capacity from mAh to Wh
battery_capacity = battery_capacity / 1000 * battery_voltage

# Convert flight time from minutes to hours
flight_time = flight_time / 60

# Calculate total energy required (Wh)
energy_required = (avg_power_consumption + lighting_power + avionics_power + communication_power) * flight_time / system_efficiency

# Apply reserve factor to total energy required
energy_required *= 1 + reserve_factor / 100

# Calculate total energy available from battery (Wh)
energy_available = battery_capacity * battery_voltage / 1000

# Apply safety factor to total energy available
energy_available *= 1 - safety_factor / 100

# Calculate energy consumed by propulsion system (Wh)
propulsion_energy = energy_required * motor_efficiency / propeller_efficiency

# Calculate energy available for other systems (Wh)
other_energy = energy_available - propulsion_energy

# Print results
print("Total energy required (with reserve factor): {:.2f} Wh".format(energy_required))
print("Total energy available from battery (with safety factor): {:.2f} Wh".format(energy_available))
print("Energy consumed by propulsion system: {:.2f} Wh".format(propulsion_energy))
print("Energy available for other systems: {:.2f} Wh".format(other_energy))

# Calculate estimated flight time
flight_time_est = other_energy * system_efficiency / (avg_power_consumption + lighting_power + avionics_power + communication_power) * 60
print("Estimated flight time (based on other system energy): {:.2f} minutes".format(flight_time_est))

# Generate a pie chart showing the energy breakdown
labels = ['Propulsion system', 'Lighting system', 'Avionics system', 'Communication system', 'Other systems']
sizes = [propulsion_energy, lighting_power * flight_time, avionics_power * flight_time, communication_power * flight_time, other_energy]
colors = ['red', 'yellow', 'orange', 'blue', 'green']
explode = (0.1, 0, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title('Power Budgeting Breakdown')

plt.show()
