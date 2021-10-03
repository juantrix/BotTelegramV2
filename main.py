from ventana_ui import *
import telebot
videos = False
fotos = False
audios = False
apikey = ""

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow) :
    def __init__ ( self, *args, **kwargs ) :
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


    def obtenerApiKey( self ):

        return self.ApiKeyText.toPlainText()


    def ComprobarChecksBoxs ( self ) :

        if self.CheckVideos_2.isChecked() :

            videos = True
        else :
            Videos = False

        if self.CheckAudios.isChecked() :

            audios = True
        else :
            audios = False

        if self.CheckFotos.isChecked() :

            fotos = True

        else :
            fotos = False



if __name__ == "__main__" :
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


def iniciarBot():

    # obtenemos la api key , inicializamos el bot

    bot = telebot.TeleBot(window.obtenerApiKey(), parse_mode=None)

    #comprobamos que tipo de media queremos enviar

    window.ComprobarChecksBoxs()

    #enviamos el media

    #TODO


