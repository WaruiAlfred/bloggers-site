import urllib.request,json
from .models import Quotes

def get_quotes(): 
  '''Function that gets the quote response data'''
  quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'
  
  with urllib.request.urlopen(quotes_url) as url: 
    quotes_data = url.read()
    quotes_url_response = json.loads(quotes_data)
    
    if quotes_url_response: 
      author = quotes_url_response['author']
      quote = quotes_url_response['quote']
      
      quotes_object = Quotes(author,quote)
  return quotes_object