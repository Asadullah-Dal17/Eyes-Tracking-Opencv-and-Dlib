import serial  # pyserial moudule
import time
RED_value, GREEN_value, Blue_Value = 0, 0, 0  # default
# empty list for colors thold held
RGB_List = []

# Setting up Arduino in order to communicate with python
Arduino = serial.Serial(port="COM3", baudrate=9600)
time.sleep(1)  # proivding time to arduino to setup communcaiton

print("Enter RGB Value Like '0,255,0' min =0 and mx=255 or 'Exit' to quite the Program ")

while True:
    Input_String = input("R,G,B or Type 'Exit' to Quite the Program = ")
    # checking String contains Exit  then break the loop/ enventually the program
    if Input_String == "Exit" or Input_String == 'exit':
        data = "R0G0B0"
        # sending data to Arduino  and encoding
        Arduino.write(data.encode())
        # proivding time to Arduino and Python
        time.sleep(0.02)
        # clearing everything out on arudino side
        Arduino.flush()
        break
    # seperating the RGB vlaue, storing it into list
    RGB_List = Input_String.split(',')  # 0,255,0
    # checking list contians values or not
    if len(RGB_List) == 3:
        RED_value, GREEN_value, Blue_Value = RGB_List
        # formating the data in order to send to Arduino
        data = f"R{RED_value}G{GREEN_value}B{Blue_Value}"
        print(data)
        # sending data to Arduino  and encoding
        Arduino.write(data.encode())
        # proivding time to Arduino and Python
        time.sleep(0.02)
        # clearing everything out on arudino side
        Arduino.flush()
    else:
        print("Please Enter correct Value of RGB")
