import random

# Define the number of apples to generate
num_apples = 1000

# Define the range of values for each parameter
diameter_range = (2.0, 4.0)
weight_range = (50, 150)
skin_color_options = ['green', 'yellow', 'red']
taste_options = ['sweet', 'sour', 'bitter']

# Generate the synthetic data
apples = []
for i in range(num_apples):
    diameter = round(random.uniform(diameter_range[0], diameter_range[1]), 2)
    weight = random.randint(weight_range[0], weight_range[1])
    skin_color = random.choice(skin_color_options)
    taste = random.choice(taste_options)
    apples.append({'diameter': diameter, 'weight': weight, 'skin_color': skin_color, 'taste': taste})

# Output the data to a CSV file
import csv
with open('synthetic_apples.csv', 'w', newline='') as csvfile:
    fieldnames = ['diameter', 'weight', 'skin_color', 'taste']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for apple in apples:
        writer.writerow(apple)
