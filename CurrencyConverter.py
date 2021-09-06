'''
Python Program for Currency Convertion In any Format user wish
Program provides a request where you have to choose the Currency and Amount for Convertion 
and hence uses the latest dataset to work upon
'''

import requests
  
class RealTimeCurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']
  
    def convert(self, from_currency, to_currency, amount): 
        amount=x
        if from_currency != 'USD': 
            amount = amount / self.currencies[from_currency]

        amount = round(amount * self.currencies[to_currency], 2) 
        return amount
   
url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = RealTimeCurrencyConverter(url)
From=input("Enter From Currency: ")
To=input("Enter To Currency: ")
x=int(input("Enter How Much amount Do you want to convert: "))
result=converter.convert(From,To,x)
print('From {} {} to {} {} '.format(x,From,result,To))

