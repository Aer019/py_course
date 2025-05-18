import xml.etree.ElementTree as ET


class TemperatureConverter:
    """Класс конвертации градусов из Цельсия в Фаренгейта"""

    def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
        """Функция конвертации градусов из Цельсия в Фаренгейта"""
        return 9.0/5.0 * temperature_in_celsius + 32
    

class ForecastXmlParser:
    """Класс для парсинга XML-файлов с прогнозом погоды и преобразования температур."""
    def __init__(self, temperature_converter):
        """Функция инициализирует ForecastXmlParser с объектом преобразователя температур."""
        self.temperature_converter = temperature_converter

    def parse(self, file):
        """Функция парсит указанный XML-файл"""
        tree = ET.parse(file)
        root = tree.getroot()
        
        for child in root:
            day = child.find('day').text
            temperature_in_celsius = int(child.find('temperature_in_celsius').text)
            temperature_in_fahrenheit = round(self.temperature_converter.convert_celsius_to_fahrenheit(temperature_in_celsius), 1)
            print(f'{day}: {temperature_in_celsius} Celsius, {temperature_in_fahrenheit} Fahrenheit')
