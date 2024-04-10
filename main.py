from pptx import Presentation
from itertools import groupby
import json

list_of_notes = []
list_of_notes_address = []

class parser:
    def get_notes(ppt):
        for slide in ppt.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        note_address = run.hyperlink.address
                        if (note_address != None):
                            list_of_notes_address.append(note_address)
                        else:
                            continue
        new_list_of_notes_address = [el for el, _ in groupby(list_of_notes_address)]
        #print(new_list_of_notes_address)

        notes = []
        for page, slide in enumerate(ppt.slides):
            temp = []
            for shape in slide.shapes:
                if shape.has_text_frame and shape.text.strip():
                    temp.append(shape.text)
            notes.append(temp)
        #print(notes)

        for i in range(0, max(len(new_list_of_notes_address), len(notes))):
            if i < len(new_list_of_notes_address):
                list_of_notes.append(new_list_of_notes_address[i])
            if i < len(notes):
                list_of_notes.append(notes[i])
        print(list_of_notes)
        return list_of_notes

    def save_to_json():
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(list_of_notes, file, ensure_ascii=False, indent=4)

    def get_pres_name():
        print('Enter the name of your presentation: ')


parser.get_pres_name()
presentation_name = input()
presentation = Presentation(presentation_name + '.pptx')

parser.get_notes(presentation)
parser.save_to_json()

