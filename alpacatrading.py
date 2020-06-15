#https://paper-api.alpaca.markets
# API key PKF507U7QP4OCBGHDB8H
# secret key I85/O6C7auYd9ClS9XdFJCvIWdtJYHoLolWjDJs1
import requests
import alpaca_trade_api as tradeapi
import smtplib

#setting Environment Variables
API_KEY= "PKF507U7QP4OCBGHDB8H"
API_SECRET = "I85/O6C7auYd9ClS9XdFJCvIWdtJYHoLolWjDJs1"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets";

#Get market values
DATA_BASE_URL = "https://data.alpaca.markets/v1"
CURRENT_PRICE_URL = "/last_quote/stocks/"

#Local ENV values
BUY_AMD_THRESHOLD = 54
SELL_AMD_THRESHOLD = 57
AMD = "AMD"
ALLSTOCKLIST = ['AMD', 'SDC', 'AAL']
ENV = "testing "

#instantiate API
api = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, api_version='v2', ) 

account = api.get_account()
print(account)
api.list_positions() #shows current positions

print('******************')
pricereq = requests.get(DATA_BASE_URL + CURRENT_PRICE_URL + 'AMD', headers={'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': API_SECRET});

currenttest = pricereq.json()
inner_dict = currenttest['last']
STOCKABSCURRENTPRICE = inner_dict['askprice']
#STOCKABSCURRENTPRICE = 55  *********test here**********

print("Price of AMD is: " + str(STOCKABSCURRENTPRICE))
print('******************')

def sendemail(price, symbol, tradetype):    
    gmail_user = 'tradingacc341@gmail.com'
    gmail_password = 'zztonmfgfsjokjoe'
    sent_from = gmail_user
    to = ['ypatel341@gmail.com']
    subject = ENV + tradetype
    body = "the Stock: " + symbol + " is " + tradetype + str(BUY_AMD_THRESHOLD) + " and is currently traded at " + str(price)
    
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (sent_from, ", ".join(to), subject, body)
    
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, message)
        server.close()
        print ("email sent")

    except Exception as e: print(e)
    return

#print(inner_dict['askprice'])
if STOCKABSCURRENTPRICE < BUY_AMD_THRESHOLD:
  print("will be buying")
  #sendemail(STOCKABSCURRENTPRICE, AMD, "BELOW ")
elif STOCKABSCURRENTPRICE > SELL_AMD_THRESHOLD:
  print("will be selling")
  #sendemail(STOCKABSCURRENTPRICE, AMD, "ABOVE ")
else: 
  print(AMD + " is trading between threshold " + "BUY " + str(BUY_AMD_THRESHOLD) + " SELL " + str(SELL_AMD_THRESHOLD))

#print(currenttest) since its json, in python you will need to write a forloop and grab by ID

#print(api.get_asset("AMD")); #Only gets asset information

#doing without client
#r = requests.get(APCA_API_BASE_URL + "/v2/account", headers={'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': API_SECRET});

#print(r.content)

#aapl = api.alpha_vantage.historic_quotes('AAPL', adjusted=True, output_format='pandas')
#amd = api.alpha_vantage.current_quote('AMD');
#print(amd);
#print(amd.price)

#print(pricereq.content)
#currentprice = pricereq.content.decode() #returns back as str
#print(str(currentprice['last']))


______________________________________________________________________________________________________________________________________

#https://paper-api.alpaca.markets
# API key PKF507U7QP4OCBGHDB8H
# secret key I85/O6C7auYd9ClS9XdFJCvIWdtJYHoLolWjDJs1
import requests
import alpaca_trade_api as tradeapi
import smtplib

#Alpaca Environment Variables
API_KEY= "PKSZ8APR5HNXR3GD4R89"
API_SECRET = "tGN4PmAxVkus5DtPF5leIs0r5df0l0JTxV7RE0Ec"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets";
ORDERS_URL = "/v2/orders"

#Get market values
DATA_BASE_URL = "https://data.alpaca.markets/v1"
CURRENT_PRICE_URL = "/last_quote/stocks/"

#Local ENV values
BUY_AMD_THRESHOLD = 54
SELL_AMD_THRESHOLD = 57
#AMD = "AMD"
ALLSTOCKLIST = ['AMD', 'SDC', 'AAL']
ENV = "testing "

