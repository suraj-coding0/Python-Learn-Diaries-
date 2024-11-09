from plyer import notification
import time

if __name__=="__main__":
    while True:
        notification.notify(title ='Please drink water',app_name="Drinking water" ,message='Please Drink Water And Maintain Your Health',timeout=5 )
        time.sleep(7200)
