from gpiozero import Button, LED
from core.models import ButtonSample
import time


def read_btn():
    print("Reading button")
    btn = Button(4)
    sample = ButtonSample()
    sample.value=btn.is_pressed
    sample.save()
    
    
