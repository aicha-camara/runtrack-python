def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note >= 40 and note % 5 >= 3:
            note = (note // 5 + 1) * 5

        notes_arrondies.append(note)

    return notes_arrondies

notes_etudiants = input("Entrez les notes initiales séparées par des virgules : ")
notes_etudiants = [int(note) for note in notes_etudiants.split(',')]
notes_arrondies = arrondir_notes(notes_etudiants)

print("Notes initiales:", notes_etudiants)
print("Notes arrondies:", notes_arrondies)