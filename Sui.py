import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Step 1: Connect to CoinGecko API and fetch historical data for SUI
def fetch_crypto_data(coin_id='sui', days='30'):
    """
    Fetch historical price and volume data for the specified cryptocurrency
    from the CoinGecko API.
    
    Parameters:
    - coin_id: The ID of the cryptocurrency (default: 'sui').
    - days: The number of days of historical data to fetch (default: 30 days).
    
    Returns:
    - df: A pandas DataFrame with price and volume data.
    """
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart'
    params = {
        'vs_currency': 'usd',  # Currency for price data
        'days': days,          # Number of days for historical data
        'interval': 'daily'    # Daily interval for data
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # Convert price and volume data to pandas DataFrame
    prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    prices['timestamp'] = pd.to_datetime(prices['timestamp'], unit='ms')
    
    volumes = pd.DataFrame(data['total_volumes'], columns=['timestamp', 'volume'])
    volumes['timestamp'] = pd.to_datetime(volumes['timestamp'], unit='ms')
    
    # Merge price and volume data into one DataFrame
    df = pd.merge(prices, volumes, on='timestamp')
    
    return df

# Step 2: Perform analysis on the fetched data
def analyze_data(df):
    """
    Perform basic analysis on the cryptocurrency data by calculating
    moving averages and volatility.
    
    Parameters:
    - df: A pandas DataFrame containing historical price and volume data.
    
    Returns:
    - df: The DataFrame with added analysis columns.
    """
    # Calculate 7-day and 30-day simple moving averages (SMA)
    df['SMA_7'] = df['price'].rolling(window=7).mean()
    df['SMA_30'] = df['price'].rolling(window=30).mean()
    
    # Calculate price volatility (standard deviation of price over 7 days)
    df['Volatility_7'] = df['price'].rolling(window=7).std()

    return df

# Step 3: Plot graphs using matplotlib
def plot_data(df_30, df_90):
    """
    Plot price trends and moving averages using matplotlib for both 30 days
    and 90 days.
    
    Parameters:
    - df_30: A pandas DataFrame containing the 30-day historical and analyzed data.
    - df_90: A pandas DataFrame containing the 90-day historical and analyzed data.
    """
    plt.figure(figsize=(14, 12))
    
    # Subplot 1: 30 days - Plot price and moving averages
    plt.subplot(4, 1, 1)
    plt.plot(df_30['timestamp'], df_30['price'], label='Price (30 days)', color='blue')
    plt.plot(df_30['timestamp'], df_30['SMA_7'], label='7-Day SMA (30 days)', color='green', linestyle='--')
    plt.plot(df_30['timestamp'], df_30['SMA_30'], label='30-Day SMA (30 days)', color='red', linestyle='--')
    plt.title('SUI Price and Moving Averages (30 Days)')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()

    # Subplot 2: 30 days - Plot trading volume
    plt.subplot(4, 1, 2)
    plt.bar(df_30['timestamp'], df_30['volume'], label='Volume (30 days)', color='orange')
    plt.title('SUI Trading Volume (30 Days)')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    
    # Subplot 3: 90 days - Plot price and moving averages
    plt.subplot(4, 1, 3)
    plt.plot(df_90['timestamp'], df_90['price'], label='Price (90 days)', color='blue')
    plt.plot(df_90['timestamp'], df_90['SMA_7'], label='7-Day SMA (90 days)', color='green', linestyle='--')
    plt.plot(df_90['timestamp'], df_90['SMA_30'], label='30-Day SMA (90 days)', color='red', linestyle='--')
    plt.title('SUI Price and Moving Averages (90 Days)')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()

    # Subplot 4: 90 days - Plot trading volume
    plt.subplot(4, 1, 4)
    plt.bar(df_90['timestamp'], df_90['volume'], label='Volume (90 days)', color='orange')
    plt.title('SUI Trading Volume (90 Days)')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    
    plt.tight_layout()
    plt.show()

# Step 4: Output analysis tables using pandas
def output_tables(df_30, df_90):
    """
    Output the last few rows of the analyzed data as a table and optionally
    save the data to a CSV file.
    
    Parameters:
    - df_30: A pandas DataFrame containing the 30-day analyzed data.
    - df_90: A pandas DataFrame containing the 90-day analyzed data.
    """
    # Select columns for analysis and display the last 10 rows for both periods
    analysis_table_30 = df_30[['timestamp', 'price', 'SMA_7', 'SMA_30', 'Volatility_7']].tail(10)
    analysis_table_90 = df_90[['timestamp', 'price', 'SMA_7', 'SMA_30', 'Volatility_7']].tail(10)
    
    print("\nLast 10 Days of Analysis (30 days):")
    print(analysis_table_30)

    print("\nLast 10 Days of Analysis (90 days):")
    print(analysis_table_90)

    # Optionally, save the tables to CSV files
    analysis_table_30.to_csv('sui_crypto_analysis_30_days.csv', index=False)
    analysis_table_90.to_csv('sui_crypto_analysis_90_days.csv', index=False)
    print("\nTables saved as 'sui_crypto_analysis_30_days.csv' and 'sui_crypto_analysis_90_days.csv'.")

# Main function
def main():
    # Fetch data for the last 30 days
    df_30 = fetch_crypto_data('sui', '30')
    
    # Fetch data for the last 90 days
    df_90 = fetch_crypto_data('sui', '90')
    
    # Analyze the data for both periods
    df_30 = analyze_data(df_30)
    df_90 = analyze_data(df_90)
    
    # Plot the data for both periods
    plot_data(df_30, df_90)
    
    # Output the tables for both periods
    output_tables(df_30, df_90)

if __name__ == '__main__':
    main()
