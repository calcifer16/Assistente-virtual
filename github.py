import webbrowser
import speech_recognition as sr
import pygame
import pyttsx3
import pyautogui
import subprocess
import time


def gerafala (texto):

    engine = pyttsx3.init()

    # Definir velocidade da fala (padrão é 200)
    engine.setProperty('rate', 150)

    # Definir volume (entre 0.0 e 1.0)
    engine.setProperty('volume', 0.9)

    # Escolher a voz (masculina ou feminina)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Mude para voices[1].id para uma voz diferente

    engine.say(texto)
    engine.runAndWait()


def captura_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Aguardando comando...')
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source)
            comando = recognizer.recognize_google(audio, language = 'pt-BR')
            print(f'voce disse {comando}')
            return comando.lower()
        except sr.UnknownValueError:
            print('Não entendi o que você disse')
            return ''
        except sr.RequestError:
            print('ERRO AO SE COMUNICAR COM O SERVIÇO DE RECONHECIMENTO DE FALA')
        return None

def comand():
    subprocess.Popen(['start', 'WhatsApp'], shell=True)

def hom():
    pyautogui.PAUSE = (2)
    process = subprocess.Popen(['start', 'chrome'], shell=True)
    time.sleep(3)
    pyautogui.click(x=938, y=571)
    pyautogui.write('https://animesdigital.org/anime/a/invdu006')
    pyautogui.press('enter')

def tv():
    pyautogui.PAUSE=(2)
    process = subprocess.Popen(['start', 'chrome'], shell = True)
    time.sleep(3)
    pyautogui.click(x=938, y=571)
    image =['fotos/pontos.png','fotos/salvar.png','fotos/trans.png','fotos/fonte.png', 'fotos/transmitirtela.png', 'fotos/Edu.png']
    try:
        for imagens in image:
            posicao = pyautogui.locateCenterOnScreen(imagens)
            if posicao:
                pyautogui.click(posicao.x, posicao.y)
            else:
                print('n')
    except pyautogui.ImageNotFoundException:
        print('posição não encontrada')

def fechar_google():
    pyautogui.click(x=1904, y=15)


def abrir_spotify():
    process = subprocess.Popen(['start', 'spotify'], shell=True)
    time.sleep(10)
    pyautogui.press('space')

def pausa():
    pyautogui.press('space')


palavra_chave = 'ativar'

def assistente_virtual():
    while True:
        comando = captura_voz()
        if comando:
            if palavra_chave in comando:
                gerafala('assistente ativado')
                while True:
                    comando = captura_voz()
                    if comando:
                        if 'abra o whatsapp' in comando:
                            resposta = 'okay!'
                            gerafala(resposta)
                            comand()

                        elif 'oi' in comando:
                            resposta = 'helo, why can i help you?'
                            gerafala(resposta)

                        elif 'quero assistir desenho' in comando:
                          resposta='sure, opening spiderman'
                          gerafala(resposta)
                          hom()


                        elif 'fechar o google' in comando:
                          resposta = 'sure'
                          gerafala(resposta)
                          fechar_google()

                        elif 'conecta na tv' in comando:
                          resposta = 'okay'
                          gerafala(resposta)
                          tv()

                        elif 'como você tá' in comando:
                          resposta = 'good and you?'
                          gerafala(resposta)

                        elif 'obrigado' in comando:
                          resposta = "you 're welcome"
                          gerafala(resposta)

                        elif 'abrir spotify' in comando:
                          resposta= 'opening spotify'
                          gerafala(resposta)
                          abrir_spotify()

                        elif 'pausar' in comando:
                            pausa()

                        elif 'pesquise' in comando:
                            pergunta = comando.split('pesquise', 1)[1].strip()
                            if pergunta:
                                resposta = f'searching {pergunta}'
                                gerafala(resposta)
                                webbrowser.open(f"https://www.google.com/search?q={pergunta}")

                        elif 'tchau' in comando:
                          resposta = 'see you later'
                          gerafala(resposta)
                          break

                        else:
                            resposta = "sorry, I didn't understand"
                            gerafala(resposta)
assistente_virtual()