import time
import lcd16x2
import machine
#connect scl to pin 5 and sda to pin 4
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
devices=i2c.scan()
addr=63    #here 63 is the address of the lcd module
if addr in devices:    
  print("device found")
time.sleep(1)
lcd=lcd16x2.lcd(i2c,addr)
try:
	while True:
		print("writing to display")
		lcd.lcd_clear()
		lcd.lcd_display_string("hello world",1)
		lcd.lcd_display_string("working fine",2)
		time.sleep(5)
		print("Testing for clear screen")
		lcd.lcd_clear()
		time.sleep(2)
		lcd.lcd_display_string("hello Lokesh",1)
		lcd.lcd_display_string("I'm working",2)
		time.sleep(5)
except Exception as e:
	print("try failed")
