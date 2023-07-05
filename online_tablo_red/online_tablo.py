import tkinter
from functools import wraps
import datetime
import requests
import icalendar
from screeninfo import get_monitors
import json

# расчет координат
displays = get_monitors()
if len(displays) == 1:
    coord_disp = {
        'width': displays[0].width,
        'height': displays[0].height,
        'x': 0,
        'y': 0
        }
elif len(displays) > 1:
    coord_disp = {
        'width': displays[1].width,
        'height': displays[1].height,
        'x': displays[1].x,
        'y': 0
        }
else:
    coord_disp = {
        'width': 1920,
        'height': 1080,
        'x': 0,
        'y': 0
        }

# извлечение конфигурационных данных
# get configuration data

data = {
        'URL':'url_of_calendar',
        'MAIN_TITLE': 'main_title_to_app',
        'RIGHT_TITLE': 'title_to_right_column',
        'LEFT_TITLE': 'title_to_left_column',
        'MAIN_FONT': int(coord_disp['height'] / 70),
        'REGULAR_FONT': int(coord_disp['height'] / 90),
        'BIG_FONT': int(coord_disp['height'] / 30),
        'SMALL_FONT': int(coord_disp['height'] / 100)
}
try:
    with open('data.json', 'r', encoding='utf-8') as file:
        temp_data = json.load(file)
        for x in temp_data:
            if x:
                data[x] = temp_data[x]
except FileNotFoundError: 
    pass

# главные переменные
# main variables
URL = data.get('URL', '')
MAIN_TITLE = data.get('MAIN_TITLE', '')
RIGHT_TITLE = data.get('RIGHT_TITLE', '')
LEFT_TITLE = data.get('LEFT_TITLE', '')
MAIN_FONT = int(coord_disp['height'] / 70)
REGULAR_FONT = int(coord_disp['height'] / 90),
BIG_FONT = int(coord_disp['height'] / 30)
SMALL_FONT = int(coord_disp['height'] / 100)
# цвет
# color
COLOR_LEFT = '#051512' 
COLOR_RIGHT = '#220605'
COLOR_DESCRIPTION = 'black'
COLOR_SUMMARY = '#1b1b1b'

## пропорции координат

line_width = round(coord_disp['height'] / 360) # толщина главных разделительных линий

# высота!
all_title_height = round(coord_disp['height'] / 13) # общая высота заголовка
main_title_height = round(all_title_height / 3 * 2) # высота главного заголовка
sub_title_height = round(all_title_height / 3) # высота подзаголовка

all_events_height = coord_disp['height'] - all_title_height - line_width # высота общей области мероприятий
event_height = round(all_events_height / 7) # высота одного мероприятия
summary_height = round(event_height / 5) # высота названия мероприятия
description_height = event_height - summary_height # высота описания мероприятия

time_height = summary_height # высота времени
month_height = summary_height # высота месяца
week_height = summary_height # высота дня недели
date_height = event_height - time_height - month_height - week_height # высота даты

# ширина!
time_width = round(coord_disp['width'] / 2 / 6) # ширина вермени
event_width = round(coord_disp['width'] / 2 - time_width - line_width) # ширина мероприятия

# создание главного окна
root = tkinter.Tk()
root.title(MAIN_TITLE)
#root.geometry(f"{coord_disp['width']}x{coord_disp['height']}+{coord_disp['x']}+{coord_disp['y']}")
root.geometry(f"{displays[0].width}x{displays[0].height}+{displays[0].x}+{displays[0].y}")

#полноэкранный режим
root.overrideredirect(True)
#root.attributes('-fullscreen', True)

def quit(e):
    root.destroy()

# кликом правой кнопки мыши - закрытие программы
root.bind('<Button-3>', quit)

# общее поле программы
#canv = tkinter.Canvas(root, bg='black', width=coord_disp['width'], height=coord_disp['height'])
canv = tkinter.Canvas(root, bg='black', width=displays[0].width, height=displays[0].height)
canv.pack()

