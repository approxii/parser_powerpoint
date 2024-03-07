from pptx import Presentation
import json
from urllib.parse import unquote

list_of_notes = []

def get_notes(ppt):
    for slide in ppt.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    note_address = run.hyperlink.address
                    note_text = run.text
                    if note_address != None:
                        note = unquote(note_address) + ':' + ' ' + "\"" + note_text +  "\""
                    else:
                        continue
                    list_of_notes.append(note)
                    #print(note_text)
                    #print(note_address)
                    print(list_of_notes)
                    print(note)
    return list_of_notes

def save_to_json():
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(list_of_notes, file, ensure_ascii=False, indent=4)

print('Enter the name of your presentation: ')
presentation_name = input()
presentation = Presentation(presentation_name + '.pptx')

get_notes(presentation)
print(list_of_notes)
save_to_json()

