import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 (VSCode)
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보 
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보


# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기

# for w in pyautogui.getWindowsWithTitle("어무니~, 아빠"):
    # print(w)
w = pyautogui.getWindowsWithTitle("어무니~, 아빠")[0]
print(w)
if w.isActive == False:
    w.activate() # 활성화 (맨 앞으로 가져오기)

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize() # 최대화

if w.isMinimized == False:
    w.minimize() # 최소화

w.restore() # 화면 원복

w.close() # 윈도우 닫기