#instantiate API
api = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, api_version='v2', ) 

def sendemail(price, symbol, tradetype):    
    gmail_user = 'tradingacc341@gmail.com'
    gmail_password = 'zztonmfgfsjokjoe'
    sent_from = gmail_user
    to = ['ypatel341@gmail.com']
    subject = ENV + tradetype
    body = "the Stock: " + symbol + " is " + tradetype + str(BUY_AMD_THRESHOLD) + " and is currently traded at " + str(price)
    
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (sent_from, ", ".join(to), subject, body)
    
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, message)
        server.close()
        print ("email sent")

    except Exception as e: print(e)
    return

def TRANSACT(shareamt, transtype, symbol, limitprice):
  #shareamt is an int
  #https://alpaca.markets/docs/trading-on-alpaca/orders/#time-in-force
  ordersreq = requests.post(APCA_API_BASE_URL + ORDERS_URL, 
  data = {'symbol': symbol,
          'side': transtype,
          'type': 'market',
          'qty': shareamt,
          'time_in_force': 'day',
          'limit_price': limitprice},
  headers={'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': API_SECRET},
  );
  print(ordersreq.raise_for_status())
  '''
  listallorders = requests.get(APCA_API_BASE_URL + ORDERS_URL, headers={'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': API_SECRET})
  print(listallorders.json())
  '''

def ACCOUNTCHECK(currentprice):
  account = api.get_account()
  #print("buyingpower " + account.buying_power)
  #print("cash " + account.cash)
  buyammount = (int(account.cash)/currentprice)/10
  print(buyammount)
  print("able to buy AMD stock number = " + str(int(buyammount)))

  getallpositions = api.list_positions()
  if not getallpositions:
    print("proceeding to buy")
    print("**************************************************")
    TRANSACT(int(buyammount), "buy", "AMD", currentprice)
  else:
    print("not buying, open positions")
  print("*")

  
def PRICECHECK(): #consider inserting symbol variable for a forloop
  pricereq = requests.get(DATA_BASE_URL + CURRENT_PRICE_URL + "AMD", headers={'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': API_SECRET});
  currentprice = pricereq.json()['last']['askprice']

  print("price of AMD is " + str(currentprice))
  print("**************************************************")
  if currentprice < BUY_AMD_THRESHOLD:
    print("will be buying")
    print("**************************************************")
    #sendemail(STOCKABSCURRENTPRICE, AMD, "FLAG: BELOW")
    ACCOUNTCHECK(currentprice)

  elif currentprice > SELL_AMD_THRESHOLD:
    print("will be selling")
    print("***************")
    #sendemail(STOCKABSCURRENTPRICE, AMD, "FLAG: ABOVE")
    
  else: 
    print(SYMBOL + " is trading between threshold " + "BUY " + str(BUY_AMD_THRESHOLD) + " SELL " + str(SELL_AMD_THRESHOLD))

PRICECHECK()










'''
def thresholdcalculator(SYMBOL, CURRENT, BUY, SELL):
  if CURRENT < BUY:
    print("will be buying")
    #sendemail(STOCKABSCURRENTPRICE, AMD, "BELOW ")
  elif CURRENT > SELL:
    print("will be selling")
    #sendemail(STOCKABSCURRENTPRICE, AMD, "ABOVE ")
  else: 
    print(SYMBOL + " is trading between threshold " + "BUY " + str(BUY) + " SELL " + str(SELL))
'''
#print(api.get_account())

#print("able to buy AMD stock number = " + str(round(buyammount))) ROUNDS to CLOSEST

#api.list_positions() #shows current positions

#print(currenttest) since its json, in python you will need to write a forloop and grab by ID

#print(api.get_asset("AMD")); #Only gets asset information

#doing without client
#r = requests.get(APCA_API_BASE_URL + "/v2/account", headers={'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': API_SECRET});

#print(r.content)

#aapl = api.alpha_vantage.historic_quotes('AAPL', adjusted=True, output_format='pandas')
#amd = api.alpha_vantage.current_quote('AMD');
#print(amd);
#print(amd.price)

#print(pricereq.content)
#currentprice = pricereq.content.decode() #returns back as str
#print(str(currentprice['last']))