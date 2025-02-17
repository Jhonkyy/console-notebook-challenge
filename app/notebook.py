# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime

class Note:

    HIGH: str = 'HIGH'
    MEDIUM:str = 'MEDIUM'
    LOW: str = 'LOW'

    def __init__(self, code: str, title: str, text: str, importance: str):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date : datetime = datetime.now()
        self.tags: list[str] = []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"


class Notebook:
    def __init__(self):
        self.notes: list[Note] = []

    def add_note(self, title: str, text: str, importance: str) -> Note:
        new_code = len(self.notes)
        while new_code not in self.notes:
            new_code += 1
        new_note = Note(new_code, title, text, importance)
        self.notes.append(new_note)
        return new_note

    def delete_note(self, code: int):
        for i, note in enumerate(self.notes):
            if note.code == code:
                del self.notes[i]
                break
