
import pyautogui

alt_texts = ["a7696d72-913e-4b57-8898-9add7fe5f18e", "7f072cfa-d53e-46c0-bdd7-e45efd56fc93"] # GUID

for i in alt_texts:
    pyautogui.moveTo(x=897, y=525) # Plott
    pyautogui.click()
    pyautogui.moveTo(x=1577, y=616) # Tekstboks
    pyautogui.click()
    pyautogui.write(i)
    pyautogui.moveTo(x=424, y=946) # Footer
    pyautogui.click()
    pyautogui.moveTo(x=1577, y=616) # Tekstboks
    pyautogui.click()
    pyautogui.write(f"Footer: {i}")
    pyautogui.moveTo(x=599, y=934) # Title 
    pyautogui.click()
    pyautogui.moveTo(x=1577, y=616) # Tekstboks
    pyautogui.click()
    pyautogui.write(f"Title: {i}")
    pyautogui.moveTo(x=1013, y=444) # Header
    pyautogui.click()
    pyautogui.moveTo(x=1577, y=616) # Tekstboks
    pyautogui.click()
    pyautogui.write(f"Title: {i}")
    pyautogui.moveTo(x=1116, y=608)
    pyautogui.click()
    pyautogui.press("pagedown") # Neste
