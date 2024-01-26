import requests
from bs4 import BeautifulSoup
url = "https://smallpdf.com/word-to-pdf#r=convert-to-word"  
l={'submit':None,'output':None,'input':None}
inp=[]
sub=[]
try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    input_tags = soup.find_all('input')
    for input_tag in input_tags:
     
        #print(f"Name: {input_tag.get('name')}, Type: {input_tag.get('type')}, Value: {input_tag.get('value')}")
        if input_tag.get('type')=="hidden":
            l['submit']={'name':input_tag.get('id')}
        elif input_tag.get('type')=='text':
            inp.append(input_tag.get('id'))
        elif "onclick" in str(input_tag):
            try:
                l['submit']={'name':input_tag.get('value')} 
                l['submit']={'name':input_tag.get('id')}
            except:
                print("there is a button but no id and value")
    l['input']=inp
    

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

print(l)
