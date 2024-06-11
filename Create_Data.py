import os
import pandas as pd
import numpy as np

# Create the flights_data directory if it doesn't exist
if not os.path.exists('flights_data'):
    os.makedirs('flights_data')

# Define the columns for the flight data
columns = ['flight_id', 'origin', 'destination', 'airline', 'status', 'delay_minutes', 'num_passengers', 'distance', 'flight_duration']

# Define some sample data for the columns
airports = ['JFK', 'LGA', 'EWR']
airlines = ['Delta', 'United', 'American']
statuses = ['On Time', 'Delayed', 'Cancelled']

# Weights for delay based on airlines and origin airports
airline_delay_weights = {'Delta': 3, 'United': 2, 'American': 1}  # More delayed flights for Delta
origin_delay_weights = {'JFK': 1, 'LGA': 2, 'EWR': 3}  # More delayed flights from EWR

# Generate and save multiple CSV files
num_files = 1000
num_rows_per_file = 1000

for i in range(num_files):
    # Generate random flight data
    origins = np.random.choice(airports, num_rows_per_file)
    airlines_sample = np.random.choice(airlines, num_rows_per_file)
    statuses_sample = np.random.choice(statuses, num_rows_per_file)
    
    delay_minutes = []
    for j in range(num_rows_per_file):
        # Ensure fewer delay minutes equal to 0 or -100 if flight is cancelled
        if statuses_sample[j] == 'Cancelled':
            delay_minutes.append(-100)
        elif np.random.random() < 0.2:  # 20% chance of 0 delay minutes
            delay_minutes.append(0)
        else:
            base_delay = np.random.randint(0, 61)  # Base delay between 0 and 60 minutes
            airline_delay = airline_delay_weights[airlines_sample[j]] * np.random.randint(0, 61)  # Additional delay based on airline
            origin_delay = origin_delay_weights[origins[j]] * np.random.randint(0, 61)  # Additional delay based on origin
            delay_minutes.append(base_delay + airline_delay + origin_delay)

    data = {
        'flight_id': np.arange(i * num_rows_per_file, (i + 1) * num_rows_per_file),
        'origin': origins,
        'destination': np.random.choice(airports, num_rows_per_file),
        'airline': airlines_sample,
        'status': statuses_sample,
        'delay_minutes': delay_minutes,
        # Increase the range for number of passengers and distance
        'num_passengers': np.random.randint(150, 701, num_rows_per_file),  # Larger range for passengers
        'distance': np.random.randint(1000, 10001, num_rows_per_file),  # Larger range for distance
        'flight_duration': np.random.randint(30, 601, num_rows_per_file)
    }
    
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv(f'flights_data/flights_data_{i+1}.csv', index=False)

print("CSV files created in the 'flights_data' folder.")