## основные линии таблицы
# horisontal 1
canv.create_line(
    coord_disp['x'],
    main_title_height + coord_disp['y'],
    coord_disp['width'] + coord_disp['x'],
    main_title_height + coord_disp['y'],
    width=line_width,
    fill='white'
)
# horisontal 2
canv.create_line(
    coord_disp['x'],
    all_title_height + coord_disp['y'],
    coord_disp['width'] + coord_disp['x'],
    all_title_height + coord_disp['y'],
    width=line_width,
    fill='white'
)
#vertical half
canv.create_line(
    coord_disp['width'] / 2 + coord_disp['x'],
    main_title_height + coord_disp['y'],
    coord_disp['width'] / 2 + coord_disp['x'],
    coord_disp['height'] + coord_disp['y'],
    width=line_width,
    fill='white'
)
# left time vertical line
canv.create_line(
    time_width + coord_disp['x'],
    all_title_height + coord_disp['y'],
    time_width + coord_disp['x'],
   coord_disp['height'] + coord_disp['y'],
    width=line_width,
    fill='white',
    dash=(2,4)
)

# right time vertical line
canv.create_line(
    coord_disp['width'] / 2 + time_width + line_width + coord_disp['x'],
    all_title_height + coord_disp['y'],
    coord_disp['width'] / 2 + time_width + line_width + coord_disp['x'],
   coord_disp['height'] + coord_disp['y'],
    width=line_width,
    fill='white',
    dash=(2,4)
)

# event horisontal line
for i in range(6):
    canv.create_line(
        coord_disp['x'],
        all_title_height + event_height + line_width + i*event_height + coord_disp['y'],
        coord_disp['width'] + coord_disp['x'],
        all_title_height + event_height + line_width + i*event_height + coord_disp['y'],
        width=line_width,
        fill='white',
        dash=(2,4)
    )

#
main_text = canv.create_text(
    coord_disp['width'] / 2 + coord_disp['x'],
    main_title_height / 3 * 2 + coord_disp['y'],
    text= "[ ... ИДЕТ ЗАГРУЗКА ... ]",
    fill='white',
    anchor='s',
    font=('monotype', MAIN_FONT, 'bold'))

left_column = canv.create_text(
    coord_disp['width'] / 4 + coord_disp['x'],
    all_title_height - line_width + coord_disp['y'],
    text='[ ... ]',
    fill='green',
    anchor='s',
    font=('monotype', REGULAR_FONT, 'bold'))

right_column = canv.create_text(
    coord_disp['width'] / 4 + coord_disp['width'] / 2 + coord_disp['x'],
    all_title_height - line_width + coord_disp['y'],
    text='[ ... ]',
    fill='red',
    anchor='s',
    font=('monotype', REGULAR_FONT, 'bold'))


# размещение инфо областей на экране
def label_place(obj, column):
    what_column = {'rep': coord_disp['x'], 'spect': coord_disp['width'] / 2 + line_width + coord_disp['x']}
    for i in obj:
        #
        obj[i]['summary'].place(
            x=what_column[column] + time_width + line_width,
            y=(all_title_height+line_width)+(i-1)*event_height + coord_disp['y'],
            width=event_width-line_width,
            height=summary_height
        )
        obj[i]['description'].place(
            x=what_column[column] + time_width + line_width,
            y=(all_title_height+line_width) + summary_height + (i-1)*summary_height + (i-1)*description_height + coord_disp['y'],
            width=event_width-line_width,
            height=description_height - line_width
        )
        obj[i]['time'].place(
            x=what_column[column],
            y=(all_title_height + line_width) + (i-1)*event_height + coord_disp['y'],
            width=time_width,
            height=time_height
        )
        obj[i]['month'].place(
            x=what_column[column],
            y=(all_title_height+line_width)+time_height+date_height+(i-1)*time_height+(i-1)*month_height+(i-1)*date_height+(i-1)*week_height + coord_disp['y'],
            width=time_width,
            height=month_height
        )
        obj[i]['date'].place(
            x=what_column[column],
            y=(all_title_height+line_width)+time_height+(i-1)*time_height+(i-1)*month_height+(i-1)*date_height+(i-1)*week_height + coord_disp['y'],
            width=time_width,
            height=date_height
        )
        obj[i]['week'].place(
            x=what_column[column],
            y=(all_title_height+line_width)+time_height+(i-1)*time_height+date_height+month_height+(i-1)*month_height+(i-1)*date_height+(i-1)*week_height + coord_disp['y'],
            width=time_width,
            height=week_height - line_width)
        #
        for i in obj:
            obj[i]['summary'].configure(wraplength=event_width)
            obj[i]['description'].configure(wraplength=event_width)
            obj[i]['time'].configure(wraplength=time_width)
            obj[i]['date'].configure(wraplength=time_width)
            obj[i]['month'].configure(wraplength=time_width)
            obj[i]['week'].configure(wraplength=time_width)

