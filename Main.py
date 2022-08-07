if __name__ == '__main__':
    while True:
        choose = int(input('''\nHello! What do you want?
1. Set Alarm
2. Show weather now
3. Convert currency
4. Draw function\n'''))
        if choose == 1:
            import Alarm
        elif choose == 2:
            import Weather
        elif choose == 3:
            import Converter
        elif choose == 4:
            import Functions
