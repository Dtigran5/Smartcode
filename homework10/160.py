def check_ie_rule(word):
    if 'ie' in word:
        return True
    elif 'ei' in word:
        if word[word.index('ei') - 1] == 'c':
            return True
        else:
            return False
    return None

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            follow_rule = set()
            violate_rule = set()

            for line in file:
                words = line.split()
                for word in words:
                    if 'ie' in word or 'ei' in word:
                        result = check_ie_rule(word)
                        if result is True:
                            follow_rule.add(word)
                        elif result is False:
                            violate_rule.add(word)

            return follow_rule, violate_rule
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None, None
    except PermissionError:
        print(f"Error: Permission denied to access the file '{filename}'.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

def main():
    filename = input("Enter the filename containing the text: ")
    follow_rule, violate_rule = process_file(filename)
    
    if follow_rule is not None and violate_rule is not None:
        print(f"Words that follow the 'I before E except after C' rule: {follow_rule}")
        print(f"Words that violate the rule: {violate_rule}")
        print(f"Number of words that follow the rule: {len(follow_rule)}")
        print(f"Number of words that violate the rule: {len(violate_rule)}")

if __name__ == "__main__":
    main()
