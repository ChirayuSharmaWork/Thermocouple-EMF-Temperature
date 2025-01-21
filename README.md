# Thermocouple-EMF-Temperature

This repository contains a Python script to convert a given EMF (Electromotive Force) value to temperature for a T-type thermocouple. The conversion is achieved using the `numpy.polyfit` method to determine the required polynomial coefficients based on calibration data.

## Features
- Supports conversion of EMF to temperature for T-type thermocouples.
- Utilizes `numpy` for polynomial fitting and efficient computation.
- Accurate within the typical temperature range of T-type thermocouples (-200°C to 400°C).

## How It Works
1. **Polynomial Fitting**: 
   - The script uses `numpy.polyfit` to fit a polynomial to the calibration data.
   - The degree of the polynomial is chosen for optimal accuracy based on the thermocouple range.
2. **Conversion**:
   - The fitted polynomial is used to calculate the temperature for a given EMF.

## Getting Started
### Prerequisites
- Python 3.6 or higher
- Required libraries: `numpy`

Install the required libraries using pip:
```bash
pip install numpy
