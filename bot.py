from os import system, listdir
import time
import telebot

with open('datos.txt', 'r') as f:
    datos = [line.strip() for line in f] #0: tiempo entre publicacion, 1: token del bot, 2: mensaje que sale debajo de la foto, 3: id del chat, 4: True si se quiere mantener las fotos enviadas(False borra)
    f.close()

bot = telebot.TeleBot(datos[1], parse_mode=None)
'''
bot.send_video(datos[3], open('./videos/'+carpetas[0][0], 'rb'))
bot.send_photo(datos[3], open('./fotos/'+carpetas[1][0], 'rb'))    
bot.send_audio(datos[3], open('./audios/'+carpetas[2][0], 'rb'))

'''
while True:
    videos = listdir('./videos')
    fotos = listdir('./fotos')
    audios = listdir('./audios')
    archivos = listdir('./archivos')
    carpetas = [archivos, videos, fotos, audios]

    for carpeta in carpetas:
        try:
            bot.send_video(datos[3], open('./videos/'+carpeta[0], 'rb'))
            if datos[4] == 'True':
                system(f'mv videos/{carpeta[0]} videos_enviados/{carpeta[0]}')
            else:
                system(f'rm videos/{carpeta[0]}')
        except:
            pass
        try:
            bot.send_photo(datos[3], open('./fotos/'+carpeta[0], 'rb'))    
            if datos[4] == 'True':
                system(f'mv fotos/{carpeta[0]} fotos_enviadas/{carpeta[0]}')
            else:
                system(f'rm fotos/{carpeta[0]}')   
        except:
            pass
        try:
            bot.send_audio(datos[3], open('./audios/'+carpeta[0], 'rb'))
            if datos[4] == 'True':
                system(f'mv audios/{carpeta[0]} audios_enviados/{carpeta[0]}')
            else:
                system(f'rm audios/{carpeta[0]}')
        except:
            pass
        try:
            bot.send_document(datos[3], open('./archivos/'+carpeta[0], 'rb'))
            if datos[4] == 'True':
                system(f'mv archivos/{carpeta[0]} archivos_enviados/{carpeta[0]}')
            else:
                system(f'rm archivos/{carpeta[0]}')
        except:
            pass
        time.sleep(int(datos[0])*60)