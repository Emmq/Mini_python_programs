from playsound import playsound
import time


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
def alarm(seconds):
    time_elapse = 0

    print(CLEAR)
    while time_elapse < seconds:
        time.sleep(1)
        time_elapse += 1 

        time_left = seconds - time_elapse
        minit_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minit_left:02d}:{seconds_left:02d}")

    playsound("alarm.wav")

minit = int(input("enter alarm mini: "))
seconds = int(input("enter alarm seconds: "))
total_time = minit * 60 + seconds

alarm(total_time)

