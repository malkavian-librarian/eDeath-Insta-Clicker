"""
I was pissed by my inability to delete Instagram posts in bulk effectively purging my data from the public space;
Yes, lots of it will be saved already somewhere, lots of it will be stored in Meta's servers anyway but giving the volume
of information out there, I am confident no one will notice once' disappearance.
This autoclicker removes pictures, one by one.
You need to have your Insta page open in your browser with a sim of Pixel 7 enabled for static and stable 
look (browser tool mobile simulation enabler for testing).
The waiting times serve 3 purposes:
- as Insta loads like hell, at times the program might start clicking on the button that didn't yet load; 
we need to wait here, sorry.
- the randomness increases the probability that Meta won't block your browser in some way, it happen to me a couple of 
times when I was playing with pyautogui (thanks Al!).
I removed everything I had, ~ 1300 posts
"""


import os
import random
import pyautogui
import time
from tqdm import tqdm

for num in tqdm(range(1000)):
    time.sleep(random.randint(5, 10))
    pyautogui.click(285,747+random.randint(1, 3))
    time.sleep(random.randint(3, 5))
    pyautogui.click(680+random.randint(1, 2),312+random.randint(1, 3))
    time.sleep(random.randint(2, 4))
    pyautogui.click(460+random.randint(1, 2),733+random.randint(1, 3))
    time.sleep(random.randint(1, 3))
    pyautogui.click(464+random.randint(1, 2),822+random.randint(1, 3))
    time.sleep(random.randint(1, 3))



   