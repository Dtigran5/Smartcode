#link -> https://www.codewars.com/kata/62ad72443809a4006998218a
def like_or_dislike(buttons):
    state = "Nothing"
    
    for button in buttons:
        if button == "Like":
            if state == "Like":
                state = "Nothing"
            else:
                state = "Like"
        elif button == "Dislike":
            if state == "Dislike":
                state = "Nothing"
            else:
                state = "Dislike"
    
    return state

print(like_or_dislike(["Dislike"]))  
print(like_or_dislike(["Like", "Like"]))  
print(like_or_dislike(["Dislike", "Like"]))  
print(like_or_dislike(["Like", "Dislike", "Dislike"]))  