import pyautogui as pya
import time

time.sleep(3)
start = 0

end = 10

while start<=end:
    print(f"contoh sederhana looping dengan python{start}")
    pya.press('enter')
    start = start+1
