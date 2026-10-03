import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# -----------------------------------
#Load Datasets
#--------------------------------------
visits = pd.read_csv('../data/Patient_Visits.csv')
# If demographics file exists, merge it
try:
    demographics = pd.read_csv('../data/Patient_Demographics.csv')
    df = visits.merge(demographics, on='Patient_ID', how='left')
except FileNotFoundError:
    df = visits.copy()

# -----------------------------
# Data Cleaning
# -----------------------------
df['Wait_Time_Minutes'] = df['Wait_Time_Minutes'].fillna(df['Wait_Time_Minutes'].median())
df['Satisfaction_Score'] = df['Satisfaction_Score'].fillna(df['Satisfaction_Score'].median())
df['Actual_Duration'] = df['Actual_Duration'].fillna(df['Scheduled_Duration'])

# -----------------------------
# Derived Metrics
# -----------------------------
df['Delay'] = df['Actual_Duration'] - df['Scheduled_Duration']
df['Visit_Efficiency'] = df['Actual_Duration'] / df['Scheduled_Duration']

# -----------------------------
# Summary Statistics
# -----------------------------
print("Summary Statistics:")
print(df.describe())

# -----------------------------
# Visualization 1: Wait Time Distribution
# -----------------------------
plt.figure(figsize=(10,5))
sns.histplot(df['Wait_Time_Minutes'], kde=True, color='blue')
plt.title('Patient Wait Time Distribution')
plt.xlabel('Wait Time (Minutes)')
plt.ylabel('Frequency')
plt.show()

# -----------------------------
# Visualization 2: Satisfaction vs Wait Time
# -----------------------------
plt.figure(figsize=(10,5))
sns.scatterplot(data=df, x='Wait_Time_Minutes', y='Satisfaction_Score', hue='Department')
plt.title('Wait Time vs Satisfaction Score')
plt.xlabel('Wait Time (Minutes)')
plt.ylabel('Satisfaction Score')
plt.show()

# -----------------------------
# Provider Delay Ranking
# -----------------------------
provider_delay = df.groupby('Provider_Name')['Delay'].mean().sort_values(ascending=False)
print("\nProvider Delay Ranking:")
print(provider_delay)

# -----------------------------
# No-Show Analysis
# -----------------------------
no_show_count = len(df[df['Visit_Status'] == 'No-Show'])
print(f"\nTotal No-Show Visits: {no_show_count}")

# -----------------------------
# Department-Level Wait Time
# -----------------------------
dept_wait = df.groupby('Department')['Wait_Time_Minutes'].mean().sort_values(ascending=False)
print("\nAverage Wait Time by Department:")
print(dept_wait)
