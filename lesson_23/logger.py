import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logging.DEBUG
# logging.INFO
# logging.WARNING
# logging.ERROR

# Створюємо обробник для запису в файл
file_handler = logging.FileHandler('log_file.log')
file_handler.setLevel(logging.DEBUG)

# Створюємо обробник для виводу в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Встановлюємо форматування
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)


# Додаємо обробники до логгера
logger.addHandler(file_handler)
logger.addHandler(console_handler)
