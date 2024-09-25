from services.note_service import NoteService

note_service = NoteService()

notes = note_service.get_all_notes()
for note in notes:
    print(note)