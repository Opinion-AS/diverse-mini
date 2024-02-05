
import pyautogui
import time


alt_texts = ["4c92ddb9-2aa7-46d9-ab6d-0c6cd1548b3e", "58ad5a18-448f-4db3-be17-e88ed5cf2420"] # GUID

for i in alt_texts:
    pyautogui.moveTo(x=994, y=457) # Plott
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.moveTo(x=1577, y=616) # Tekstboks
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.write(i)
    pyautogui.moveTo(x=424, y=935) # Footer
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.moveTo(x=1577, y=616) # Tekstboks
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.write(f"Footer: {i}")
    pyautogui.moveTo(x=1123, y=920) # Title 
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.moveTo(x=1577, y=616) # Tekstboks
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.write(f"Title: {i}")
    pyautogui.moveTo(x=1013, y=344) # Header
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.moveTo(x=1577, y=616) # Tekstboks
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.write(f"Title: {i}")
    pyautogui.moveTo(x=1439, y=542)
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.press("pagedown") # Neste
 
