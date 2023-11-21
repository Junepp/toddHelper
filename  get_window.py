import pyautogui


getObj = pyautogui.getActiveWindow()

print(getObj.title)
print(getObj.size)
print(getObj.left, getObj.top, getObj.right, getObj.bottom)

