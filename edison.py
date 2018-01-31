import mraa
import pyupm_i2clcd
import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer
import pyupm_ldt0028 as ldt0028
import pyupm_mic as upmMicrophone
import time
import twilo

from thread import *

class Edison(object):

  
  def __init__(self):
    # Create the LDT0-028 Piezo Vibration Sensor object using AIO pin 0
    self.piezo = ldt0028.LDT0028(0)
    
    # Create the light sensor object using AIO pin 1
    self.light = grove.GroveLight(1)
    
    #led on D5
    self.led = mraa.Gpio(5)
    self.led.dir(mraa.DIR_OUT)
    
    self.mic = upmMicrophone.Microphone(2)
    self.threshContext = upmMicrophone.thresholdContext()
    self.threshContext.averageReading = 0
    self.threshContext.runningAverage = 0
    self.threshContext.averagedOver = 2
    

  def getLoudness(self):
    buffer = upmMicrophone.uint16Array(128)
    len = self.mic.getSampledWindow(2, 128, buffer)
    thresh = 0
    if len:
      thresh = self.mic.findThreshold(self.threshContext, 30, buffer, len)
      self.mic.printGraph(self.threshContext)
    return thresh

  def getBrightness(self):
    return self.light.value()

  def getVibration(self):
    return self.piezo.getSample()    
    
  def isParty(self):
    loudness = self.getLoudness()
    brightness = self.getBrightness()
    vibration = self.getVibration()
    isactive = 0
    if (loudness > 70 and brightness > 50 and vibration > 15):    
        self.led.write(True)
        twilo.send_massage()
        isactive = 1
    else:
        isactive = 0
    return isactive
       