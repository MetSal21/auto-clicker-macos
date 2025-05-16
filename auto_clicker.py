import pyautogui
import time

print("Durdurmak için Ctrl+C veya pencereyi kapatın.")

try:
    while True:
        pyautogui.click()
        time.sleep(4)
except KeyboardInterrupt:
    print("\nİşlem sonlandırıldı.")
