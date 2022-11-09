"""
Convert miles to km kivy program
"""

from kivy.app import App
from kivy.lang import Builder

__author__ = "Brock Allen"


class MilesToKmConverterApp(App):
    """Miles To KM Converter App is used for converting Miles to Kilometers"""

    def build(self):
        """Build the Kivy app for converting Miles to KM"""
        self.title = "Miles to KM Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


MilesToKmConverterApp().run()
