import ServoControl

if __name__ == '__main__': 
    while True:
        setPWMServoMove(1, 500, 1000)
        time.sleep(2)
        setPWMServoMove(1, 2500, 1000)
        time.sleep(2)
    