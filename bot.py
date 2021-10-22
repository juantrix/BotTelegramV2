from os import system, listdir
import time
import telebot

with open('datos.txt', 'r') as f:
    datos = [line.strip() for line in f] #0: tiempo entre publicacion, 1: token del bot, 2: mensaje que sale debajo de la foto, 3: id del chat, 4: True si se quiere mantener las fotos enviadas(False borra)
    f.close()                            # cantidad de repeticiones 5:videos, 6:fotos, 7:audios, 8:archivos 

bot = telebot.TeleBot(datos[1], parse_mode=None)

repeticiones = [int(datos[5]), int(datos[6]), int(datos[7]), int(datos[8])]

carpeta_or = ['videos', 'fotos', 'audios', 'archivos']


while True:
    videos = listdir('./videos')
    fotos = listdir('./fotos')
    audios = listdir('./audios')
    archivos = listdir('./archivos')
    carpetas = [videos, fotos, audios, archivos]
    
    for carpeta, rep, carp in zip(carpetas, repeticiones, carpeta_or):
        for i in range(rep):

            try:
                if carp == 'videos':
                    bot.send_video(datos[3], open(f'./{carp}/'+carpeta[i], 'rb'), caption=datos[2])
                    print(carp)

                elif carp == 'fotos':
                    bot.send_photo(datos[3], open(f'./{carp}/'+carpeta[i], 'rb'), caption=datos[2])
                    print(carp)

                elif carp == 'audios':
                    bot.send_audio(datos[3], open(f'./{carp}/'+carpeta[i], 'rb'), caption=datos[2])
                    print(carp)
                
                elif carp == 'archivos':
                    bot.send_document(datos[3], open(f'./{carp}/'+carpeta[i], 'rb'), caption=datos[2])
                    print(carp)

                if datos[4] == 'True':
                    system(f'mv {carp}/{carpeta[i]} {carp}_enviados/{carpeta[i]}')
                else:
                    system(f'rm {carp}/{carpeta[i]}')

            except:
                pass

            time.sleep(int(datos[0])*60)
            