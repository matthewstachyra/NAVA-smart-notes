from pyfiglet import Figlet

class Logo:
    def __init__(self):
        f = Figlet(font='slant')
        self.logo = f.renderText('NAVA') + 'smart notetaking.' + '\n' + '\n' +'\n'

    def __str__(self):
        print(self.logo)


