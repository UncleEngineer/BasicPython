#copybot.py

import pyautogui as pg
import time

################## LINE 1 ###################
#-ใช้เมาส์คลิกไปยังตำแหน่งที่ต้องการก็อปปี้ (ด้านหน้า)
# x=1046, y=266
time.sleep(1) # รอ 1 วินาที
start_point = (1046,266)
pg.click(start_point)

#-ลากไปให้สุดบรรทัด
time.sleep(1)
end_point = (1400,266)
pg.dragTo(end_point, duration=2)

#-กดปุ่ม Ctrl + C เพื่อก็อปปี้
pg.hotkey('ctrl','c')
#-ขยับเมาส์ไปทางด้านซ้าย
left_notepad = (800,266)
pg.click(left_notepad)
#-กด Ctrl + V เพื่อวาง แล้วกด Enter
pg.hotkey('ctrl','v')
pg.press('enter')


################## LINE 2 ###################
#-ใช้เมาส์คลิกไปยังตำแหน่งที่ต้องการก็อปปี้ (ด้านหน้า)
# x=1046, y=266
time.sleep(1) # รอ 1 วินาที
start_point = (1046,308) # 266 + 42
pg.click(start_point)

#-ลากไปให้สุดบรรทัด
time.sleep(1)
end_point = (1400,308)
pg.dragTo(end_point, duration=2)

#-กดปุ่ม Ctrl + C เพื่อก็อปปี้
pg.hotkey('ctrl','c')
#-ขยับเมาส์ไปทางด้านซ้าย
left_notepad = (800,266)
pg.click(left_notepad)

### ********
pg.press('down')

#-กด Ctrl + V เพื่อวาง แล้วกด Enter
pg.hotkey('ctrl','v')
pg.press('enter')

################## LINE 3 ###################
#-ใช้เมาส์คลิกไปยังตำแหน่งที่ต้องการก็อปปี้ (ด้านหน้า)
# x=1046, y=266
time.sleep(1) # รอ 1 วินาที
start_point = (1046,350) # 308 + 42 (42 pixel คือ ระยะระหว่างบรรทัด)
pg.click(start_point)

#-ลากไปให้สุดบรรทัด
time.sleep(1)
end_point = (1400,350)
pg.dragTo(end_point, duration=2)

#-กดปุ่ม Ctrl + C เพื่อก็อปปี้
pg.hotkey('ctrl','c')
#-ขยับเมาส์ไปทางด้านซ้าย
left_notepad = (800,266)
pg.click(left_notepad)

### ********
pg.press('down')
pg.press('down')

#-กด Ctrl + V เพื่อวาง แล้วกด Enter
pg.hotkey('ctrl','v')
pg.press('enter')
