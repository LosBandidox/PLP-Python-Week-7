# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
# Load the dataset
try:
    file_path = 'Student Mental health.csv'  # Path to the uploaded dataset
    data = pd.read_csv(file_path)
    
    # Display the first few rows
    print("First 5 rows of the dataset:")
    print(data.head())
    
    # Explore the structure of the dataset
    print("\nDataset Information:")
    data.info()
    
    # Check for missing values
    print("\nMissing values in each column:")
    print(data.isnull().sum())

    # Clean the dataset by filling missing values (Age column)
    median_age = data['Age'].median()
    data['Age'].fillna(median_age, inplace=True)
    print("\nMissing values after cleaning:")
    print(data.isnull().sum())
except FileNotFoundError:
    print("The file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
# Compute basic statistics for numerical columns
print("\nBasic Statistics for Numerical Columns:")
print(data.describe())

# Perform groupings and compute mean
print("\nMean Age by Gender:")
gender_age_mean = data.groupby('Choose your gender')['Age'].mean()
print(gender_age_mean)

# Perform groupings and compute depression rates by gender
print("\nProportion of Students with Depression by Gender:")
depression_rate = data.groupby('Choose your gender')['Do you have Depression?'].value_counts(normalize=True)
print(depression_rate)

# Identify interesting patterns: Correlation between age and seeking treatment
print("\nCorrelation Between Age and Seeking Treatment:")
age_treatment_correlation = data.groupby('Did you seek any specialist for a treatment?')['Age'].mean()
print(age_treatment_correlation)

# Task 3: Data Visualization
sns.set(style="whitegrid")  # Set the visual style for seaborn plots

# 1. Line Chart: Age trend over timestamps
plt.figure(figsize=(10, 5))
plt.plot(data['Timestamp'], data['Age'], marker='o', linestyle='-', label='Age')
plt.title('Age Trend Over Time', fontsize=14)
plt.xlabel('Timestamp', fontsize=12)
plt.ylabel('Age', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar Chart: Average Age by Gender
plt.figure(figsize=(8, 5))
sns.barplot(x='Choose your gender', y='Age', data=data, ci=None, palette='pastel')
plt.title('Average Age by Gender', fontsize=14)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Average Age', fontsize=12)
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of Age
plt.figure(figsize=(8, 5))
sns.histplot(data['Age'], bins=10, kde=True, color='skyblue')
plt.title('Distribution of Age', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Relationship between Age and CGPA
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='What is your CGPA?', data=data, hue='Choose your gender', palette='muted')
plt.title('Relationship Between Age and CGPA', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('CGPA', fontsize=12)
plt.legend(title='Gender')
plt.tight_layout()
plt.show()
