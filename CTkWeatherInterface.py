import customtkinter as ctk

from infoFinder import PlaceInfo
from widgetText import *

ctk.set_appearance_mode("dark")

class WeatherApp(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.iconbitmap('images/weather-forecast.ico')
        self.title(titleRu)
        app_width = 400
        app_height = 600
        x = self.winfo_screenwidth() - 2*app_width
        y = (self.winfo_screenheight() - app_height)/2
        self.geometry(f'{app_width}x{app_height}+{x}+{y}')
        self.resizable(False, False)

        twFont = ctk.CTkFont('Uniform Bro Black', 56)
        infoFont = ctk.CTkFont('Futura', 20)
        errorFont = ctk.CTkFont('Futura', 15)

        self.findingFrame = ctk.CTkFrame(self)
        self.findingFrame.pack(pady=30)
        self.placeLabel = ctk.CTkLabel(self.findingFrame, text=placeLabelTextRu, font=infoFont).pack(pady=5)
        self.placeInputField = ctk.CTkEntry(self.findingFrame, width=300, placeholder_text=placeInputFieldTextRu)
        self.placeInputField.pack(pady=10)
        self.showBtn = ctk.CTkButton(self.findingFrame, text=showBtnTextRu, font=infoFont,
                                    fg_color='blue', command=self.showData).pack(pady=10)
        self.wrongInput = ctk.CTkLabel(self.findingFrame, text='', font=errorFont, text_color='red')
        self.wrongInput.pack()

        self.timeFrame = ctk.CTkFrame(self)
        self.timeFrame.pack(padx=10)
        self.timeLabel = ctk.CTkLabel(self.timeFrame, text=timeLabelTextRu, font=infoFont).pack(padx=10, pady=5)
        self.timeCur = ctk.CTkLabel(self.timeFrame, text=f'--:--', font=twFont)
        self.timeCur.pack(padx=10, pady=10)

        self.gradFrame = ctk.CTkFrame(self)
        self.gradFrame.pack(padx=10, pady=30)
        self.weatherLabel = ctk.CTkLabel(self.gradFrame, text=weatherLabelTextRu, font=infoFont).pack(padx=10, pady=5)
        self.weatherCur = ctk.CTkLabel(self.gradFrame, text=f'--°C', font=twFont)
        self.weatherCur.pack(padx=10, pady=10)

        self.settingBtn = ctk.CTkButton(self, text=settingTextRu, command=self.openToplevel, fg_color='#9A92E1')
        self.settingBtn.pack()
        self.toplevel_window = None

    def showData(self):
        try:
            self.place = PlaceInfo(self.placeInputField.get())
            temp = self.place.getTemp()
            time = self.place.getTime()
            self.weatherCur.configure(text=f'{temp}°C')
            self.timeCur.configure(text=f'{time}')
            self.wrongInput.configure(text='')
        except:
            self.wrongInput.configure(text=wrongInputTextRu)

    def openToplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = SettingsWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.iconbitmap('images/weather-forecast.ico')
        self.title(settingTextRu)
        self.geometry("400x400")
        self.resizable(False, False)

        pointFont = ctk.CTkFont('Uniform Bro Black', 20)
        labelFont = ctk.CTkFont('Futura', 30)

        self.themeLabel = ctk.CTkLabel(self, text=themeLabelTextRu, font=labelFont)
        self.themeLabel.pack(padx=20, pady=20)

        self.themeRadio_var = ctk.IntVar(value=0)
        self.blackTheme = ctk.CTkRadioButton(self, text=blackThemeTextRu, font=pointFont,
                                                     command=self.radiobutton_event_color, variable=self.themeRadio_var, value=1)
        self.lightTheme = ctk.CTkRadioButton(self, text=lightThemeTextRu, font=pointFont,
                                                     command=self.radiobutton_event_color, variable=self.themeRadio_var, value=2)
        self.blackTheme.pack(pady=10)
        self.lightTheme.pack(pady=10)


        self.langLabel = ctk.CTkLabel(self, text=langLabelText, font=labelFont)
        self.langLabel.pack(padx=20, pady=20)

        self.langRadio_var = ctk.IntVar(value=0)
        self.rusLang = ctk.CTkRadioButton(self, text=rusLangText, font=pointFont,
                                                          command=self.radiobutton_event_lang, variable=self.langRadio_var,
                                                          value=1, state='normal')
        self.engLang = ctk.CTkRadioButton(self, text=engLangText, font=pointFont,
                                                          command=self.radiobutton_event_lang, variable=self.langRadio_var,
                                                          value=2, state='disabled')
        self.rusLang.pack(pady=10)
        self.rusLang.select()
        self.engLang.pack(pady=10)

    def radiobutton_event_color(self):
        if self.themeRadio_var.get() == 1:
            ctk.set_appearance_mode('dark')
        elif self.themeRadio_var.get() == 2:
            ctk.set_appearance_mode('light')

    def radiobutton_event_lang(self):
        pass