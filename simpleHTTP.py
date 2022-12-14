from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import csv

class Handler(BaseHTTPRequestHandler): #класс обработки запросов
    def _set_response(self): #ответ ОК на запрос
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self): #реакция на POST запрос
        content_length = int(self.headers['Content-Length']) #получаем длину тела запроса
        post_data = self.rfile.read(content_length) #читаем тело запроса
        reqStr=str(post_data) #преобразуем в строку тело запроса
        if 'PICO' in reqStr: #если в теле запроса есть слово PICO, то выполняем код
            eventTime = time.localtime() #определяем системное время
            csvLine = [eventTime.tm_hour, eventTime.tm_min, eventTime.tm_sec, eventTime.tm_mday, eventTime.tm_mon, eventTime.tm_year, 1]  #массив данных времени и индикатор 1
            csv.writer(csvfile, delimiter=';').writerow(csvLine) #пишем в CSV массив как строчку, при этом разделяем элементы массива ;
            print(csvLine) #контрольная печать в консоль
#тело программы
print(chr(27) + "[2J") #очищаем экран 
with open('e:\coding\pico\datafile.csv', 'a') as csvfile: #создаем или открываем на дозапись файл csv
    server_class=HTTPServer #назначаем сервер
    handler_class=Handler #назначаем обрабочтик запросов
    port=3030 #порт обращения
    server_address = ('', port) #локальный адрес и указанный порт обращения
    http_listener = server_class(server_address, handler_class) #запускаем сервем с обработчиком запросов (листенер-слушатель)
    print('Starting http...\n') #контрольная печать в консоль
    try: #обработчик запросов работает в вечном цикле пока не будет команда на прерывание
        http_listener.serve_forever() #запускаем
    except KeyboardInterrupt: #если получаем ctlr-c выходим из цикла
        pass #выход из цикла
    http_listener.server_close() #отключаем сервер
    print('Stopping httpd...\n') #контрольная печать в консоль
