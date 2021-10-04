from time import sleep
from os import listdir, system
from PyQt5.sip import delete

from telebot.types import Message
from ventana_ui import *
import telebot


apikey = ""
ChatID = ""
timePost = 15 # minutos
message_text = 'test' # mensaje debajo de cada publicacion
delete_media = False # si se va a borrar los archivos al enviarlo o se van a guardar

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow) :
    fotos = False
    audios = False
    videos = False
    stopButton = False

    def __init__ ( self, *args, **kwargs ) :
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.StartButton.clicked.connect(self.iniciarBot)
        self.stopButton.clicked.connect(self.ApagarBot)

    def ApagarBot (self):

        self.stopButton = False


    def obtenerChatID( self ):

        return self.ChatID.toPlainText()


    def obtenerApiKey( self ):

        return self.ApiKeyText.toPlainText()


    def ComprobarChecksBoxs ( self ) :

        if self.CheckVideos_2.isChecked() :

            self.videos = True

        else :
            self.videos = False

        if self.CheckAudios.isChecked() :

            self.audios = True
        else :
            self.audios = False

        if self.CheckFotos.isChecked() :

            self.fotos = True

        else :
            self.fotos = False

    def iniciarBot (self) :

        self.stopButton = True

        # obtenemos la api key , inicializamos el bot

        bot = telebot.TeleBot(self.obtenerApiKey(), parse_mode=None)

        # comprobamos que tipo de media queremos enviar

        window.ComprobarChecksBoxs()

        # enviamos el media

        while not self.stopButton:

            fotos_list = listdir('./fotos')
            videos_list = listdir('./fotos')
            audios_list = listdir('./audios')

            if self.fotos and len(fotos_list) > 0:
                bot.send_photo(chat_id=ChatID, photo=open('./fotos/'+fotos_list[0], 'rb'), caption=message_text)
                
                if delete_media:
                    system(f'rm fotos/{fotos_list[0]}')
                else:
                    system(f'mv fotos/{fotos_list[0]} fotos_enviadas/{fotos_list[0]}')

            if self.videos and len(videos_list) > 0:
                bot.send_video(chat_id=ChatID, video=open('./videos/'+videos_list[0], 'rb'), caption=message_text)
                
                if delete_media:
                    system(f'rm videos/{videos_list[0]}')
                else:
                    system(f'mv videos/{videos_list[0]} videos_enviados/{videos_list[0]}')

            if self.audios and len(audios_list) > 0:
                bot.send_photo(chat_id=ChatID, audio=open('./fotos/'+fotos_list[0], 'rb'), caption=message_text)
                
                if delete_media:
                    system(f'rm audios/{audios_list[0]}')
                else:
                    system(f'mv audios/{audios_list[0]} audios_enviados/{audios_list[0]}')

            sleep(timePost * 60)



if __name__ == "__main__" :
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



