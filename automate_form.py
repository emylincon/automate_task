from selenium import webdriver
from datetime import *
from time import gmtime, strftime
import random as random
from random import randrange
import time


def get_time():
    global d
    global s_ran_hour
    global s_ran_min
    global f_ran_min
    global f_ran_hour
    global t_time

    d = date.today()
    s_ran_hour = random.randint(8, 9)
    s_ran_min = randrange(60)
    f_ran_hour = random.randint(21, 23)
    f_ran_min = randrange(60)
    t_time = '{}:{}'.format(f_ran_hour, f_ran_min)
    _timer = datetime(d.year, d.month, d.day, f_ran_hour, f_ran_min)


def initialization():
    global driver

    driver = webdriver.Chrome(executable_path=r"C:\Program Files\chrome driver\chromedriver.exe")
    driver.get('https://goo.gl/forms/EW8UxiE56ACtYrS73')


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
    form = driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/content/span')

    student_id.send_keys('3331605')
    first_name.send_keys('Emeka')
    surname.send_keys('Ugwuanyi')
    office_no.send_keys('FW210')
    date_.send_keys('{}/{}/{}'.format(d.day, d.month, d.year))
    #date_.send_keys('04/04/2019')
    time_in_m.send_keys(s_ran_min)
    time_in_h.send_keys(s_ran_hour)
    time_out_h.send_keys(f_ran_hour)
    time_out_m.send_keys(f_ran_min)
    note.send_keys("Emeka's attendance")
    #form.click()


def main():
    try:
        while True:
            get_time()
            while True:
                time_now = datetime.now().strftime("%H:%M")
                if time_now == t_time:
                    attendance()
                    time.sleep(60)
                    break
    except KeyboardInterrupt:
        print('\nProgramme Terminated')


get_time()
attendance()