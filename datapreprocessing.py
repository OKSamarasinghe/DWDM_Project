#import libraries
import pandas as pd

# Load the dataset into a pandas DataFrame
data = pd.read_csv('hotel_bookings 2.csv')

# View the data
print(data)

# View information about the data
data.info()

# Access a specific column
print(data['country'])

# Access a specific row
print(data.loc[1])

# Select the first 1000 records
data = data.head(1000)

# View information about the data after selecting 1000 records
data.info()

# View the data after selecting 1000 records
print(data)

# Access a specific column after selecting 1000 records
print(data['country'])

# Access a specific row after selecting 1000 records
print(data.loc[1])

# Get the number of records
print(data.shape)

# Check for missing values
print(data.isnull().sum())

# Fill missing values in the country column with the most frequent value
data['country'].fillna(data['country'].mode()[0], inplace=True)

# Fill missing values in the agent column with the most frequent value
data['agent'].fillna(data['agent'].mode()[0], inplace=True)

# Check for missing values after filling
print(data.isnull().sum())

# View information about the data after filling missing values
data.info()

# Check for duplicate values
print(data.duplicated().sum())

# Remove duplicate rows
data = data.drop_duplicates()

# Verify that duplicates are removed
print(data.duplicated().sum())

# Describe the data
print(data.describe())

# Save the updated dataset to a CSV file
data.to_csv('updated_hotel_bookings.csv')

# Download the updated CSV file to the user's local computer
files.download('updated_hotel_bookings.csv')

# Install scikit-learn
!pip install scikit-learn

# Iterate over each column and apply LabelEncoder if it's not numerical
for column in data.columns:
  if data[column].dtype == 'object': # Check if the column is categorical (object type)
    le = preprocessing.LabelEncoder()
    data[column] = le.fit_transform(data[column])

# Save the ARFF data to a file
with open('updated_hotel_bookings.arff', 'w') as f:
  f.write('@RELATION hotel_bookings\n\n')

  # Write the attribute names
  for i, column in enumerate(data.columns):
    f.write(f'@ATTRIBUTE {column} NUMERIC\n') # Use actual column names

  # Write the data
  f.write('\n@DATA\n')
  for _, row in data.iterrows():
    f.write(','.join(str(x) for x in row) + '\n')

# Download the ARFF file to the user's local computer
files.download('updated_hotel_bookings.arff')
