import sqlite3

class NoteService:
    def __init__(self, db_path='notes-organizer.sqlite'):
        self.db_path = db_path
    
    def _connect(self):
        return sqlite3.connect(self.db_path)
    
    def get_all_notes(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, description FROM notes')
        notes = cursor.fetchall()
        conn.close()
        return notes

    def add_note(self, data):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO notes (title, description) VALUES (?, ?)', (data['title'], data['description']))
        conn.commit()
        conn.close()

    def update_note(self, data):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('UPDATE notes SET title = ?, description = ? WHERE id =?', (data['title'], data['description'], data['id']))
        conn.commit()
        conn.close()
    
    def delete_note(self, id):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM notes WHERE id = ?', (id,))
        conn.commit()
        conn.close()