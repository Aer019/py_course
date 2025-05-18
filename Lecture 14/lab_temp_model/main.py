from lab_temp_model import BatterySimulation
import logging

FORMAT = '%(levelname)s - %(message)s'

def main():
    """Основная функция для настройки логирования и запуска симуляции батареи."""
    
    logger = logging.getLogger('battery.temperature')
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler('battery_temperature.log', mode='w')
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    battery_simulation = BatterySimulation(logger)
    battery_simulation.simulate_last_hour()

if __name__ == "__main__":
    main()
    print("I prefer to be a module")
else:
    print("I like to be a module")
