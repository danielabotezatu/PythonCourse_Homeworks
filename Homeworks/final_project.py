import PySimpleGUI as sg
import time
from playsound import playsound

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp = "hosts"
redirect = "127.0.0.1"
web_sites_list = ["www.facebook.com", "facebook.com"]

sg.theme('DarkAmber')

def start_blocking_sites():
    with open(hosts_path, "r+") as file:
        content = file.read()
        for website in web_sites_list:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")
        file.close()

def stop_blocking_sites():

    with open(hosts_path, "r+") as file:
        content = file.readlines()
        file.seek(0)
        file.truncate()
        file.close()

    with open(hosts_path, "r+") as file:
        file.seek(0)
        print(content)
        for line in content:
            if not any(website in line for website in web_sites_list):
                file.write(line)
        file.close()
    time.sleep(1)

layout = [
    [sg.Text('Cat timp vrei sa inveti? ')],
    [sg.Text('Timp de studiu: ', size=(15, 1)), sg.InputText()],
    [sg.Text('Timp de pauza: ', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('Timer', layout, margins=(100, 100))
event, values = window.read()

if event == "Cancel" or event == sg.WIN_CLOSED :
    window.close()

else:
    study = int(values[0]) * 60 * 100
    pause = int(values[1]) * 60 * 100
    start_blocking_sites()
    window.close()

    layout = [[sg.Text('Timp de lucru', size=(20, 2), justification='center', key = '-OUTPUT1-')],
                  [sg.Text(size=(10, 2), font=('Helvetica', 20), justification='center', key='-OUTPUT-')],
                  [sg.T(' ' * 5), sg.Button('Start/Stop', focus=True), sg.Quit()]]

    window = sg.Window("Study", layout, margins=(200, 100))

    timer_running, counter = True, study

    while True:
        event, values = window.read(timeout=10)
        if event == "Quit" or event == sg.WIN_CLOSED:
            window.close()
            break

        elif event == "Start/Stop":
            timer_running = not timer_running
            if timer_running is True:
                start_blocking_sites()
            else:
                stop_blocking_sites()

        if timer_running:
            window['-OUTPUT-'].update(
                '{:02d}:{:02d}'.format((counter//100) // 60, (counter//100) % 60))
            counter -= 1

        if counter == 0:
            playsound('alarm.mp3')
            window['-OUTPUT-'].update("Sesiunea s-a terminat!")
            stop_blocking_sites()
            window.refresh()
            time.sleep(1.5)

            window['-OUTPUT-'].update("Pauza! ")
            window['-OUTPUT1-'].update("Pauza")
            timer_running_pause, counter_pause = True, pause

            window.refresh()
            time.sleep(2)

            while True:
                event, values = window.read(timeout=10)
                if event == "Quit" or event == sg.WIN_CLOSED:
                    window.close()

                elif event == "Start/Stop":
                    if counter_pause != 0:
                        timer_running_pause = not timer_running_pause

                    elif counter_pause == 0:
                        window.close()
                        layout = [[sg.Text('Timp de lucru', size=(20, 2), justification='center', key = '-OUTPUT1-')],
                                  [sg.Text(size=(10, 2), font=('Helvetica', 20), justification='center', key='-OUTPUT-')],
                                  [sg.T(' ' * 5), sg.Button('Start/Stop', focus=True), sg.Quit()]]

                        window = sg.Window("Study", layout, margins=(200, 100))

                        timer_running, counter = True, study
                        break
                if counter_pause == 0:
                    playsound('alarm.mp3')
                    timer_running_pause = False
                    window['-OUTPUT-'].update("Pauza s-a terminat!")
                    window.refresh()
                    time.sleep(1.5)

                if timer_running_pause:
                    window['-OUTPUT-'].update('{:02d}:{:02d}'.format((counter_pause//100) // 60, (counter_pause//100) % 60 ))
                    counter_pause -= 1

    window.close()
