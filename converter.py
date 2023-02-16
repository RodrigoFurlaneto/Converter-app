import PySimpleGUI as sg

layout = [
    [
        sg.Input(key = '-INPUT-'), 
        sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key = '-CONVERTER-'),
        sg.Button('Convert', key = '-ENTER-'),
    ],
    [sg.Text('', key = '-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-ENTER-':
        if values['-INPUT-'].isnumeric():
            if values['-CONVERTER-'] == 'km to mile':
                 miles = int(values['-INPUT-']) / 1.609
                 update = f"{values['-INPUT-']}km are {round(miles, 2)} mile"
            elif values['-CONVERTER-'] == 'kg to pound':
                 pound = int(values['-INPUT-']) * 2.205
                 update = f"{values['-INPUT-']}kg are {round(pound, 2)} pound"
            else:
                 min = int(values['-INPUT-']) / 60
                 update = f"{values['-INPUT-']}sec are {round(min, 2)} min"
        else:
            update = 'You must type a number...'
    window['-OUTPUT-'].update(update)

window.close()
