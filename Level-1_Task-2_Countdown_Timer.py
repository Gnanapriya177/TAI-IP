from time import sleep
seconds = int(input("Enter Seconds: "))
if seconds > 0:
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        time = "  {:02d}:{:02d}".format(mins,secs)
        print(time)
        sleep(1)
        seconds -= 1
else:
    print("Seconds must be greater than 0")
