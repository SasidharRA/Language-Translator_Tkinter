from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1100x320')
root.resizable(0,0)
root.iconbitmap('mini.ico')
root['bg']= 'thistle2'

root.title("Language Translator by Sasidhar R A")
Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold").pack()

Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
Input_text = Entry(root, width = 60)
Input_text.place(x=30,y = 100)
Input_text.get()

Label(root,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)
Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)

language = list(LANGUAGES.values())

dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=890,y=60)
dest_lang.set('choose output language')

def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'royal blue1', activebackground = 'sky blue')
trans_btn.place(x = 490, y= 180 )
root.mainloop()
