import sqlite3
import os

# Connect to the SQLite database
conn = sqlite3.connect('notes-organizer.sqlite')

# Create a table to keep track of applied migrations
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS migrations (
    id INTEGER PRIMARY KEY,
    migration TEXT NOT NULL,
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

# Get the list of applied migrations
cursor.execute('SELECT migration FROM migrations')
applied_migrations = set(row[0] for row in cursor.fetchall())

# Get the list of migration files
migration_files = sorted(f for f in os.listdir('database/migrations') if f.endswith('.py'))

# Apply pending migrations
for migration_file in migration_files:
    if migration_file not in applied_migrations:
        print(f'Applying {migration_file}...')
        migration_module = __import__(f'database.migrations.{migration_file[:-3]}', fromlist=['migrate'])
        migration_module.migrate(conn)
        cursor.execute('INSERT INTO migrations (migration) VALUES (?)', (migration_file,))
        conn.commit()
        print(f'{migration_file} applied.')

# Close the connection
conn.close()