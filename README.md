# Prime Factorization

## Overview
This Python function computes the prime factorization of a given integer `n`. It returns a list of tuples, where each tuple contains a prime factor and its corresponding exponent.

## Features
- **Prime Factorization**: Efficiently calculates the prime factors of a number.
- **Output Format**: Returns factors as a list of tuples, each containing the prime factor and its exponent.

## Requirements
- Python 3.x

## Usage
To use the `primeFactorization` function, simply call it with an integer value:

```python
result = primeFactorization(n)
```


# Weather Data Aggregator

## Overview
This Python function aggregates weather data from a list of records, calculating the average temperature and humidity for each city. It returns a dictionary with the average values for each city.

## Features
- **Data Aggregation**: Computes average temperature and humidity for each city.
- **Handles Missing Data**: Ignores missing temperature or humidity values in the calculations.

## Requirements
- Python 3.x

## Usage
To use the `aggregate_weather_data` function, call it with a list of weather records:

```python
result = aggregate_weather_data(records)
```


# DataManipulation.py

## Overview
This Python script connects to a MySQL database and updates the prices of products by increasing them by 10%. It then retrieves and displays the updated product names along with their new prices.

## Features
- **Update Product Prices**: Increase the price of all products by 10%.
- **Display Updated Prices**: Fetch and display the updated product names and their new prices.

## Requirements
- Python 3.x
- `mysql-connector-python` library

## Installation
To install the required library, run:

```bash
pip install mysql-connector-python