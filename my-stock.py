import yfinance as yf

# S&P500 is "^GSPC"
# Dow Jones is "^DJI"
# NASDAQ Composite is "^IXIC"
#  S&P/TSX Composite index is "^GSPTSE"


# data = yf.download("SPY AAPL", start="2008-01-01", end="2023-05-22")
# data.to_csv("data/SPY_AAPL.csv")

data = yf.download("^GSPTSE ENGH.TO RY.TO TD.TO CNR.TO ENB.TO CP.TO SHOP.TO CNQ.TO BMO.TO BNS.TO", start="2008-01-01", end="2023-05-22")
data.to_csv("data/S&P_TSX.csv")
data.to_excel("data/S&P_TSX.xlsx")


data2 = yf.download("^IXIC RY TD ENB CP SHOP CNQ BMO BNS TRI BN", start="2008-01-01", end="2023-05-22")
data2.to_csv("data/NASDAQ_CanadaCom.csv")
data2.to_excel("data/NASDAQ_CanadaCom.xlsx")
