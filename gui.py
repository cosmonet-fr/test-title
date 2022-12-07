import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import functions as function
#import gui_functions as gui_function

def runTest(button_1):
    print("File selected: %s" % csvUploadButton.get_filename())
    if (titleCheck.get_active() == True):
        function.title()
    if (metaCheck.get_active() == True):
        function.meta()
        
def fileChanged(csvUploadButton):
    #print("File selected: %s" % csvUploadButton.get_filename())
    #grid.attach(button_1, 0, 7, 6, 1)
    #button_1.connect('clicked', runTest)
    function.meta(csvUploadButton.get_filename())

mainWindow = Gtk.Window()
mainWindow.set_border_width(25)
mainWindow.set_title('Balise Test')
mainWindow.connect('delete-event', Gtk.main_quit)

grid = Gtk.Grid()
mainLabel = Gtk.Label()
mainLabel.set_markup('<span weight="bold" font="roboto">Sélectionnez les tests à effectuer : </span>')
titleCheck = Gtk.Switch()
titleLabel = Gtk.Label('Tester les balises <title> ')
titleLabel.set_justify(Gtk.Justification.LEFT) # Ce truc ne fonctionne pas !!!
titleCheck.set_active(True)
metaCheck = Gtk.Switch()
metaLabel = Gtk.Label('Tester les metas descriptions')
csvUploadButton = Gtk.FileChooserButton(title="Fichier CSV")
csvUploadButton.set_current_folder('/')
csvUploadButton.connect("file-set", fileChanged)
#print(dir(csvUploadButton.props))
button_1 = Gtk.Button(label='Valider !', relief="none")
button_1.set_relief(0)

grid.attach(mainLabel, 0,0,6,1)
grid.attach(titleCheck, 6,1,1,1)
grid.attach(titleLabel, 0,1,1,1)
grid.attach(metaCheck, 6,2,1,1)
grid.attach(metaLabel, 0,2,1,1)
grid.attach(csvUploadButton, 0, 6, 6, 1)

grid.set_row_spacing(8)

mainWindow.add(grid)
mainWindow.show_all()
Gtk.main()