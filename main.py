from pptx import Presentation
import json
from urllib.parse import unquote

list_of_notes = []

class parser:
    def get_notes(ppt):
        for slide in ppt.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for paragraph in shape.text_frame.paragraphs:
                    somde_str = str()
                    for run in paragraph.runs:
                        note_address = run.hyperlink.address
                        somde_str += run.text
                        if note_address != None:
                            note = unquote(note_address) + ':' + ' ' + '"' + somde_str +  '"'
                        else:
                            continue
                        list_of_notes.append(note)
                        for i in range(1,len(list_of_notes)):
                            if list_of_notes[i] == list_of_notes[i - 1]:
                                list_of_notes.remove(i)
                        print(note)
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
print(list_of_notes)
parser.save_to_json()

