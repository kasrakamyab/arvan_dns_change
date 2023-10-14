from funcs import watch, change
while True:
    print(""">please print
watch - for only watching your dns records
change - for changing you whole dns records
exit - for exit from the app""")
    order = input("> ")
    if order.lower() == "exit":
        print("farewell")
        break
    elif order.lower() == "watch":
        watch.watch()
        print("that's your whole dns records")
        print("*" * 50)
    elif order.lower() == "change":
        change.change()
        print("every thing has been changed")
    else:
        print("print correct value please")