# словарь с объектами полей для репетиций
rep_label_dict = {
    1: {
        'summary': tkinter.Label(bg=COLOR_LEFT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_LEFT),
        'date': tkinter.Label(bg=COLOR_LEFT),
        'month': tkinter.Label(bg=COLOR_LEFT),
        'week': tkinter.Label(bg=COLOR_LEFT)
    },
    2: {
        'summary': tkinter.Label(bg=COLOR_LEFT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_LEFT),
        'date': tkinter.Label(bg=COLOR_LEFT),
        'month': tkinter.Label(bg=COLOR_LEFT),
        'week': tkinter.Label(bg=COLOR_LEFT)
    },
    3: {
        'summary': tkinter.Label(bg=COLOR_LEFT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_LEFT),
        'date': tkinter.Label(bg=COLOR_LEFT),
        'month': tkinter.Label(bg=COLOR_LEFT),
        'week': tkinter.Label(bg=COLOR_LEFT)
    },
    4: {
        'summary': tkinter.Label(bg=COLOR_LEFT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_LEFT),
        'date': tkinter.Label(bg=COLOR_LEFT),
        'month': tkinter.Label(bg=COLOR_LEFT),
        'week': tkinter.Label(bg=COLOR_LEFT)
    },
    5: {
        'summary': tkinter.Label(bg=COLOR_LEFT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_LEFT),
        'date': tkinter.Label(bg=COLOR_LEFT),
        'month': tkinter.Label(bg=COLOR_LEFT),
        'week': tkinter.Label(bg=COLOR_LEFT)
    },
    6: {
        'summary': tkinter.Label(bg=COLOR_LEFT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_LEFT),
        'date': tkinter.Label(bg=COLOR_LEFT),
        'month': tkinter.Label(bg=COLOR_LEFT),
        'week': tkinter.Label(bg=COLOR_LEFT)
    },
    7: {
        'summary': tkinter.Label(bg=COLOR_LEFT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_LEFT),
        'date': tkinter.Label(bg=COLOR_LEFT),
        'month': tkinter.Label(bg=COLOR_LEFT),
        'week': tkinter.Label(bg=COLOR_LEFT)
    }
    
}

# словарь с объектами полей для спектаклей
spec_label_dict = {
    1: {
        'summary': tkinter.Label(bg=COLOR_RIGHT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_RIGHT),
        'date': tkinter.Label(bg=COLOR_RIGHT),
        'month': tkinter.Label(bg=COLOR_RIGHT),
        'week': tkinter.Label(bg=COLOR_RIGHT)
    },
    2: {
        'summary': tkinter.Label(bg=COLOR_RIGHT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_RIGHT),
        'date': tkinter.Label(bg=COLOR_RIGHT),
        'month': tkinter.Label(bg=COLOR_RIGHT),
        'week': tkinter.Label(bg=COLOR_RIGHT)
    },
    3: {
        'summary': tkinter.Label(bg=COLOR_RIGHT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_RIGHT),
        'date': tkinter.Label(bg=COLOR_RIGHT),
        'month': tkinter.Label(bg=COLOR_RIGHT),
        'week': tkinter.Label(bg=COLOR_RIGHT)
    },
    4: {
        'summary': tkinter.Label(bg=COLOR_RIGHT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_RIGHT),
        'date': tkinter.Label(bg=COLOR_RIGHT),
        'month': tkinter.Label(bg=COLOR_RIGHT),
        'week': tkinter.Label(bg=COLOR_RIGHT)
    },
    5: {
        'summary': tkinter.Label(bg=COLOR_RIGHT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_RIGHT),
        'date': tkinter.Label(bg=COLOR_RIGHT),
        'month': tkinter.Label(bg=COLOR_RIGHT),
        'week': tkinter.Label(bg=COLOR_RIGHT)
    },
    6: {
        'summary': tkinter.Label(bg=COLOR_RIGHT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_RIGHT),
        'date': tkinter.Label(bg=COLOR_RIGHT),
        'month': tkinter.Label(bg=COLOR_RIGHT),
        'week': tkinter.Label(bg=COLOR_RIGHT)
    },
    7: {
        'summary': tkinter.Label(bg=COLOR_RIGHT),
        'description': tkinter.Label(bg=COLOR_DESCRIPTION),
        'time': tkinter.Label(bg=COLOR_RIGHT),
        'date': tkinter.Label(bg=COLOR_RIGHT),
        'month': tkinter.Label(bg=COLOR_RIGHT),
        'week': tkinter.Label(bg=COLOR_RIGHT)
    }
}

