import yfinance as yf
import pandas as pd

# Load the stock weightage data from CSV
df_weights = pd.read_csv('stocks.csv')

# Convert stock tickers to the proper format for Yahoo Finance (e.g., appending .NS for NSE stocks)
df_weights['Ticker'] = df_weights['Ticker'].apply(lambda x: f"{x}.NS" if x.isalpha() else x)

# User inputs
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")
investment_amount = float(input("Enter total investment amount: "))

# Create a dataframe to store the results
result_df = pd.DataFrame()

# Loop through each stock in the dataframe
for _, row in df_weights.iterrows():
    stock = row['Ticker']
    weightage = row['Weightage']
    
    # Calculate the amount allocated to this stock based on the weightage
    allocated_amount = investment_amount * weightage
    
    # Fetch historical data for the stock
    data = yf.download(stock, start=start_date, end=end_date)
    
    if data.empty:
        print(f"No data found for {stock}")
        continue

    # Calculate the number of shares that can be bought each day
    data['Allocated_Amount'] = allocated_amount
    data['Shares_Bought'] = data['Close'].apply(lambda x: round(allocated_amount / x, 2))  # Round to 2 decimal places
    
    # Rename Shares_Bought column to the stock ticker name for easier identification
    result_df[stock] = data['Shares_Bought']

# Save the results to an Excel file
result_df.to_excel('investment_plan.xlsx')
print("Investment plan has been saved to investment_plan.xlsx")
