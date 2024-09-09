import pyautogui
# 스크린 샷 찍기
img = pyautogui.screenshot()
img.save("screenshot.png") # 스크린 샷 파일로 저장

pixel = pyautogui.pixel(28, 18)
print(pixel)

# print(pyautogui.pixelMatchesColor(28, 18, (36, 171, 242))) # RGB 값이 다른지 같은지를 알려줌 