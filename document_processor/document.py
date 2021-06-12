from cursor import Cursor


class Document:
    def __init__(self):
        self.cursor = Cursor(self)
        self.file_name = ""
        self.characters = []

    def insert(self, character):
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        with open(self.filename, "w") as f:
            f.write("".join(self.characters))


if __name__ == '__main__':
     d = Document()
     d.insert('h')
     d.insert('e')
     d.insert('l')
     d.insert('l')
     d.insert('o')
     d.insert('\n')
     d.insert('w')
     d.insert('o')
     d.insert('r')
     d.insert('l')
     d.insert('d')
     d.cursor.home()
     d.insert("*")
     print("".join(d.characters))