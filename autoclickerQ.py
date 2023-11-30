import os
import random
import pyautogui
import time
from tqdm import tqdm

for num in tqdm(range(30)):
    time.sleep(random.randint(1, 10))
    pyautogui.click(305,740)
    time.sleep(random.randint(3, 5))
    pyautogui.click(684,324)
    time.sleep(random.randint(3, 5))
    pyautogui.click(467,552)
    time.sleep(random.randint(3, 5))
    pyautogui.click(491,648)
    time.sleep(random.randint(3, 5))
   