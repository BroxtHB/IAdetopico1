
import pyttsx3
import speech_recognition as sr
import pandas as pd
import pywhatkit
import datetime
import re

import numpy as np
import sympy as cas

datos = pd.read_excel('pruebita.xlsx')
df=pd.DataFrame(datos)

name = 'alexa'

listener = sr.Recognizer()

engine = pyttsx3.init()

#tipos de voces
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
 

def talk(text):
    engine.say(text)
    engine.runAndWait()
    


#lo que va a decir la computadora
engine.say("Hola, me llamo alexa, que puedo hacer por ti ")
engine.runAndWait()


def listen(): 
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
           #lower es para poner todo minusculas
            rec = rec.lower()
            #para que busque la palabra en la oracion que le estas diciendo
            if name in rec:
                #para que no diga una palabra en este caso es el nombre 
                rec = rec.replace(name,'')
                #para imprimir lo que diga 
                #print (rec)
    except:
        pass
    return rec


#si encontro la palabra reproduce en el audio entonces excribe reproduce y lo dice
def run():
    rec = listen()
    if 'nombre'  in rec:
        print('Reproduciendo...')
        if 'oscar' in rec:
            talk('su nombre completo es oscar octavio rodriguez villegas')
        if 'octavio' in rec:
            talk('el nombre completo de octavio es Oscar Octavio Rodriguez villegas')


    elif 'ora' in rec:
        hora = datetime.datetime.now().strftime('%H:%M')
        talk("son las " + hora)
    print (rec)
        
run()