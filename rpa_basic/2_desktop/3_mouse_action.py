import pyautogui

# pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())

# pyautogui.click(66, 25, duration=1) # 1초 동안 (66, 25) 좌표로 이동 후 마우스 클릭
# pyautogui.mouseDown()
# pyautogui.mouseUp() # 이것도 마찬가지로 down up은 클릭임

# pyautogui.doubleClick()
# pyautogui.click(clicks=2) # 두번 클릭함

# pyautogui.moveTo(100, 100)
# pyautogui.mouseDown()
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp() # 마우스 뗀 상태
# pyautogui.sleep(3)
# pyautogui.rightClick()
# pyautogui.middleClick() # 마우스 휠

# print(pyautogui.position())
# pyautogui.moveTo()
# pyautogui.drag(100 ,0, duration=0.25) # 현재 위치 기준으로 x 100 만큼, y 0 만큼 드래그 
# pyautogui.dragTo(100, 0) # 절대 좌표 기준으로 드래그

pyautogui.sleep(3)
pyautogui.scroll(300) # 위 방향으로 300만큼 스크롤.
# -300 아래 방향으로 300만큼 스크롤