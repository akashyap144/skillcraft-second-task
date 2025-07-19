# SkillCraft Internship - Task 02  
## Titanic Dataset - Data Cleaning & Exploratory Data Analysis (EDA)  

This project is part of my **SkillCraft Data Science Internship**.  
The task focuses on cleaning and analyzing the famous **Titanic dataset** to extract meaningful insights about passenger survival rates.

---

## 🔥 Key Features  
✅ Data cleaning and handling of missing values  
✅ Conversion of categorical data into numerical format  
✅ Exploratory Data Analysis (EDA) with visualizations  
✅ Insights into passenger survival patterns based on **gender, class, and age**  

---

## 🛠 Technologies Used  
- Python  
- Pandas  
- Matplotlib  
- Seaborn  

---

## 📂 Files in this Repository  
- `2ndtask.py` → Python script for cleaning and analyzing the dataset  
- '2ndtask.csv'→ Cleaned dataset (if generated)  
- Graphs:  
  - `survival_by_gender.png`  
  - `survival_by_class.png`  
  - `age_distribution.png`  

---

## ✅ Code Snippet  

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("2ndtask.csv")
print("✅ Data Loaded Successfully!")
print(df.head())

# Data Cleaning - Handle Missing Values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Convert Categorical to Numeric
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Save Cleaned Data
df.to_csv("2ndtask.csv", index=False)

# EDA - Survival by Gender
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.savefig("survival_by_gender.png")
plt.show()

# EDA - Survival by Class
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Class")
plt.savefig("survival_by_class.png")
plt.show()

# EDA - Age Distribution
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Age Distribution of Passengers")
plt.savefig("age_distribution.png")
plt.show()# skillcraft-second-task
This repository contains the solution for Task 02 of the SkillCraft Technology internship program. The objective of this task is to perform data cleaning and exploratory data analysis (EDA) on a dataset of choice — in this case, the Titanic dataset from Kaggle


Author
Kumar Akash Deep
Skillcraft Data Science Intern
