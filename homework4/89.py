def ordinal_number(n):
    if n < 1 or n > 12:
        return ""
    ordinals = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }
    return ordinals[n]

if __name__ == "__main__":
    for i in range(1, 13):
        print(f"{i}: {ordinal_number(i)}")
