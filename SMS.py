from weather_sdk import get_new_event, SMSServer
import os


token = os.getenv('FORECAST_TOKEN')
town_title = 'Курск'

sms_token = os.getenv('SMS_TOKEN')
server = SMSServer(sms_token)

new_event = get_new_event(token, town_title)

event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = '''{}: {} {} {} ожидается {}. Будьте внимательны и осторожны.'''

sms_message = sms_template.format(
    town_title,
    event_time,
    event_date,
    event_area,
    phenomenon_description,
)

server.send(sms_message)


# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print('new_event ', new_event)
# Установленный факт: Переменная new_event выводит 2 строчки без значений "Регион:  Погода:"
# Вывод: Функция которая назначается для переменной "new_event" некорректно принимает или не принимает аргументы.

# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: Выведу переменную title
# Код для проверки: print("town_title", town_title)
# Установленный факт: В переменной town_title есть строчка с названием города "Курск"
# Вывод: Переменная town_title не пустая. Она принимает строку

# Гипотеза 2.2: В town_title не название города
# Способ проверки: Выведу переменную title
# Код для проверки: print("town_title", town_title)
# Установленный факт: В переменной town_title название города
# Вывод: Переменная указывается корректно и принимает строку с названием города.

# Гипотеза 3: Переменная token на самом деле пуста
# Способ проверки: Выведу переменную token
# Код для проверки: print("token", token)
# Установленный факт: Переменная token выводит None
# Вывод: Функция  os.getenv, с параметром SMS_TOKEN возвращает None. Возможно в переменной среды ничего нет.

# Гипотеза 4.1: Может, `token` всё ещё пуст?
# Способ проверки: Выведу переменную token подставив значения для переменной окружения
# Код для проверки: print("token", token)
# Установленный факт: Способ вывел значение переменной token
# Вывод: Подставив значение для переменной окружения не исправляет ошибку.

# Гипотеза 4.2: Может, в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`?
# Способ проверки: Выведу переменную token подставив значения для переменной окружения
# Код для проверки:  print("token", token)
# Установленный факт: Отобразилось значение переменной токена `85b98d96709fd49a69ba8165676e4592`.
# Вывод: Подставленное значение соответствует действительности при проверке.

# Гипотеза 4.3: Может, значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки `new_event = ...`?
# Способ проверки: Закомментировать последущие присвоения для переменной token. И вывести переменную new_event через print
# Код для проверки: print("new_event", new_event)
# Установленный факт: Подставились значения со строками "Регион", "Погода" при выводе переменной new_event
# Вывод: Дальнейшее изменние значение переменной token убирает значения переменной new_event

# Гипотеза 5.1: Переменная `event_time` пуста/в ней не время
# Способ проверки: Вывести значение переменной event_time на экран до переменной sms_message
# Код для проверки: print("event_time утром", event_time)
# Установленный факт: Значение переменной event_time утром выводит "утром"
# Вывод: В переменную event_time верно подставляются значения/не пуста

# Гипотеза 5.2: Переменная `event_date` пуста/в ней не дата
# Способ проверки: Вывести значение переменной event_date на экран до переменной sms_message
# Код для проверки: print("event_date", event_date)
# Установленный факт: Переменная event_date вывело строку "5 сентября"
# Вывод: В переменную event_date верно подставляются значения/не пуста

# Гипотеза 5.3: Переменная `event_area` пуста/в ней не место
# Способ проверки: Вывести значение переменной event_area на экран до переменной sms_message
# Код для проверки: print("event_area", event_area)
# Установленный факт: Значение переменной event_area утром выводит строку "д. Обоянь"
# Вывод: В переменную event_area верно подставляются значения/не пуста

# Гипотеза 5.4: Переменная `phenomenon_description` пуста/в ней не описание погодного явления
# Способ проверки: Вывести значение переменной phenomenon_description на экран до переменной sms_message
# Код для проверки: print("phenomenon_description", phenomenon_description)
# Установленный факт: Значение переменной phenomenon_description утром выводит строку "заморозки до минус 34 градусов"
# Вывод: В переменную phenomenon_description верно подставляются значения/не пуста

# Гипотеза 6.1: Использование f-строк.
# Способ проверки: Использовать f-строк для того чтобы явно указать переменную в тексте, вместо обычной строки. Это позволит проверить верно ли указана переменная при редактировании строки.
# Код для проверки: sms_template = f'''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''
# Установленный факт: Код запускается, но не верно отображает анимацию
# Вывод: Код запускается через раз

# Гипотеза 6.2: Использование ключевых слов
# Способ проверки: Указать ключевые слова, при использовании метода format
# Код для проверки: sms_message = sms_template.format(
#     phenomenon_description=phenomenon_description,
#     town_title=town_title,
#     event_time=event_time,
#     event_date=event_date,
#     event_area=event_area,
# )
# Установленный факт: Код запускается, но не верно отображает анимацию загрузки
# Вывод: Метод использования ключевых слов, помогает избежать ошибок при указании переменных строки в шаблоне.

# Гипотеза 6.3: Указать переменные в круглых скобках
# Способ проверки: Заменить фигурные скобки в шаблоне на круглые
# Код для проверки: sms_template = '''(town_title): (event_time) (event_date) (event_area) ожидается (phenomenon_description). Будьте внимательны и осторожны.'''
# Установленный факт: Код запускается, но отображается неверная анимация
# Вывод: Использование круглых скобок не исправляет ошибку

# Гипотеза 6.4: Указать переменные в квадратных скобках
# Способ проверки: Заменить фигурные скобки в шаблоне на квадртаные
# Код для проверки: sms_template = '''(town_title): (event_time) (event_date) (event_area) ожидается (phenomenon_description). Будьте внимательны и осторожны.'''
# Установленный факт: Код запускается, но отображается неверная анимация
# Вывод: Редактирование строки в шаблоне, не меняет результат вывода

# Гипотеза 7: Указать аргументы по умолчанию
# Способ проверки: Оставить фигурные скобки пустые
# Код для проверки: sms_template = '''{}: {} {} {} ожидается {}. Будьте внимательны и осторожны.'''
# Установленный факт: Код запускается, но отображается неверная анимация
# Вывод: Редактирование строки в шаблоне, не меняет результат вывода


# Гипотеза 8: Использование ключевых слов в переменных шаблона
# Способ проверки: Использовать имена для переменных в шаблоне с текстом, для редактирование значений.
# Код для проверки: sms_template = '''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''
#                   sms_message = sms_template.format(
#    town_title=town_title,
#    event_time=event_time,
#    event_date=event_date,
#    event_area=event_area,
#   phenomenon_description=phenomenon_description,
#)                

# Установленный факт: Подставив значение, информация отображается верно
# Вывод: Использование ключевых слов, позволяет подставлять в шаблон текста необходимые строчки, а также изменят их с помощью .format().