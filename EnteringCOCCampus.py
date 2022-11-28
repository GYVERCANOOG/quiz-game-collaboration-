uniform=input("""Welcome to COC campus!
Did you wear your school uniform?
[Y] [N]
>>> """).lower()
if uniform=='y':
    a=input("""What shift are you?
[A] Shift A
[B] Shift B
[C] Shift C
>>> """).lower()
    if a == 'a':
        aa=input("What day is today?\n>>> ").lower()
        if aa == 'monday' or aa == 'tuesday':
            print("You can enter the campus.")
        elif aa == 'wednesday':
            wash=input("Do you wear your washing day polo?\n[Y] [N]\n>>> ").lower()
            if wash == 'y':
                print("You can enter the campus.")
            elif wash == 'n':
                nowash=input("Do you wear a proper uniform?\n[Y] [N]\n>>> ").lower()
                if nowash == 'y':
                    print("You can enter the campus.")
                else:
                    print("Sorry, you can't enter the campus.")
        else:
            print("It is not your designated shift!")
    elif a == 'b':
        ab=input("What day is today?\n>>> ").lower()
        if ab == 'thursday' or ab == 'friday' or ab == 'saturday':
            print("You can enter the campus.")
        else:
            print("It is not your designated shift!")
    elif a == 'c':
        ac = input("What day is today?").lower()
        if ac == 'sunday' or ac == 'monday' or ac == 'tuesday':
            print("You can enter the campus.")
        else:
            print("It is not your designated shift!")
    else:
        print("You cannot enter the campus.")
else:
    print("You cannot enter the campus.")
