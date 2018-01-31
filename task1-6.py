import mraa
import pyupm_i2clcd
import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer
import time

#redlight on port D8
#self.redLightState = 0
#self.redLight = mraa.Gpio(8)
#self.redLight.dir(mraa.DIR_OUT)

#lcd on i2c
lcd = pyupm_i2clcd.Jhd1313m1(6, 0x3E, 0x62)
lcd.clear()
lcd.setColor(50, 50, 255)
lcd.setCursor(0, 0)
lcd.write("Hello!")  
time.sleep(1)
lcd.write("ck!")    
time.sleep(1)
 

