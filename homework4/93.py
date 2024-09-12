def center_string(s, w):
    if len(s) >= w:
        return s
    else:
        spaces = (w - len(s)) // 2
        return ' ' * spaces + s

if __name__ == "__main__":
    strings = ["Hello, World!", "Python Programming", "Center Me!", "Short"]
    window_width = 30
    
    for string in strings:
        centered_string = center_string(string, window_width)
        print(centered_string)
