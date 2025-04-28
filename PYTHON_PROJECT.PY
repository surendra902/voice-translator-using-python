from tkinter import *
from googletrans import Translator
import pyttsx3

# Create the main window
Screen = Tk()
Screen.title("Language Translator App")
Screen.config(bg="white")

# Define language choices
LanguageChoices = [
    'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian',
    'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese (Simplified)', 'Chinese (Traditional)',
    'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish',
    'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian',
    'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese',
    'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian',
    'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian',
    'Myanmar (Burmese)', 'Nepali', 'Norwegian', 'Odia (Oriya)', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi',
    'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak',
    'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai',
    'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba',
    'Zulu'
]

# Sort the language choices alphabetically
LanguageChoices.sort()

# Create language choice variables
InputLanguageChoice = StringVar(Screen)
TranslateLanguageChoice = StringVar(Screen)

# Set default language choices
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Spanish')

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Translate function
def Translate():
    translator = Translator()
    translation = translator.translate(TextVar.get(), src=InputLanguageChoice.get(), dest=TranslateLanguageChoice.get())
    OutputVar.set(translation.text)
    # Speak the translated text
    engine.say(translation.text)
    engine.runAndWait()

# Create the language choice menus
InputLanguageChoiceMenu = OptionMenu(Screen, InputLanguageChoice, *LanguageChoices)
InputLanguageChoiceMenu.config(bg="white")
InputLanguageChoiceMenu.grid(row=1, column=0, padx=10, pady=10)

TranslateLanguageChoiceMenu = OptionMenu(Screen, TranslateLanguageChoice, *LanguageChoices)
TranslateLanguageChoiceMenu.config(bg="white")
TranslateLanguageChoiceMenu.grid(row=1, column=2, padx=10, pady=10)

# Create the text input and output fields
Label(Screen, text="Enter Text", bg="white").grid(row=2, column=0, padx=10, pady=10)
TextVar = StringVar()
TextBox = Entry(Screen, textvariable=TextVar, bg="white", width=40, font=("Arial", 12))
TextBox.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

Label(Screen, text="Output Text", bg="white").grid(row=3, column=0, padx=10, pady=10)
OutputVar = StringVar()
OutputBox = Entry(Screen, textvariable=OutputVar, bg="white", width=40, font=("Arial", 12))
OutputBox.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

# Create the translate button
BtnTranslate = Button(Screen, text="Translate", command=Translate, relief=GROOVE, bg="light blue", fg="black", font=("Arial", 12))
BtnTranslate.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
Screen.mainloop()