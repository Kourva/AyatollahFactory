#!/usr/bin/env python3

## Ayatollah Generator App Made With KivyMD
## GITHUB: https://github.com/Kourva

# Imports
from sys import exit
import random
import arabic_reshaper
import bidi.algorithm
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.toolbar.toolbar import MDTopAppBar, MDBottomAppBar
from kivymd.uix.textfield import MDTextField, MDTextFieldRect

# App Class
class AyatollahFactory(MDApp):
    
    def generate(self, *args):
        with open("data.csv") as data:
            colors = "1a2b34c5d67e8f90"
            lines = data.readlines()
            number = random.randint(1,19890)
            target = lines[number].split(",")[0].split('"')[1]
            meaning = lines[number].split(",")[1].split('"')[1]
            reshaped_meaning = bidi.algorithm.get_display(arabic_reshaper.reshape(meaning))
            reshaped_text = bidi.algorithm.get_display(arabic_reshaper.reshape("آیت الله " + target))

            self.Output.text = reshaped_text
            self.Meaning.text = reshaped_meaning
            self.Logo.color = "#" + "".join(random.choices(colors, k=6))
     
    # Clears OutPut
    def clear(self, *args):
        self.Output.text = ""
        self.Logo.color = "#ffffff"
        self.Meaning.text = ""
 
    # Opens Github Dialog
    def githubOpen(self, *args):
        self.Github.open()

    # Closes Github Dialog
    def githubClose(self, *args):
        self.Github.dismiss(force=True)

    # Build
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"

        home = MDScreen()

        # Top Toolbar
        self.Toolbar = MDTopAppBar(
            opposite_colors = True,
            title = "Ayatollah Factory",
            pos_hint = {"top": 1},
            right_action_items = [
                ["github", self.githubOpen],
                ["close-thick", lambda _: exit()]
            ]
        ) 

        # OutPut
        self.Output = MDTextFieldRect(
            cursor_blink = True,
            font_size = 20,
            font_name= "iransans.ttf",
            use_handles = True,
            halign = "center",
            size_hint = (0.5, None),
            multiline = False,
            height = "40dp",
            pos_hint = {"center_x": 0.5, "center_y": 0.3},
            background_color = "#4caf50"
        )

        # Meaning
        self.Meaning = MDTextFieldRect(
            cursor_blink = True,
            font_size = 20,
            font_name= "iransans.ttf",
            use_handles = True,
            halign = "center",
            size_hint = (0.98, None),
            multiline = False,
            height = "40dp",
            pos_hint = {"center_x": 0.5, "center_y": 0.05},
            background_color = "#4caf50",
        )

        # Build Botton
        self.GBotton = MDRaisedButton(
            text = "Build",
            text_color = "black",
            line_color = "black",
            size_hint = (0.2, None),
            height = "30dp",
            pos_hint = {"center_x": 0.35, "center_y": 0.2},
            on_press = self.generate
        )

        # Clear Botton
        self.CBotton = MDRaisedButton(
            text = "Clear",
            text_color = "black",
            line_color = "black",
            size_hint = (0.2, None),
            height = "30dp",
            pos_hint = {"center_x": 0.65, "center_y": 0.2},
            on_press = self.clear
        )

        # Text Label
        self.Text = MDLabel(
            font_style= "H6",
            text = "Ayatollah Factory - ImamZade Builder",
            theme_text_color = "Custom",
            text_color = "#4caf50",
            halign = "center",
            size_hint = (0.5, 0.5),
            pos_hint = {"center_x": 0.5, "center_y": 0.8},
        )

        # Text Meaning
        self.Hint = MDLabel(
            font_style= "Subtitle1",
            text = "** The Meaning Of Name **",
            theme_text_color = "Custom",
            text_color = "#000000",
            halign = "center",
            size_hint = (0.5, 0.5),
            pos_hint = {"center_x": 0.5, "center_y": 0.1},
        )

        # Github Dialog
        self.Github = MDDialog(
            title = "Developer Note",
            text = "Support me by giving a star :D\n\nhttps://github.com/Izolabela/AyatollahFactory",
            buttons = [
                MDFlatButton(
                    text = "Close",
                    theme_text_color = "Custom",
                    text_color = "#4caf50",
                    on_press = self.githubClose
                )
            ]
        )

        # Logo
        self.Logo = Image(
            source = 'logo.png',
            size_hint = (0.3, 0.3),
            pos_hint = {"center_x": 0.5, "center_y": 0.55},
        )

        # Add Widgets and Items
        home.add_widget(self.Toolbar)
        home.add_widget(self.Output)
        home.add_widget(self.GBotton)
        home.add_widget(self.CBotton)
        home.add_widget(self.Text)
        home.add_widget(self.Hint)
        home.add_widget(self.Logo)
        home.add_widget(self.Meaning)

        # Return Home 
        return home

# Run
AyatollahFactory().run()
