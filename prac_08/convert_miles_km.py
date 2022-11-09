"""
Convert miles to km kivy program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = "Brock Allen"

MILES_TO_KM = 1.60934


class MilesToKmConverterApp(App):
    """Miles To KM Converter App is used for converting Miles to Kilometers"""
    conversion_output = StringProperty()

    def build(self):
        """Build the Kivy app for converting Miles to KM"""
        self.title = "Miles to KM Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.conversion_output = ""
        return self.root

    def convert_m_to_km(self, value):
        """Converts Miles to Kilometers"""
        try:
            result = float(value) * MILES_TO_KM
            self.conversion_output = str(f"{result:.3f}")
        except ValueError:
            self.conversion_output = str("0.0")

    def handle_increment(self, current_value, increment_value):
        """Increments the stated miles."""
        try:
            result = float(current_value) + increment_value
            self.root.ids.input_number.text = str(f"{result:.3f}")
            self.convert_m_to_km(result)
        except ValueError:
            result = 0 + increment_value
            self.root.ids.input_number.text = str(f"{result:.3f}")
            self.convert_m_to_km(result)
            pass


MilesToKmConverterApp().run()
