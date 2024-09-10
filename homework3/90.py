def display_verse(verse_number):
    gifts = [
        "A partridge in a pear tree.",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five golden rings,",
        "Six geese a-laying,",
        "Seven swans a-swimming,",
        "Eight maids a-milking,",
        "Nine ladies dancing,",
        "Ten lords a-leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,"
    ]
    
    print(f"On the {['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'][verse_number - 1]} day of Christmas")
    print("my true love sent to me:")
    
    for i in range(verse_number, 0, -1):
        if i == 1 and verse_number != 1:
            print("And " + gifts[i - 1])
        else:
            print(gifts[i - 1])

for day in range(1, 13):
    display_verse(day)
    print() 
