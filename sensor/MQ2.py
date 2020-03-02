import RPi.GPIO as GPIO
import time

MQ = 40

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MQ, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

def detect():
    while 1:
        status = GPIO.input(MQ)
        if status == True:
            print("环境正常")
        else:
            print("检测到危险气体！")
        time.sleep(0.5)

try:
    detect()
except KeyboardInterrupt:
    GPIO.cleanup()
    print('键盘请求退出（Ctrl+C），IO口清理完毕')
