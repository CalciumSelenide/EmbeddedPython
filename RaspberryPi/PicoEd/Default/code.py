# 导入程序所需要的模块
import board
import digitalio
import time
from picoed import *
from picoed import display



led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
P_0 = digitalio.DigitalInOut(board.P0_A0)
P_1 = digitalio.DigitalInOut(board.P1_A1)
P_2 = digitalio.DigitalInOut(board.P2_A2)
P_3 = digitalio.DigitalInOut(board.P3_A3)
P_4 = digitalio.DigitalInOut(board.P4)
P_5 = digitalio.DigitalInOut(board.P5)
P_6 = digitalio.DigitalInOut(board.P6)
P_7 = digitalio.DigitalInOut(board.P7)
P_8=  digitalio.DigitalInOut(board.P8)
P_9 = digitalio.DigitalInOut(board.P9)
P_10 = digitalio.DigitalInOut(board.P10)
P_11 = digitalio.DigitalInOut(board.P11)
P_12 = digitalio.DigitalInOut(board.P12)
P_13 = digitalio.DigitalInOut(board.P13)
P_14 = digitalio.DigitalInOut(board.P14)
P_15 = digitalio.DigitalInOut(board.P15)
P_16 = digitalio.DigitalInOut(board.P16)

P_0.direction = digitalio.Direction.OUTPUT
P_1.direction = digitalio.Direction.OUTPUT
P_2.direction = digitalio.Direction.OUTPUT
P_3.direction = digitalio.Direction.OUTPUT
P_4.direction = digitalio.Direction.OUTPUT
P_5.direction = digitalio.Direction.OUTPUT
P_6.direction = digitalio.Direction.OUTPUT
P_7.direction = digitalio.Direction.OUTPUT
P_8.direction = digitalio.Direction.OUTPUT
P_9.direction = digitalio.Direction.OUTPUT
P_10.direction = digitalio.Direction.OUTPUT
P_11.direction = digitalio.Direction.OUTPUT
P_12.direction = digitalio.Direction.OUTPUT
P_13.direction = digitalio.Direction.OUTPUT
P_14.direction = digitalio.Direction.OUTPUT
P_15.direction = digitalio.Direction.OUTPUT
P_16.direction = digitalio.Direction.OUTPUT



display.clear()

while True:
  if button_a.is_pressed() and button_b.is_pressed():
      for x in range(display.width):
        for y in range(display.height):
          display.pixel(x, y, 20)
      if not i2c.try_lock():
        pass
      i2c.writeto(0x08,bytes([0x0A]))
      time.sleep(1)
      P_0.value = True
      i2c.writeto(0x08,bytes([0x00]))
      time.sleep(0.1)
      P_0.value = False
      
      P_1.value = True
      i2c.writeto(0x08,bytes([0x01]))
      time.sleep(0.1)
      P_1.value = False
      
      P_2.value = True
      i2c.writeto(0x08,bytes([0x02]))
      time.sleep(0.1)
      P_2.value = False
      P_2.value = False
      
      
      P_3.value = True
      i2c.writeto(0x08,bytes([0x03]))
      time.sleep(0.1)
      P_3.value = False
      
      P_4.value = True
      i2c.writeto(0x08,bytes([0x04]))
      time.sleep(0.1)
      P_4.value = False
      
      P_5.value = True
      i2c.writeto(0x08,bytes([0x05]))
      time.sleep(0.1)
      P_5.value = False
      
      P_6.value = True
      i2c.writeto(0x08,bytes([0x06]))
      time.sleep(0.1)
      P_6.value = False
      
      P_7.value = True
      i2c.writeto(0x08,bytes([0x07]))
      time.sleep(0.1)
      P_7.value = False
      
      P_8.value = True
      i2c.writeto(0x08,bytes([0x08]))
      time.sleep(0.1)
      P_8.value = False
      
      P_9.value = True
      i2c.writeto(0x08,bytes([0x09]))
      time.sleep(0.1)
      P_9.value = False
      
      P_10.value = True
      i2c.writeto(0x08,bytes([0x0A]))
      time.sleep(0.1)
      P_10.value = False
      
      P_11.value = True
      i2c.writeto(0x08,bytes([0x0B]))
      time.sleep(0.1)
      P_11.value = False
      
      P_12.value = True
      i2c.writeto(0x08,bytes([0x0C]))
      time.sleep(0.1)
      P_12.value = False
      
      P_13.value = True
      i2c.writeto(0x08,bytes([0x0D]))
      time.sleep(0.1)
      P_13.value = False
      
      P_14.value = True
      i2c.writeto(0x08,bytes([0x0E]))
      time.sleep(0.1)
      P_14.value = False
      
      P_15.value = True
      i2c.writeto(0x08,bytes([0x0F]))
      time.sleep(0.1)
      P_15.value = False
      
      P_16.value = True
      i2c.writeto(0x08,bytes([0x10]))
      time.sleep(0.1)
      P_16.value = False
      
      time.sleep(1)
      led.value = True
      i2c.writeto(0x08,bytes([0x11]))
      time.sleep(0.5)
      music.pitch(1000, 100)
      i2c.writeto(0x08,bytes([0x13]))
  else:
      pass







                    