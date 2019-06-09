import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GLib

class Cronometro(Gtk.Box):

    def __init__(self, minuti):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)

        self.__minuto = minuti
        self.__secondo = 0

        self.pack_start(self.contatore(self.__minuto, self.__secondo), True, False, 0)
        self.__timer = GLib.timeout_add(1000, self.timer)

    def contatore(self, minuto, secondo):
        self.__label = Gtk.Label(label='{:02d}'.format(minuto) + ':' + '{:02d}'.format(secondo))
        return self.__label
    
    def decrementa_minuto(self):
        self.__minuto -= 1
        self.print()
    
    def decrementa_secondo(self):
        self.__secondo -= 1
        self.print()
        
    def print(self):
        GLib.idle_add(
            self.__label.set_label, '{:02d}'.format(self.__minuto) + ':' + '{:02d}'.format(self.__secondo)
        )

    def timer(self):
        if 1 < self.__secondo < 60:
            self.decrementa_secondo()
            return True
        elif not self.__minuto == 0 and self.__secondo == 1:
            self.decrementa_secondo()
            return True
        elif self.__secondo == 0:
            self.__secondo = 59
            self.decrementa_minuto()
            return True
        elif self.__minuto == 0 and self.__secondo == 1:
            self.decrementa_secondo()
            self.destroy()
            return False
        else:
            return False

if __name__ == "__main__":
    
    win = Gtk.Window()
    win.connect('destroy', Gtk.main_quit)
    win.set_size_request(300, 200)

    timer = Cronometro(5)
    win.add(timer)
    win.show_all()
    
    Gtk.main()

