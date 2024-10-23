import ServoControl
import time

if __name__ == '__main__': 
    while True:
        #ServoControl.setPWMServoMove(1, 500, 1000)
        #time.sleep(2)
        #ServoControl.setPWMServoMove(1, 2500, 1000)
        #time.sleep(2)

        servos = [10, 1000, 8, 2000]  # 舵机10: ID 10, 正转 (1000 us), 舵机8: ID 8, 反转 (2000 us)
        ServoControl.setPWMServoMoveByArray(servos, 2, 2000)

        time.sleep(2)  # Python中的等待2秒

        servos = [10, 1500, 8, 1500]  # 中位值1500表示停止
        ServoControl.setPWMServoMoveByArray(servos, 2, 0)
