import pyautogui as pya
import time

time.sleep(3)
start = 0

end = 10

while start<=end:
    print(f"aku mengulang{start}")
    pya.press('enter')
    start = start+1