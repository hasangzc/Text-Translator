import googletrans
from tkinter import *
from trytrans import trans
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob

root = Tk()
root.geometry('500x500')
root.title("Translator")
root.resizable(False, False)
root.configure(bg="gray")


def tt():
    try:
        word = TextBlob(variable_name1.get())  # TextBlob is a Python (2 and 3) library for processing textual data.
        # It provides a simple API for diving into common natural language processing (NLP)
        # tasks such as part-of-speech tagging, noun phrase extraction,
        # sentiment analysis, classification, translation, and more
        lan = word.detect_language()  # detect
        lan_to_dict = languages.get()
        lan_to = lang_dict[lan_to_dict]
        word = word.translate(from_lang=lan, to=lan_to)
        variable_name2.set(word)
        label3.configure(text=word)

    except:
        variable_name2.set("Try another keyword!")

def main_exit():
    ex = messagebox.askyesnocancel("Notification", "Are you want to exit?", parent=root)
    if (ex==True):
        root.destroy()


# -----------------------------------------------------------------------------------------------------------------------------------------------------

# Binding functions


def enter_entry1(e):
    entry1["bg"] = "springgreen"


def leave_entry1(e):
    entry1["bg"] = "white"


def enter_entry2(e):
    entry2["bg"] = "springgreen"


def leave_entry2(e):
    entry2["bg"] = "white"


# -----------------------------------------------------------------------------------------------------------------------------------------------------


trans()
lang_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}


# ------------------------------------------------------------------------------------------------------------------------------------

# (Combobox) Combobox is a combination of Listbox and an entry field. It is one of the Tkinter widgets where it contains
# down arrow to select from a list of options. It helps the users to select according to the list of options displayed.
# When the user clicks on the drop-down arrow on the entry field,
# a pop up of the scrolled Listbox is displayed down the entry field.
# The selected option will be displayed in the entry field only when an option from the Listbox is selected.
languages = StringVar()
box = Combobox(root, width=20, textvariable=languages, state="readonly")
box["value"] = [i for i in lang_dict.keys()]
box.current(95)
box.place(x=300, y=0)

# ------------------------------------------------------------------------------------------------------------------------------------

# (Entry Box) The Entry widget
# is used to accept single-line text strings from a user.
variable_name1 = StringVar()  # StringVar() is a class from tkinter.
# It's used so that you can easily monitor changes to tkinter variables if they occur through the example code provided
entry1 = Entry(root, width=30, textvariable=variable_name1, font=("times", 15, "italic bold"))
entry1.place(x=120, y=40)

variable_name2 = StringVar()
entry2 = Entry(root, width=30, textvariable=variable_name2, font=("times", 15, "italic bold"))
entry2.place(x=120, y=80)

# ------------------------------------------------------------------------------------------------------------------------------------

# (Labels) If you want to display one or more lines of text that cannot
# be modified by the user, then you should use the Label widget.
label1 = Label(root, text="Enter Word: ", font=("times", 15, "italic bold"),  bg="gray")
label1.place(x=5, y=45)

label2 = Label(root, text="Translated: ", font=("times", 15, "italic bold"), bg="gray")
label2.place(x=5, y=85)

label3 = Label(root, text="", font=("times", 15, "italic bold"), bg="gray")
label3.place(x=10, y=250)

# ------------------------------------------------------------------------------------------------------------------------------------

# (Buttons)
btn1 = Button(root, text="Click", bg="red", bd=3, activebackground="yellow",  width=10, font=("times", 15, "italic bold"), command=tt)
btn1.place(x=180, y=150)

btn2 = Button(root, text="Exit", bg="red", bd=3, activebackground="yellow",  width=10, font=("times", 15, "italic bold"), command=main_exit)
btn2.place(x=180, y=200)
root.bind("<Return>", tt)   # <Return> The user pressed the Enter key. You can bind to virtually all keys on the keyboard:
                            # The special keys are Cancel (the Break key), BackSpace, Tab, Return(the Enter key),
                            # Shift_L (any Shift key), Control_L (any Control key), Alt_L (any Alt key), Pause, Caps_Lock, Escape,
                            # Prior (Page Up), Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert,
                            # Delete, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, and Scroll_Lock.


# ------------------------------------------------------------------------------------------------------------------------------------

# (Binding) We can bind Python’s Functions and methods to an event
#  as well as we can bind these functions to any particular widget.

entry1.bind("<Enter>", enter_entry1)  # <Enter> 	The mouse pointer entered the widget.
entry2.bind("<Enter>", enter_entry2)

root.mainloop()
