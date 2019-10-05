from selenium import webdriver
from datetime import *
from time import gmtime, strftime
import random as random
from random import randrange
import time
import smtplib
import calendar
import config


def _day():
    x = calendar.day_name[d.weekday()]
    return x.lower()


def get_time():
    global d
    global s_ran_hour
    global s_ran_min
    global f_ran_min
    global f_ran_hour
    global t_time
    global _timer

    d = date.today()
    s_ran_hour = random.randint(8, 9)
    s_ran_min = randrange(10, 59)
    f_ran_hour = random.randint(21, 23)
    f_ran_min = randrange(10, 59)
    t_time = '{}:{}'.format(f_ran_hour, f_ran_min)
    _timer = datetime(d.year, d.month, d.day, f_ran_hour, f_ran_min).strftime("%d/%m/%y %H:%M")


def initialization():
    global driver

    driver = webdriver.Chrome(executable_path=r"C:\Program Files\chrome driver\chromedriver.exe")
    driver.get('https://goo.gl/forms/EW8UxiE56ACtYrS73')


def send_email():
    global msg
    try:
        # server = smtplib.SMTP('smtp.gmail.com:587')
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        # server.starttls()
        server.login(config.email_address, config.password)
        subject = 'Attendance form'
        msg = 'Attendance done for {}'.format(_timer)
        message = 'Subject: {}\n\n{}\n\n SENT BY RIHANNA \n\n'.format(subject, msg)
        server.sendmail(config.email_address, config.send_email, message)
        server.quit()
        print("Email sent!")
    except Exception as e:
        print(e)


def attendance():
    initialization()
    xpath_id = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input'
    student_id = driver.find_element_by_xpath(xpath_id)
    first_name = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
    surname = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input')
    office_no = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input')
    date_ = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div/div[2]/div[1]/div/div[1]/input')
    time_in_h = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input')
    time_in_m = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[2]/div[3]/div/div[1]/div/div[1]/input')
    #time_in_ap = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[2]/div[4]/div[1]/div[1]/div[1]/content')
    time_out_h = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input')
    time_out_m = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div/div[2]/div[3]/div/div[1]/div/div[1]/input')
    #time_out_ap = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div/div[2]/div[4]/div[1]/div[1]/div[1]')
    note = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[8]/div/div[2]/div/div[1]/div/div[1]/input')
    form = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/span/span')

    student_id.send_keys('3331605')
    first_name.send_keys('Emeka')
    surname.send_keys('Ugwuanyi')
    office_no.send_keys('FW210')

    if len(str(d.day)) == 2:
        day = d.day
    else:
        day = f"0{d.day}"
    if len(str(d.month)) == 2:
        month = d.month
    else:
        month = f"0{d.month}"
    date = f"{day}/{month}/{d.year}"
    date_.send_keys(date)

    time_in_m.send_keys(s_ran_min)
    time_in_h.send_keys(s_ran_hour)
    time_out_h.send_keys(f_ran_hour)
    time_out_m.send_keys(f_ran_min)
    note.send_keys("Emeka's attendance")
    form.click()
    time.sleep(2)
    driver.close()


def main():
    try:
        while True:
            print('--------------------------------------------')
            print("Running Emeka's Script, Please do not close")
            print('--------------------------------------------')
            print('Program is active...')
            get_time()
            print('Next attendance will be automated at {}'.format(t_time))
            while True:
                time_now = datetime.now().strftime("%H:%M")
                if time_now == t_time:
                    attendance()
                    send_email()
                    print(msg)
                    print('Program is Sleeping for 20 hours')
                    print('--------------------------------------------\n')
                    if _day() == 'saturday':
                        print('Program next active on Monday')
                        slp = 60*60*24
                        time.sleep(slp)

                    sleep = 60*60*20
                    time.sleep(sleep)
                    break
                else:
                    time.sleep(50)
    except KeyboardInterrupt:
        print('\nProgramme Terminated')


if __name__ == "__main__":
    main()

