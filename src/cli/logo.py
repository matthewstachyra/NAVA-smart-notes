from pyfiglet import Figlet

class Logo:
    def __init__(self):
        f = Figlet(font='rev')
        self.logo = f.renderText('NAVA') + '\n' +  'smart notes, organized for you by NAVA' + '\n' + 'v0.1.0' +'\n'

    def __str__(self):
        print(self.logo)


