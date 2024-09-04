import urwid


def digit_check(password, score):
    score+=2 * any(digit.isdigit() for digit in password)
    return score

    
def letters_check(password, score):
    return any(word.isalpha()  for word in password)

    
def length_check(password, score):
    score+=2 * (len(password) > 12)
    return score


def lower_letters_check(password, score):
    return any(word.islower() for word in password)

    
def upper_letters_check(password, score):
    score+=2 * any(word.isupper() for word in password)
    return score
    
    
def symbols_check(password, score):
    score+=2 * any(not(sym.isalpha() or sym.isdigit() or '') for sym in password)
    return score
    
    
def on_ask_change(edit, new_edit_text):
    score = 0
    check = [upper_letters_check, length_check, digit_check, symbols_check]
    password = new_edit_text
    for c in check:
        score = c(password, score)
    reply.set_text("Рейтинг пароля: " + str(score))
        

if __name__ == "__main__":
    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
    

    
    