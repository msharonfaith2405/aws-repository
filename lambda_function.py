import json
import requests
import pandas as pd

def lambda_handler(event, context):
    
    print("Event Data ->", event)
    response = requests.get("https://www.google.com")
    print(response.text)
    
    d={'Names':['Sharon','Cherry'],'Ages':[23,22]}
    df=pd.DataFrame(data=d)
    print(df)
    print('Done x1.1')