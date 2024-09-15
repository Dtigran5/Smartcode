def killer(suspect_info, dead):
    for suspect, seen in suspects.items():
        if all(person in seen for person in dead_people):
            return suspect

suspects = {
    'James': ['Jacob', 'Bill', 'Lucas'],
    'Johnny': ['David', 'Kyle', 'Lucas'],
    'Peter': ['Lucy', 'Kyle']
}

dead_people = ['Lucas', 'Bill']
killer = killer(suspects, dead_people)
print(killer)

