# Таймер напоминалка
import time  # Модуль для работы со временем

text = str(input('О чем вам напомнить?'))
hourses = float(input('Через сколько часов?'))
local_time = float(input('Через сколько минут?'))
# Переводим минуты в секунды
minutes = local_time * 60
# Переводим часы в минуты
hours = hourses * 3600
# Запуск таймера
time.sleep(hours + minutes)
# Отображаем напоминание
print(text)
