import os
import pyautogui
import time

for num in range(1):
    time.sleep(2)
    print(pyautogui.position())
    print(f"starting removal of the post #{num}")
    pyautogui.click(719,835)
    time.sleep(1)
    pyautogui.click(1645,190)
    time.sleep(1)
    pyautogui.click(974,399)
    time.sleep(1)
    pyautogui.click(1017,602)
    time.sleep(1)
    print(f"your post #{num} has been removed")

   