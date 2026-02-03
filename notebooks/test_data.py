import yfinance as yf
import pandas as pd

# Test pulling SPY data
print("Testing data pull...")
spy = yf.download('SPY', start='2020-01-01', end='2024-01-01')
print(f"\nSPY data shape: {spy.shape}")
print(f"\nFirst few rows:")
print(spy.head())
print(f"\nLast few rows:")
print(spy.tail())