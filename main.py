from time import sleep

from ventana_ui import *
import telebot


apikey = ""
ChatID = ""

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




if __name__ == "__main__" :
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



