# Power Budgeting Calculator for UAV/Aircraft

This Python script is designed to calculate the power budget for a UAV or aircraft, based on various input parameters. It calculates the total energy required, total energy available from the battery, energy consumed by the propulsion system, and energy available for other systems. It also estimates the flight time based on the available energy.

## Background

Power budgeting is an important aspect of UAV and aircraft design. It involves calculating the power requirements for all the systems on board the vehicle, and ensuring that the available power from the battery or other power source is sufficient to meet those requirements. The power budget can be affected by a range of factors, including the type of motor and propeller used, the efficiency of the propulsion and other systems, and the power consumed by avionics, lighting, and communication systems.


## Usage

To use the script, you need to have Python installed on your computer. You also need to install the Matplotlib library to generate the pie chart. You can install it using the following command:
```
`pip install matplotlib`
```

To run the script, open the command prompt or terminal and navigate to the directory where the script is saved. Then type the following command:
```
python power_budgeting.py

```

You will then be prompted to enter the input parameters one by one. Once all the input parameters are entered, the script will output the results and show a pie chart.
Requirements

The script requires Python 3.x and the Matplotlib library to be installed.




## Input Parameters

The input parameters required by the script are as follows:

    Battery voltage (V)
    Battery capacity (mAh)
    Desired flight time (minutes)
    Motor efficiency (%)
    Propeller efficiency (%)
    System efficiency (%)
    Average power consumption (W)
    Reserve factor (%)
    Safety factor (%)
    Power consumption by lighting system (W)
    Power consumption by avionics system (W)
    Power consumption by communication system (W)

## Output

The script outputs the following:

    Total energy required (with reserve factor) in Wh
    Total energy available from battery (with safety factor) in Wh
    Energy consumed by propulsion system in Wh
    Energy available for other systems in Wh
    Estimated flight time (based on other system energy) in minutes
    A pie chart showing the energy breakdown

## Formulae    

The following formulae are used by the script:

    `battery_capacity` = `battery_capacity` / 1000 * `battery_voltage` - converts battery capacity from mAh to Wh
    `flight_time` = `flight_time` / 60 - converts flight time from minutes to hours
    `energy_required` = (`avg_power_consumption` + `lighting_power` + `avionics_power` + `communication_power`) * `flight_time` / `system_efficiency` - calculates total energy required (Wh)
    `energy_required` *= 1 + `reserve_factor` / 100 - applies reserve factor to total energy required
    `energy_available` = `battery_capacity` * `battery_voltage` / 1000 - calculates total energy available from battery (Wh)
    energy_available` *= 1 - `safety_factor` / 100 - applies safety factor to total energy available
    `propulsion_energy` = `energy_required` * `motor_efficiency` / `propeller_efficiency` - calculates energy consumed by propulsion system (Wh)
    `other_energy` = `energy_available` - `propulsion_energy` - calculates energy available for other systems (Wh)
    `flight_time_est` = `other_energy` * ``system_efficiency / (`avg_power_consumption` + `lighting_power` + `avionics_power` + `communication_power`) * 60 - estimates flight time based on other system energy



## Future Improvements

Future improvements to the script could include:

    Adding support for multiple batteries and battery configurations
    Adding support for different motor and propeller types
    Adding support for different flight modes (e.g. hover, cruise)
    Adding support for different altitude and temperature conditions



## Authors
This tool was created by Sadiq Ali (UG Aerospace Engineering student at R.V College of Engineering),
under the guidance of Prof. Benjamin Rohit (Department of Aeropace Engineering, RVCE).

## License
This tool is licensed under the MIT License. See the LICENSE file for more details.
