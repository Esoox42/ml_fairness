import csv
import random

# Set the desired probability for males
male_probability = 0.6

# Generate the list of genders based on the desired probability
genders = ['male' if random.random(
) < male_probability else 'female' for _ in range(45211)]

# Create and write the data to the CSV file
with open('gender_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['gender'])  # Write the header
    writer.writerows([[gender] for gender in genders])
