signal_intensity = int(input("Введіть інтенсивність сигналу (0-100): "))

# 1. Визначення рівня сигналу (від найбільшого значення до найменшого)
if signal_intensity >= 95:
    level = "Насичення фотоприймача"
elif signal_intensity >= 60:
    level = "Сильний сигнал"
elif signal_intensity >= 20:
    level = "Робочий діапазон"
else:
    level = "Слабкий сигнал"

# 2. Тернарний вираз для визначення режиму роботи
mode = "Потрібна увага" if (signal_intensity < 20 or signal_intensity >= 95) else "Звичайний режим"

# 3. Вивід результату
print(f"Рівень: {level}")
print(f"Режим: {mode}")