# удаление html тэгов
def edit_description(text):
        filter_none = [
            '<html-blob>',
            '</html-blob>', 
            '<br>',
            '<b>',
            '</b>',
            '<i>',
            '</i>',
            '<u>',
            '</u>',
            '<br />',
            '&nbsp;&nbsp;'
        ]
        filter_space = ['\n']
        filter_1 = [
            'пом. реж. Адамова Ю.Э.',
            'пом. реж. Петрова О.А.',
            'пом. реж. Катырева Т.Б.',
            'пом. реж. Марченко Л.М.',
            'пом. реж. Павлюкова Е.И.'
        ]

        for x in filter_none:
            text = text.replace(x, '')

        for x in filter_space:
            text = text.replace(x, ' ')

        text = text.replace(',', ', ')
        for x in filter_1:
            text = text.replace(x, f'\n={x}\n')
        
        return text


# запрос событий календаря
def get_calendar(url):
    url = url
    try:
        # скачивание данных календаря
        web_data = requests.get(url).text
        # сохранение данных и даты скачивания бэкапного файла
        with open('content.json', 'w', encoding='utf-8') as file:
            json.dump(web_data, file, ensure_ascii=False)
        with open('date.json', 'w') as file:
            json.dump(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'), file)
        status = 'online'
        
    except Exception as e:
        print(e)
        try:
            with open('content.json', 'r', encoding='utf-8') as file:
                web_data = json.load(file)
        except Exception as e:
            print(e)
            web_data = None
        status = 'offline'

    return(status, web_data)

# отбор данных (словарь) будущих мероприятий календаря и упаковка в список
def get_data(data_file):
    # установка переменной часового пояса и ссылки на календарь
    delta = datetime.timedelta(hours=5)
    ical = icalendar.Calendar.from_ical(data_file)
    # отбор мероприятий
    ical_data = ical.walk()
    ical_data = [x for x in ical_data if x.name == 'VEVENT']

    data = []
    for x in ical_data:
        temp_dict = {}
        # заполнение словаря мероприятия
        temp_dict['start'] = datetime.datetime.fromisoformat(str(x.decoded('DTSTART', '2000-01-01'))) + delta
        temp_dict['end'] = datetime.datetime.fromisoformat(str(x.decoded('DTEND', '2000-01-01'))) + delta
        temp_dict['summary'] = str(x.get('SUMMARY', ''))
        temp_dict['description'] = edit_description(str(x.get('DESCRIPTION', '')))
        temp_dict['location'] = str(x.get('LOCATION', ''))
        # добавление в список словарь мероприятия
        data.append(temp_dict)
    # отсев будущих мероприятий и сортировка по порядку
    future_data = [x for x in data if x['start'].timestamp() > datetime.datetime.today().timestamp()]
    future_data = sorted(future_data, key=lambda x: x['start'], reverse=False)

    return future_data

# сортировка по колоннам
def sort_data(data):
    filter_list_rep = [
            'репетиция',
            'прогон',
            'читка',
            'сдача',
            'сбор',
            'иформация'
        ]

    filter_list_act = [
            'премьера',
            'спектакль', 
            'выезд'
        ]

    rep_list = list(filter(lambda x: any([i in x['summary'].lower() for i in filter_list_rep]), data))  
    spect_list = list(filter(lambda x: any([i in x['summary'].lower() for i in filter_list_act]), data))

    return (rep_list, spect_list)

# подготовка дянных для отображения
def set_data(data, area):
    weekdays_name_dict = {
        0: 'ПОНЕДЕЛЬНИК',
        1: 'ВТОРНИК',
        2: 'СРЕДА',
        3: 'ЧЕТВЕРГ',
        4: 'ПЯТНИЦА',
        5: 'СУББОТА',
        6: 'ВОСКРЕСЕНЬЕ'
    }

    month_name_dict = {
        1: 'Января',
        2: 'Февраля',
        3: 'Марта',
        4: 'Апреля',
        5: 'Мая',
        6: 'Июня',
        7: 'Июля',
        8: 'Августа',
        9: 'Сентября',
        10: 'Октября',
        11: 'Ноября',
        12: 'Декабря'
    }
    # 
    index = 0
    while index < len(data) and (index+1) in area.keys():
        #
        area[index+1]['summary'].configure(
            text=f"{data[index]['summary']} ({data[index]['location']})",
            fg='white',
            anchor='sw',
            font=('monotype', MAIN_FONT, 'bold'),
            justify=tkinter.LEFT)
        #
        area[index+1]['description'].configure(
            text=data[index]['description'],
            fg='#BBBBBB',
            anchor='nw',
            font=('monotype', REGULAR_FONT),
            justify=tkinter.LEFT)
        #
        area[index+1]['time'].configure(
            text=f"{data[index]['start'].strftime('%H:%M')} -- {data[index]['end'].strftime('%H:%M')}",
            fg='white',
            anchor='s',
            font=('monotype', REGULAR_FONT, 'bold'),
            justify=tkinter.CENTER)
        #
        area[index+1]['date'].configure(
            text=data[index]['start'].day,
            fg='white',
            anchor='s',
            font=('monotype', BIG_FONT, 'bold'),
            justify=tkinter.CENTER)
        #
        area[index+1]['month'].configure(
            text=month_name_dict[data[index]['start'].month],
            fg='white',
            anchor='n',
            font=('monotype', REGULAR_FONT, 'bold'),
            justify=tkinter.CENTER)
        #
        area[index+1]['week'].configure(
            text=weekdays_name_dict[data[index]['start'].weekday()],
            fg='white',
            anchor='n',
            font=('monotype', SMALL_FONT, 'italic'),
            justify=tkinter.CENTER)

        index += 1
        
# главная выполняющая функция
def main():
    web_data = get_calendar(URL)
    if web_data[1]:
        if web_data[0] == 'online':
            canv.itemconfig(main_text, text = f'#online {MAIN_TITLE} online#')
            canv.itemconfig(left_column, text = LEFT_TITLE)
            canv.itemconfig(right_column, text = RIGHT_TITLE)
        else:
            try:
                with open('date.json', 'r', encoding='utf-8') as file:
                    date = json.load(file)
                    canv.itemconfig(main_text, text = f'!!! ВНИМАНИЕ : ОТСУТСТВУЕТ  ПОДКЛЮЧЕНИЕ  К  ИНТЕРНЕТУ !!! последнее обновление:  {date}')
                    canv.itemconfig(left_column, text = LEFT_TITLE)
                    canv.itemconfig(right_column, text = RIGHT_TITLE)
            except:
                canv.itemconfig(main_text, text = '!!! ВНИМАНИЕ : ОТСУТСТВУЕТ  ПОДКЛЮЧЕНИЕ  К  ИНТЕРНЕТУ !!!')
        #
        label_place(rep_label_dict, 'rep')
        label_place(spec_label_dict, 'spect')
        #    
        all_data = get_data(web_data[1])
        data = sort_data(all_data)
        set_data(data[0], rep_label_dict)
        set_data(data[1], spec_label_dict)
    else:
        canv.itemconfig(main_text, text = f'!!! ВНИМАНИЕ : ЧТО-ТО ПОШЛО НЕ ТАК !!!')
    # цикл
    root.after(15000, main)
        
# главный цикл для отображение GUI
root.after(1000, main)
root.mainloop()


