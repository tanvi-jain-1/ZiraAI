import speech_recognition as sr
import os
import openai
import requests
import win32com.client
import webbrowser
import datetime
import openai
from config import apikey
from requests import get

chatStr = ""

# def chat(query):
#     global chatStr
#     print(chatStr)
#     openai.api_key = apikey
#     chatStr += f"Tanvi: {query}\n Zira: "
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt= chatStr,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     # todo: Wrap this inside of a  try catch block
#     speaker.Speak(response["choices"][0]["text"])
#     chatStr += f"{response['choices'][0]['text']}\n"
#     return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    #Creates a folder named Openai and then inside that folder will create a txt file which will save response to our prompt
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def news():
    main_url = 'url + api'

    main_page = requests.get(main_url).json()

    articles = main_page["articles"]

    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):

        speaker.Speak(f"today's{day[i]} news is: {head[i]}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        #can set threshold accordingly
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Zira"


speaker=win32com.client.Dispatch("SAPI.SpVoice")
#
# while 1:
#     print("Enter the word you want to speak it out from computer")
#     s=input()
#     speaker.Speak(s)

if __name__ == '__main__':
    speaker.Speak('Hello How can I assist you today?')

    while True:
        print("Listening...")
        query = takeCommand().lower()
        speaker.Speak(query)
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ["geeksforgeeks", "https://www.geeksforgeeks.org/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} ...")
                webbrowser.open(site[1])

            if "play music" in query.lower():
                musicPath = "C:/Users/hp/Downloads/FavSong.mp3"
                speaker.Speak(f"Playing Music...")
                os.startfile(musicPath)

            elif "what's the time" in query:
                musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                speaker.Speak(f"Ma'am time is {hour}  {min} minutes")

            elif "Using artificial intelligence".lower() in query.lower():
                ai(prompt=query)

            elif "Goodbye".lower() in query.lower():
                speaker.Speak(f"Goodbye! If you have any more questions or need assistance in the future, feel free to ask. Take care!")
                exit()

            elif "tell me news" in query:
                speaker.Speak("Please wait ,fetching the latest news")
                news()

            elif "reset chat".lower() in query.lower():
                chatStr = ""

            # else:
            #     print("Chatting...")
            #     chat(query)