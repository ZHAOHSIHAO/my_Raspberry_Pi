import RPi.GPIO as GPIO

import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.IN)
# print('1')


def check():
    #p rint('2')
    GPIO.output(16, GPIO.HIGH)
    # GPIO.setup(16, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(16, GPIO.LOW)
    # print('5')
    while GPIO.input(12) == 0:
        # print('6')
        pass
    t1 = time.time()
    #print(t1)
    while GPIO.input(12) == 1:
        # print("7")
        pass
    t2 = time.time()
    #print(t2)
    distance = (t2-t1)*340/2
    #print("dis:{}".format(distance))
    return distance


try:
    #print('3')
    while True:
        #print('4')
        time.sleep(2)
        distance = check()
        print('Distance is {}'.format(distance))
except KeyboardInterrupt:
    GPIO.cleanup()
    print('键盘请求退出（Ctrl+C），IO口清理完毕')
 
