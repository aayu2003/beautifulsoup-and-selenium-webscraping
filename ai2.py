
import requests
from bs4 import BeautifulSoup

url = "https://smallpdf.com/word-to-pdf#r=convert-to-word"  
l={'submit':None,'output':None,'input':None}
inp=[]
sub=[]

def submits(input_tag):
    if "onclick" in str(input_tag):
        try:
            return(["onclick","value",input_tag.get("value")])
        except:
            return(["onclick","id",input_tag.get("id")])
    elif "onkeyup" in str(input_tag):
        try:
            return(["onkeyup","id",input_tag.get("id")])
        except:
            return(["onkeyup","value",input_tag.get("value")])
    elif input_tag.get('type')=='submit':
        try:
            return(["submit","value",input_tag.get("value")])
        except:
            return(["submit","id",input_tag.get("id")])
    elif input_tag.get('type')=='button':
        
        try:
            try:
                return(["button","class",input_tag('class')])
            except:
                return(["button","id",input_tag.get("id")])
        except:
            return(["button","value",input_tag.get("value")])

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    input_tags = soup.find_all('input')
    for input_tag in input_tags:
        if input_tag.get('type')=="text":
            try:
                inp.append({"name":input_tag.get('name')})
            except:
                inp.append({"id":input_tag.get('id')})
        elif input_tag.get('type')=="file":
            inp.append({"id":input_tag.get("id")})
            button_tags = soup.find_all('button')
            for button in button_tags:
                button_class = button.get(sub.append(["button","class",button.get('class')]))
        else:
            sub.append(submits(input_tag))
    l['submit']=sub
    l['input']=inp
except:
    print("something went wrong")
print(l)

