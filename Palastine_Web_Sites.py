import tkinter
import tkinter as tk
r= tk.Tk()
r.title("City of Palastine")
r.geometry("500x500+300+100")
r.configure(background="black")
yazi=tkinter.Label(
    text="أحب فلسطين كثيراً.",
    fg="red",
    bg="black",
    width=20,
    height=3,
    font="Algerian"
)
yazi.pack()
def listeye_tikla(event):
    secilen = liste.get(liste.curselection())
    if secilen == "Ramallah":
        sonuc_label.config(text="Ramallah is located in the West Bank region\n of Palestine and is 10 km from Jerusalem.\n\
Government buildings in \nPalestine are located in this city.",fg="green",bg="black",font="Tahoma")
    elif secilen == "Gazze":
        sonuc_label.config(text="Gaza city is located on the Mediterranean\n coast and neighbors Egypt.\n\
Unfortunately, this city remained\n under the blockade of terrorists.",fg="green",bg="black",font="Tahoma")
    elif secilen == "El-Halil":
        sonuc_label.config(text="The city of Hebron, 30 km away from Jerusalem,\n\
is very beautiful from a spiritual perspective.\n\
However, peaceful life in this city becomes\n\
difficult because of Zionist terrorists.",fg="green",bg="black",font="Tahoma")
    elif secilen == "Beytullahim":
        sonuc_label.config(text="Bethlehem is a Palestinian city\n 10 km from Jerusalem.\n\
Unfortunately, full control cannot be \nachieved because of the invaders.",fg="green",bg="black",font="Tahoma")
    elif secilen == "Yafa":
        sonuc_label.config(text="Unfortunately, Jaffa was occupied by the Zionists.\n\
The distance between Jaffa and Jerusalem\n is approximately 70 kilometers.\n\
Jaffa must become Palestine again.",fg="green",bg="black",font="Tahoma")
    elif secilen == "Kudüs":
        sonuc_label.config(text="Jerusalem is a very important\n city because many prophets lived here.\n Also,\
Masjid al-Aqsa\n is located in Jerusalem. \nUnfortunately,\
this beautiful city,\n which should belong to Palestine,\n is under occupation.",fg="green",bg="black",font="Tahoma")
liste=tk.Listbox(r)
liste.pack()
liste.insert(tk.END,"Ramallah")
liste.insert(tk.END,"Gazze")
liste.insert(tk.END,"El-Halil")
liste.insert(tk.END,"Beytullahim")
liste.insert(tk.END,"Yafa")
liste.insert(tk.END,"Kudüs")
sonuc_label = tk.Label(r, text="",fg="green",bg="red",font="Algerian")
sonuc_label.pack()
liste.bind("<ButtonRelease-1>", listeye_tikla)
r.mainloop()
###LOVE PALASTİNE###
