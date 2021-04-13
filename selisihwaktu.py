

from tkinter import *

class DemoSelisihWaktu:
    def __init__(self, parent, title):
        self.parent = parent

        #self.parent.geometry("300x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.tutupWindow)
        self.parent.resizable(False, False)

        self.aturKomponen()

        self.entWaktu1.focus_set()

    def aturKomponen(self):
        # set mainFrame
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # set input waktu 1
        Label(mainFrame, text="Waktu 1 (hh:mm): ").grid(row=0, column=0, sticky=W)
        self.entWaktu1 = Entry(mainFrame, width=5)
        self.entWaktu1.grid(row=0, column=1)

        # set input waktu 2
        Label(mainFrame, text="Waktu 2 (hh:mm): ").grid(row=1,column=0, sticky=W)
        self.entWaktu2 = Entry(mainFrame, width=5)
        self.entWaktu2.grid(row=1, column=1)

        # set output selisih
        Label(mainFrame, text="Selisih Waktu: ").grid(row=2,column=0, sticky=W)
        self.entSelisih = Entry(mainFrame)
        self.entSelisih.grid(row=2, column=1)

        # set tombol Hapus dan Selisih
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.hapus)
        self.btnHapus.grid(row=3, column=0)
        self.btnSelisih = Button(mainFrame, text='Selisih', command=self.selisih)
        self.btnSelisih.grid(row=3, column=1)

    def hapus(self, event=None):
        self.entWaktu1.delete(0, END)
        self.entWaktu2.delete(0, END)
        self.entSelisih.delete(0, END)

        self.entWaktu1.focus_set()

    def selisih(self, event=None):
        jam1, menit1 = self.entWaktu1.get().split(':')
        jam2, menit2 = self.entWaktu2.get().split(':')

        waktu1 = int(menit1) + 60*int(jam1)
        waktu2 = int(menit2) + 60*int(jam2)

        delta = waktu2 - waktu1

        strSelisih = "%i jam %i menit" %(delta//60, delta%60)
        self.entSelisih.delete(0, END)
        self.entSelisih.insert(END, strSelisih)
        self.entSelisih.focus_set()

    def tutupWindow(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()

    aplikasi = DemoSelisihWaktu(root, ":: Demo Selisih Waktu ::")

    root.mainloop()
