import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    # Remove useless empty columns
    df = df.drop(columns=['New', 'PendingS'], errors='ignore')

    # Convert date
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Fix numeric columns
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df['Qty'] = pd.to_numeric(df['Qty'], errors='coerce')

    # Drop rows only where important values are missing
    df = df.dropna(subset=['Order ID', 'Date', 'Amount', 'Category'])

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Keep valid sales only
    df = df[df['Amount'] > 0]

    return df