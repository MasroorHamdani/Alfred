import sys, os, keyboard
import speech_recognition as sr
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '47da946ec0f441728422eb1a61d2ff20'

ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

request = ai.text_request()

request.lang = 'de'  # optional, default value equal 'en'

request.session_id = "abcde"

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print "you said: " + text
    request.query = text
    response = request.getresponse()
    print(response.read());
    os.system('wmctrl -a gedit')
    print(type(str(text)))
    keyboard.write(str(text))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
