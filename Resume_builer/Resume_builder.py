import datetime
from pathlib import Path

import PySimpleGUI as sg
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / "DEMOCV.docx"
doc = DocxTemplate(document_path)

today = datetime.datetime.today()
today_in_one_week = today + datetime.timedelta(days=7)

layout = [
    [sg.Text("Document Name"), sg.Input(key="DOCUMENTNAME", do_not_clear=False)],
    [sg.Text('Please enter your personal details:')],
    [sg.Text("First & last names:"), sg.Input(key="NAMES", do_not_clear=False)],
    [sg.Text("Address:"), sg.Input(key="ADDRESS", do_not_clear=False)],
    [sg.Text("Phone:"), sg.Input(key="PHONE", do_not_clear=False)],
    [sg.Text("Email:"), sg.Input(key="EMAIL", do_not_clear=False)],
    [sg.Text("Portfolio link:"), sg.Input(key="LINK", do_not_clear=False)],
    [sg.Text('Please enter your skills below:')],
    [sg.Text("Option:1"), sg.Input(key="SKILL1", do_not_clear=False)],
    [sg.Text("Option:2"), sg.Input(key="SKILL2", do_not_clear=False)],
    
    
    
    [sg.Button("Create CV"), sg.Exit()],
]

window = sg.Window("CV Generator", layout, element_justification="right")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Create CV":
        # Add calculated fields to our dict
        #values["NONREFUNDABLE"] = round(float(values["AMOUNT"]) * 0.2, 2)
        #values["TODAY"] = today.strftime("%Y-%m-%d")
        #values["TODAY_IN_ONE_WEEK"] = today_in_one_week.strftime("%Y-%m-%d")

        # Render the template, save new word document & inform user
        doc.render(values)
        output_path = Path(__file__).parent / f"{values['DOCUMENTNAME']}-CV.docx"
        doc.save(output_path)
        sg.popup("File saved", f"File has been saved here: {output_path}")

window.close()