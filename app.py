import PySimpleGUI as sg

lista = ["Brasil", "Alemanha"]

column1 = [[sg.Text(f'Scrollable{i}')] for i in range(10)]
column2 = [[sg.Text(f'{i}')] for i in lista]

layout = [
    [
        sg.Column(column1, scrollable=True, vertical_scroll_only=True),
        sg.Column(column2)
    ]
]

window = sg.Window('Scrollable', layout)
event, values = window.read()
window.close()
