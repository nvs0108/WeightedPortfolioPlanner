# Weighted Portfolio Planner

**Weighted Portfolio Planner** is a Python tool that helps investors build an investment plan by allocating a total investment amount across multiple stocks according to user-defined weightages. It uses historical stock data from Yahoo Finance to simulate how many shares could be bought on each day within a selected date range.

## 📌 Features
- Reads stock tickers and investment weightages from a CSV file
- Fetches historical stock prices using `yfinance`
- Calculates share allocations based on weight and closing prices
- Outputs the plan to an Excel file (`investment_plan.xlsx`)

## 🗂️ Input
Prepare a `Stocks.csv` file in this format:

```csv
Ticker,Weightage
RELIANCE,0.3
TCS,0.25
INFY,0.2
HDFCBANK,0.25
```

✅ Tickers are automatically converted to Yahoo Finance format (e.g., `RELIANCE` → `RELIANCE.NS`).

## 🧪 How to Use
1. Make sure you have Python 3 installed.  
2. Install the required libraries:  
```bash
pip install yfinance pandas openpyxl
```  
3. Run the script:  
```bash
python WeightedPortfolioPlanner.py
```  
4. Input the following when prompted:  
   - Start date (e.g., `2023-01-01`)  
   - End date (e.g., `2023-12-31`)  
   - Total investment amount (e.g., `100000`)  
5. The program will generate `investment_plan.xlsx`, containing the number of shares to buy for each stock by date.

## 📦 Output
An Excel file that breaks down the share allocation by stock and trading day.

## 🔧 Dependencies
- `pandas`
- `yfinance`
- `openpyxl`

## 📄 License
Open source — feel free to use, modify, and contribute!
