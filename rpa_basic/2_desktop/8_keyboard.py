import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25)
# pyautogui.write("나도코딩") # 처음에는 한글 지원안돼

pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval=0.25)
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 2번, l a 순서대로 적고 enter 입력

# automate the boring stuff with python 홈페이지에서 keyboard관련 gui 정보를 더 얻을 수 있음 

# 특수 문자
pyautogui.keyDown("shift") # shift 키를 누른 상태에서
pyautogui.press("4") # 숫자 4를 입력하고
pyautogui.keyUp("shift") # shift 키를 뗀다

# 조합키 
pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a") # press("a")
pyautogui.keyUp("ctrl") # Ctrl + A

# 간편한 조합키

# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# Ctrl 누르고 > Alt 누르고 > Shift 누르고 > A 누르고 > A 떼고 > Shift 떼고 ...
pyautogui.hotkey("ctrl", "a")


import pyperclip
pyperclip.copy("나도코딩") # 나도코딩 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용을 붙여넣기