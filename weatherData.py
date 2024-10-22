def aggregate_weather_data(records) -> list:
    # Dictionary to hold the aggregated data
    aggregated_data = {}
    

    for record in records:
        city = record.get('city')
        temperature = record.get('temperature')
        humidity = record.get('humidity')
        

        if city not in aggregated_data:
            aggregated_data[city] = {
                'total_temperature': 0,
                'total_humidity': 0,
                'count': 0
            }
        

        if temperature is not None:
            aggregated_data[city]['total_temperature'] += temperature

        if humidity is not None:
            aggregated_data[city]['total_humidity'] += humidity
        

        aggregated_data[city]['count'] += 1
    

    results = {}
    for city, data in aggregated_data.items():
        count = data['count']
        avg_temperature = data['total_temperature'] / count if count > 0 else None
        avg_humidity = data['total_humidity'] / count if count > 0 else None
        
        results[city] = {
            'average_temperature': avg_temperature,
            'average_humidity': avg_humidity
        }
    
    return results


records = [
    {'city': 'Karachi', 'temperature': 65, 'humidity': 70},
    {'city': 'Hyderabad', 'temperature': 90},
    {'city': 'Delhi', 'humidity': 40, 'temparature': None},
    {'city': 'Karachi', 'temperature': 75, 'humidity': 60},
    {'city': 'Delhi', 'temperature': 50, 'humidity': None},
]

# function Call
average_weather = aggregate_weather_data(records)

#  print the result
print(average_weather)