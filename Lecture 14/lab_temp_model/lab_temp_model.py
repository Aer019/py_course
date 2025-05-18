import logging
import random

FORMAT = '%(levelname)s - %(message)s'

class BatterySimulation:
    """Класс для симуляции температуры батареи в течение последнего часа."""
    def __init__(self, logger):
        self.logger = logger

    def simulate_last_hour(self):
        """Функция симулирующая изменение температуры батареи каждую минуту в течение часа."""
        for minute in range(1, 60 +1):
            temperature = random.randint(20, 40)

            if temperature < 30:
                self.logger.debug('{0} C'.format(temperature))
            elif temperature >= 30 and temperature <= 35:
                self.logger.warning('{0} C'.format(temperature))
            elif temperature > 35:
                self.logger.critical('{0} C'.format(temperature))
            else:
                raise Exception('Temperature out of range.')
            
if __name__ == "__main__":
    print("I prefer to be a module")
else:
    print("I like to be a module")