import time
def Timer():
    Time = int(input("Please Enter Time : "))
    for i in range(Time,0,-1):
        seconds = i%60
        minutes = int((i/60)%60)
        hours = int(i/3600)
        print(f"{hours}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    print("Time's Up !")
Timer()

