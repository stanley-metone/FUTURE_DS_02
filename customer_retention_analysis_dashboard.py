import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = 'CSV.csv'
df = pd.read_csv(file_path)

# Basic cleaning
print("Dataset Preview:")
print(df.head())

# Convert date columns if present
for col in df.columns:
    if 'date' in col.lower():
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Churn Analysis
if 'Churn' in df.columns:
    churn_rate = df['Churn'].value_counts(normalize=True) * 100
    print("\nChurn Rate (%):")
    print(churn_rate)

    churn_counts = df['Churn'].value_counts()
    churn_counts.plot(kind='bar', title='Churn Distribution')
    plt.show()

# Retention Trends
if 'SubscriptionLength' in df.columns:
    df['SubscriptionLength'].hist()
    plt.title('Subscription Length Distribution')
    plt.show()

# Customer Lifetime Value (if revenue present)
if 'MonthlyRevenue' in df.columns and 'SubscriptionLength' in df.columns:
    df['CLV'] = df['MonthlyRevenue'] * df['SubscriptionLength']
    print("\nAverage CLV:", df['CLV'].mean())

    df['CLV'].hist()
    plt.title('Customer Lifetime Value Distribution')
    plt.show()

# Key Drivers (simple correlation)
numeric_cols = df.select_dtypes(include=['float64','int64']).columns
if len(numeric_cols) > 1:
    corr = df[numeric_cols].corr()
    print("\nCorrelation Matrix:")
    print(corr)

# Save summary
summary = {
    'Total Customers': len(df),
    'Churn Rate (%)': churn_rate.get(1, None) if 'Churn' in df.columns else None,
    'Avg CLV': df['CLV'].mean() if 'CLV' in df.columns else None
}

print("\nSummary:")
print(summary)

# Export cleaned dataset
df.to_csv('processed_customer_data.csv', index=False)

print("\nDashboard generation complete. Use visual outputs for reporting.")
