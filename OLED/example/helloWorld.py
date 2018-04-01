import machine
import time
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
addr = 60 
oledIsConnected = False
hSize       = 32  # height
wSize       = 128 # width
print('Scaning i2c bus...')
devices = i2c.scan()
if len(devices) == 0:
	print("No i2c device !")
else:
	print('i2c devices found:',len(devices))
	for device in devices: 
		if device == addr:
			oledIsConnected = True
		print(device)
if oledIsConnected:
	oled = ssd1306.SSD1306_I2C(wSize, hSize, i2c, addr)
	oled.fill(0)
     	oled.text("Hello", 0, 0)
    	oled.text("world", 0, 10)
     	oled.text("E> E>", 0, 20)
     	oled.show()
else:
	print('! No i2c display')
 	time.sleep_ms(5000)
