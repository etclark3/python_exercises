def is_vowel(v):
    if v in ['a','e','i','o','u'] or v in ['A','E','I','O','U']:
        return True
    else: 
        return False

def calculate_tip(check,tip):
    x = check
    y = tip
    return x * y

def get_letter_grade(what):
    if what >= 90:
        return 'A'
    elif what >= 80:
        return 'B'
    elif what >= 70:
        return 'C'
    else:
        return 'F'