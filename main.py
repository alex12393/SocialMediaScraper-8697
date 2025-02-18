```python
# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a dictionary of data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'James'],
    'Age': [28, 24, 35, 32, 30],
    'City': ['New York', 'Paris', 'Berlin', 'Madrid', 'London'],
    'Profession': ['Doctor', 'Engineer', 'Architect', 'Scientist', 'Lawyer'],
    'Salary': [70000, 80000, 85000, 90000, 95000]
}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Show the dataframe
print(df)

# Basic Data Processing

# 1. Data Inspection
print(df.shape)  # get the shape of the data
print(df.columns)  # get the column names
print(df.info())  # information about the data
print(df.describe())  # statistical details of the data

# 2. Data Cleaning
df.isnull().sum()  # check missing values
df.duplicated().sum()  # check duplicate values

# 3. Data Manipulation

# Add a new column
df['Experience'] = [10, 2, 8, 6, 9]
print(df)

# Delete a column
df.drop('Experience', axis=1, inplace=True)
print(df)

# Rename columns
df.rename(columns={'Name': 'First Name'}, inplace=True)
print(df)

# Change the index
df.set_index('First Name', inplace=True)
print(df)

# 4. Data Filtering

# Filter the data
filter = df['Age'] > 30
print(df[filter])

# 5. Data Sorting

# Sort the data
sorted_df = df.sort_values(by='Age')
print(sorted_df)

# 6. Data Aggregation

# Group by Profession
grouped = df.groupby('Profession')
print(grouped['Salary'].mean())

# 7. Data Visualization

# Histogram
df['Age'].plot(kind='hist')
plt.show()

# Boxplot
df['Salary'].plot(kind='box')
plt.show()

# Bar chart
df['Profession'].value_counts().plot(kind='bar')
plt.show()

# Scatter plot
df.plot(kind='scatter', x='Age', y='Salary')
plt.show()
```
Цей код виконує базову обробку даних, включаючи інспекцію даних, очищення даних, маніпуляції з даними, фільтрацію даних, сортування даних, агрегацію даних та візуалізацію даних.