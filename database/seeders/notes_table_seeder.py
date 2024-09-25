import sqlite3

def seed_notes(conn):
    cursor = conn.cursor()
    
    # Sample data to insert into the notes table
    sample_notes = [
        ("Note 1", "This is the description for note 1."),
        ("Note 2", "This is the description for note 2."),
        ("Note 3", "This is the description for note 3."),
        ("Note 4", "This is the description for note 4."),
        ("Note 5", "This is the description for note 5.")
    ]
    
    # Insert sample data into the notes table
    cursor.executemany('''
    INSERT INTO notes (title, description) VALUES (?, ?)
    ''', sample_notes)
    
    conn.commit()

if __name__ == "__main__":
    # Connect to the SQLite database
    conn = sqlite3.connect('notes-organizer.sqlite')
    
    # Seed the notes table
    seed_notes(conn)
    
    # Close the connection
    conn.close()