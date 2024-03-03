import math

# Defining the data
data = [
    {"Day": "D1", "Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Wind": "Weak", "Play Tennis": "No"},
    {"Day": "D2", "Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Wind": "Strong", "Play Tennis": "No"},
    {"Day": "D3", "Outlook": "Overcast", "Temperature": "Hot", "Humidity": "High", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Day": "D4", "Outlook": "Rain", "Temperature": "Mild", "Humidity": "High", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Day": "D5", "Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Day": "D6", "Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "Play Tennis": "No"},
    {"Day": "D7", "Outlook": "Overcast", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "Play Tennis": "Yes"},
    {"Day": "D8", "Outlook": "Sunny", "Temperature": "Mild", "Humidity": "High", "Wind": "Weak", "Play Tennis": "No"},
    {"Day": "D9", "Outlook": "Sunny", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Day": "D10", "Outlook": "Rain", "Temperature": "Mild", "Humidity": "Normal", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Day": "D11", "Outlook": "Sunny", "Temperature": "Mild", "Humidity": "Normal", "Wind": "Strong", "Play Tennis": "Yes"},
    {"Day": "D12", "Outlook": "Overcast", "Temperature": "Mild", "Humidity": "High", "Wind": "Strong", "Play Tennis": "Yes"},
    {"Day": "D13", "Outlook": "Overcast", "Temperature": "Hot", "Humidity": "Normal", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Day": "D14", "Outlook": "Rain", "Temperature": "Mild", "Humidity": "High", "Wind": "Strong", "Play Tennis": "No"}
]

# Function to calculate entropy
def entropy(data):
    # Count the occurrences of each label
    label_counts = {}
    for entry in data:
        label = entry["Play Tennis"]
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1
    
    # Calculate entropy
    total_samples = len(data)
    entropy_value = 0.0
    for count in label_counts.values():
        probability = count / total_samples
        entropy_value -= probability * math.log2(probability)
    
    return entropy_value

# Function to calculate information gain
def information_gain(data, attribute):
    # Partition the data based on the attribute values
    partitions = {}
    for entry in data:
        value = entry[attribute]
        if value in partitions:
            partitions[value].append(entry)
        else:
            partitions[value] = [entry]
    
    # Calculate the weighted average entropy
    total_samples = len(data)
    weighted_entropy = 0.0
    for partition in partitions.values():
        partition_size = len(partition)
        weighted_entropy += (partition_size / total_samples) * entropy(partition)
    
    # Calculate information gain
    return entropy(data) - weighted_entropy

# Calculate entropy and gain for each attribute
attributes = ["Outlook", "Temperature", "Humidity", "Wind"]
for attribute in attributes:
    entropy_value = entropy(data)
    gain = information_gain(data, attribute)
    print(f"Entropy for {attribute}: {entropy_value}")
    print(f"Information Gain for {attribute}: {gain}")
    print()
