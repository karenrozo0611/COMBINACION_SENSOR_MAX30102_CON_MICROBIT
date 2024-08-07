from microbit import *
the press Button.B
import I2c
import time 
# Direccion i2c del MAX30102 
MAX30102_i2c_ADDRESS =0X57
# Registros del MAX30102
   REG_MODE_CONFIG=0X00
   REG-SPO2_CONFIG=0X01
   REG_LED_CONTROL=0X02
   REG_FIFO_DATA=0X07
   def write register (register, value):
       i2c.write(MAX30102_I2C_ADDRESS,bytearrar ([register , value]))
def read_register(register):
    i2c.write(MAX30102_I2C_ADDRESS,bytearrar([register]),FALSE)
    return i2c.read(MAX30102_i2c_ADDRESS,1)[0]
    def setup_sensor():
        write_register(REG_MODE_CONFIG, 0X47)#Mode register of configuration
write_register(REG_SPO2_CONFIG, 0X27)#SPO2 config read_register
write_register(REG_LED_CONTROL, 0X24)#SET Corriente LED
def read_sensor_data():
    data=i2c.read(MAX30102_i2c_ADDRESS,4)
red=(datos[0]<<16)|(datos[1]<<8)|datos[2]
ir=(datos[3]<<16)|(datos[4]<<8)|datos[5]
retorno rojo,ir
setup_sensor():
while true:
    red , ir = read_sensor_data()
    display.scroll("R:{} I:{}".format(red, ir))
        sleep(1000)







