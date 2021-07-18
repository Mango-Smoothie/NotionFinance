# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

import key
import yfinance as yf
from notion.client import NotionClient
from datetime import datetime

client = NotionClient(token_v2=key.api_key)

cv = client.get_collection_view(
    "https://www.notion.so/5ab23b8ffb5c4646a02fa0a213ee2133?v=c3cb2917568944fe8c0cf7ef61776cdf")

tickers = ['AAPL', 'SQ', 'AMD', 'KO', 'WMT']
for ticker in tickers:
    price = yf.Ticker(ticker)
    row = cv.collection.add_row()
    hist = price.history(period="1d")

    # information:
    row.Stock = ticker
    row.Date = datetime.today().strftime('%Y-%m-%d')
    row.Close = float(round((hist.Close[0]), 1))
    row.Open = float(round((hist.Open[0]), 1))
    row.Volume = float(round((hist.Volume[0]), 1))
    row.High = float(round((hist.High[0]), 1))
    row.DayReturn = float(round(((hist.Close[0]) - (hist.Open[0])) / (hist.Open[0]) * 100, 2))

print("The script has completed")
