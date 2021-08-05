
from tkinter import Tk   
from tkinter.filedialog import askopenfilename
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


#This Section is for Functions that I will use in my Program 

# This Function will allow the user to Choose a Text file and convert it to audio File
def TxtFileFromDevice() :
    url ="https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/0580a91d-2c01-467e-9362-908b12e35208"
    apikey= "EO1gQcYfO8xEIhSWbPDTS27BQ-XYNDzo4_mUs-lF87xT"
    

    authenticator = IAMAuthenticator(apikey)
    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url(url)
    
    
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    
    with open(filename, 'r') as f:
        text = f.readlines()

    text = [line.replace('\n','') for line in text]
    text = ''.join(str(line) for line in text)
    with open('./Output.mp3', 'wb') as audio_file:
        res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
        audio_file.write(res.content)



# This Function will allow the user to Write a Text and convert it to audio File

def TxtToSpeech(Txt) :
    url ="https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/0580a91d-2c01-467e-9362-908b12e35208"
    apikey= "EO1gQcYfO8xEIhSWbPDTS27BQ-XYNDzo4_mUs-lF87xT"

    authenticator =IAMAuthenticator(apikey)
    tts= TextToSpeechV1(authenticator = authenticator)
    tts.set_service_url(url)
    with open('./speech.mp3', 'wb') as audio_file:
        res = tts.synthesize(Txt, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
        audio_file.write(res.content)

#
# This Function will allow the user to Choose a audio file and convert it to Text File

def AudioFromDevice():
    apikey = 'nzN8WFtC9g2RwkMZzu23sizbHl_VHyqX9UxqSz_nUUhV'
    url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/51f9a737-c3ef-47b8-8d33-4ffa6a5b783b'

    authenticator = IAMAuthenticator(apikey)
    stt = SpeechToTextV1(authenticator=authenticator)
    stt.set_service_url(url)

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    

    with open(filename, 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()
    text = res['results'][0]['alternatives'][0]['transcript']
    with open('output.txt', 'w') as out:
        out.writelines(text)
