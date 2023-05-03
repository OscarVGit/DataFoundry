import pandas as pd

# Load the JSON file
with open('surcharge_data.json', 'r') as file:
    data = pd.read_json(file)


# Reset the index and rename the columns
#data = data.reset_index().rename(columns={'index': 'tripID'})

# Reorder the columns
#data = data[['tripID', 'improvement_surcharge', 'congestion_surcharge']]

# Save the data as a CSV file
data.to_csv('surchage_data_.csv', index=False)

# Print the data
print(data)