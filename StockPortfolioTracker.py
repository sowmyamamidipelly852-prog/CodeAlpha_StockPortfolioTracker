#Stock_Portfolio_Tracker

import pandas as pd
#stock_prices Dictionary store stocknames and their prices
#stockname:price
stock_prices = {
    'RELIANCE': 1219.20,
    'HDFCBANK': 729.80,
    'BHARTIARTL': 1800.80,
    'ICICIBANK': 1336.10,
    'SBIN': 978.50,
    'TCS': 2073.60,
    'INFY': 1000.20,

    'AAPL': 255.00,
    'MSFT': 510.00,
    'GOOGL': 250.00,
    'NVDA': 180.00,
    'AMZN': 230.00,
    'META': 750.00,
    'TSLA': 450.00
}

#Displaying the available stocks and prices
print(stock_prices)

#no.of stocks the user bought
no_of_stocks=int(input("Enter no of stocks you buyed:"))


total_investment=0 #store total investment
stock_portfoilo=[]

for i in range(1,no_of_stocks+1):
    #ask the user to enter the stock name 
    stock_name=input(f"Enter Stock {i} name:").upper()
    #ask the user to enter the no.of shares
    quantity=int(input("Enter quantity:"))
    
    #checking whether the user stcok is available
    if stock_name in stock_prices:

        #get the price of user entered stock
        stock_price=stock_prices[stock_name]

        #calculate investement for each stock
        stock_investment=stock_price*quantity

        print("---------------------------------------------")
        print("total price of",stock_name,":",stock_investment)
        print("---------------------------------------------")

        stock_portfoilo.append([stock_name,stock_price,quantity,stock_investment])
        
        #add stock_investment to total_investment
        total_investment=total_investment+stock_investment

    else:
        #if stock not available
        print("Stock not found")
#Displaying the total_investment of user in all stocks
print("your total investemnt on stocks:",total_investment)


#creating the dataframe for stock_portofilo
df=pd.DataFrame(stock_portfoilo,columns=['stock_name','Price','Shares','Investment'])

#saving the results into .csv file using pandas 
df.to_csv("stock_portfoilo_tracker.CSV",index=False)

