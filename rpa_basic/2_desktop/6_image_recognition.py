import pyautogui
file_menu = pyautogui.locateOnScreen("file_menu.png") # 이미지가 있는 위치를 알려줌. 
print(file_menu)
pyautogui.click(file_menu)

for i in pyautogui.locateAllOnScreen("check.png"):
    print(i)
    pyautogui.click(i, duration=0.25)
## 똑같은 그림이 몇 개가 있으면 순서대로 눌러줌
# locateOnScreen은 하나만 찾아도 끝남 

# 속도 개선
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)

# 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(x, y, width, height))
run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.999)
pyautogui.moveTo(run_btn)