from requests import get
import json

def get_bit_data(data_request:str)-> dict:
    '''
    Input:
    data_request = http request. Example: 'https://api.coindesk.com/v1/bpi/historical/close.json'
    
    Output:
    Dictionary containing bit coin data. Key: date, Value: "bitcoin average price for that day"
    '''
    
    # Submit the request and save the response
    response = get(data_request)
    
    # Verify the request was submitted correctly, otherwise output the error code
    if response.status_code != 200:
        print(response.status_code)
    else:
        data = json.loads(response.text)
        return data['bpi']