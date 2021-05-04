from datetime import date
today =date.today()

d1=today.strftime("%B %d,%y")

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)
if __name__ == '__main__':
    import requests
    import json
    date1 = "news of " + d1 + "is"
    speak(date1)
    url = ('https://newsapi.org/v2/top-headlines?'
           'sources=bbc-sport&'
           'apiKey=f20c9f7913814733a8fec57accbfd741')

    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(0, 11):
        speak(my_json['articles'][i]['title'])