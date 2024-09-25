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