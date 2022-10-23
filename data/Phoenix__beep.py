"""
Beep-коды представлены последовательностью звуковых сигналов
Например, 1-1-2 означает 1 короткий сигнал, пауза, 1 короткий сигнал, пауза, и 2 коротких сигнала.
"""
Phoenix = {
    '1 - 2': 'Ошибка в работе адаптеров, имеющих собственный BIOS',
    '1 - 1 - 2': 'Ошибка при тесте процессора. Процессор неисправен. Замените процессор',
    '1 - 1 - 3': 'Ошибка при чтении данных из микросхемы встроенной памяти СМОS',
    '1 - 1 - 4': 'Ошибка контрольной суммы микросхемы CMOS',
    '1 - 2 - 1': 'Ошибка на системной плате',
    '1 - 2 - 2': 'Ошибка контроллера DМА системной платы',
    '1 - 2 - 3': 'Ошибка чтения или записи данных в один из каналов DМА',
    '1 - 3 - 1': 'Ошибка в оперативной памяти',
    '1 - 3 - 3': 'Ошибка инициализации первых 64 Кбайт оперативной памяти',
    '1 - 3 - 4': 'Ошибка инициализации первых 64 Кбайт оперативной памяти',
    '1 - 4 - 1': 'Ошибка инициализации материнской платы',
    '1 - 4 - 2': 'Ошибка инициализации оперативной памяти',
    '1 - 4 - 3': 'Ошибка инициализации системного таймера',
    '1 - 4 - 4': 'Ошибка записи/чтения в/из одного из портов ввода/вывода',
    '2 - 1 - 1': 'Обнаружена ошибка при чтении/записи 0-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 1 - 2': 'Обнаружена ошибка при чтении/записи 1-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 1 - 3': 'Обнаружена ошибка при чтении/записи 2-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 1 - 4': 'Обнаружена ошибка при чтении/записи 3-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 2 - 1': 'Обнаружена ошибка при чтении/записи 4-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 2 - 2': 'Обнаружена ошибка при чтении/записи 5-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 2 - 3': 'Обнаружена ошибка при чтении/записи 6-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 2 - 4': 'Обнаружена ошибка при чтении/записи 7-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 3 - 1': 'Обнаружена ошибка при чтении/записи 8-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 3 - 2': 'Обнаружена ошибка при чтении/записи 9-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 3 - 3': 'Обнаружена ошибка при чтении/записи 10-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 3 - 4': 'Обнаружена ошибка при чтении/записи 11-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 4 - 1': 'Обнаружена ошибка при чтении/записи 12-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 4 - 2': 'Обнаружена ошибка при чтении/записи 13-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 4 - 3': 'Обнаружена ошибка при чтении/записи 14-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '2 - 4 - 4': 'Обнаружена ошибка при чтении/записи 15-го бита (в шестнадцатеричном представлении) первых 64 Кбайт ОЗУ',
    '3 - 1 - 1': 'Ошибка в первом канале DMA',
    '3 - 1 - 2': 'Ошибка во втором канале DМА',
    '3 - 1 - 3': 'Ошибка при обработке прерываний',
    '3 - 1 - 4': 'Ошибка контроллера прерываний материнской платы',
    '3 - 2 - 4': 'Ошибка контроллера клавиатуры',
    '3 - 3 - 4': 'Ошибка видеоадаптера',
    '3 - 4 - 1': 'Ошибка при тестировании видеопамяти',
    '3 - 4 - 2': 'Ошибка при поиске видеопамяти',
    '4 - 2 - 1': 'Ошибка системного таймера',
    '4 - 2 - 2': 'Завершение тестирования',
    '4 - 2 - 3': 'Ошибка контроллера клавиатуры',
    '4 - 2 - 4': 'Ошибка центрального процессора',
    '4 - 3 - 1': 'Ошибка тестирования оперативной памяти',
    '4 - 3 - 3': 'Ошибка системного таймера',
    '4 - 3 - 4': 'Ошибка часов реального времени',
    '4 - 4 - 1': 'Ошибка последовательного порта',
    '4 - 4 - 2': 'Ошибка параллельного порта',
    '4 - 4 - 3': 'Ошибка математического сопроцессора',
    '1 - 2 - 2 - 3': 'Ошибка при подсчете контрольной суммы BIOS',
    '1 - 3 - 1 - 1': 'Ошибка в работе оперативной памяти',
    '1 - 3 - 1 - 3': 'Ошибка контроллера клавиатуры',
    '1 - 3 - 4 - 1': 'Ошибки при тестировании оперативной памяти',
    '2 - 1 - 2 - 3': 'Ошибка при проверке уведомления об авторском праве ROM BIOS',
    '2 - 2 - 3 - 1': 'Ошибка при обработке непредвиденных прерываний',
    'continuous long': 'Неисправна материнская плата',
    'continuous high-low frequency': 'Неисправна видеокарта, проверить электролитические емкости, на утечку или заменить все на новые, заведомо исправные',
    'continuous': 'Не подключен (неисправен) кулер CPU'
}