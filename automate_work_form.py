from selenium import webdriver
from datetime import *
import calendar
import schedule
import time
import config
import smtplib


__author__ = 'Emmanuel'

d = date.today()


def _day():
    x = calendar.day_name[d.weekday()]
    return x.lower()


def initialization():
    global driver

    driver = webdriver.Chrome(executable_path=r"C:\Program Files\chrome driver\chromedriver.exe")
    driver.get('https://mypayments.lsbu.ac.uk/vts/')
    username = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldUserName"]')
    password = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldPwd"]')
    login = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_cmdBar"]/div/div/div/ul/li[1]/a/span/span/span/span')

    username.send_keys('ugwuane3')
    password.send_keys(passwd)

    login.click()

    submit_claims = driver.find_element_by_xpath(xpath='//*[@id="ctl00_VTSMnu"]/ul/li[7]/a/span')
    submit_claims.click()


def francis():
    day = _day()
    initialization()
    select_CMIT = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstSess_ctl00__0"]').click()
    select_OK = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    select_OK.click()

    add_hours = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a').click()

    work_date = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldWorkDte_dateInput"]')

    start_time = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldStTime"]')

    finish_time = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldEnTime"]')

    hours_worked = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldActHours"]')

    sick_hours = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldSickHours"]')

    comment = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldComment"]')

    # add_hours_CMIT = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span').click()
    work_date.send_keys('{}\{}\{}'.format(d.day, d.month, d.year))
    #work_date.send_keys('{}\{}\{}'.format(28, 3, 2019))
    if day == 'tuesday':
        start_time.send_keys('14:00')
        finish_time.send_keys('16:00')
        comment.send_keys('Management Concepts and Evaluation Techniques 1')
    elif day == 'thursday':
        start_time.send_keys('11:00')
        finish_time.send_keys('13:00')
        comment.send_keys('Management Concepts and Evaluation Techniques 2')
    hours_worked.send_keys('2')
    sick_hours.send_keys('0')
    okay = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    okay.click()
    driver.close()
    send_email('Management Concepts and Evaluation Techniques')


def lucia():
    initialization()
    select_MIP = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstSess_ctl00__1"]').click()
    select_OK = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    select_OK.click()

    add_hours = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a').click()

    work_date = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldWorkDte_dateInput"]')

    start_time = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldStTime"]')

    finish_time = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldEnTime"]')

    hours_worked = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldActHours"]')

    sick_hours = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldSickHours"]')

    comment = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldComment"]')
    work_date.send_keys('{}\{}\{}'.format(d.day, d.month, d.year))
    #work_date.send_keys('{}\{}\{}'.format(25, 3, 2019))
    start_time.send_keys('10:00')
    finish_time.send_keys('13:00')
    hours_worked.send_keys('3')
    sick_hours.send_keys('0')
    comment.send_keys('ICT Project Management in Practice')
    okay = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    okay.click()
    driver.close()
    send_email('ICT Project Management in Practice')


def lucia_prepare():
    initialization()
    select_MIP = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstSess_ctl00__1"]').click()
    select_OK = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    select_OK.click()

    add_hours = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a').click()

    work_date = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldWorkDte_dateInput"]')

    start_time = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldStTime"]')

    finish_time = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldEnTime"]')

    hours_worked = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldActHours"]')

    sick_hours = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldSickHours"]')

    comment = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldComment"]')
    work_date.send_keys('{}\{}\{}'.format(d.day, d.month, d.year))
    start_time.send_keys('18:00')
    finish_time.send_keys('19:00')
    hours_worked.send_keys('1')
    sick_hours.send_keys('0')
    comment.send_keys('Preparation: ICT Project Management in Practice')
    okay = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    okay.click()
    driver.close()
    send_email('Preparation: ICT Project Management in Practice')


def iot():
    initialization()
    select_iot = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstSess_ctl00__2"]').click()
    select_OK = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    select_OK.click()

    add_hours = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a').click()

    work_date = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldWorkDte_dateInput"]')

    start_time = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldStTime"]')

    finish_time = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldEnTime"]')

    hours_worked = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldActHours"]')

    sick_hours = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldSickHours"]')

    comment = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_fldComment"]')
    work_date.send_keys('{}\{}\{}'.format(d.day, d.month, d.year))
    #work_date.send_keys('{}\{}\{}'.format(28, 3, 2019))
    start_time.send_keys('16:00')
    finish_time.send_keys('18:00')
    hours_worked.send_keys('2')
    sick_hours.send_keys('0')
    comment.send_keys('Embedded Systems and Internet of things')
    okay = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    okay.click()
    driver.close()
    send_email('Embedded Systems and Internet of things')


def send_email(module):
    global msg
    try:
        # server = smtplib.SMTP('smtp.gmail.com:587')
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        # server.starttls()
        server.login(config.email_address, config.password)
        subject = 'Work form'
        msg = 'Work form done for {}'.format(module)
        message = 'Subject: {}\n\n{}\n\n SENT BY RIHANNA \n\n'.format(subject, msg)
        server.sendmail(config.email_address, config.send_email, message)
        server.quit()
        print("Email sent!")
    except Exception as e:
        print(e)
#francis(_day().lower())
#francis('tuesday')
#lucia()
#lucia_prepare()
#iot()


def main():
    global passwd

    passwd = config.passwd
    print('--------------------------------------------')
    print("Running Emeka's Script, Please do not close")
    print('--------------------------------------------')
    print('Program is active...')
    schedule.every().tuesday.at("18:30").do(francis)
    schedule.every().wednesday.at("15:00").do(lucia)
    schedule.every().wednesday.at("15:10").do(lucia_prepare)
    schedule.every().thursday.at("14:00").do(francis)
    schedule.every().thursday.at("19:00").do(iot)
    while True:
        schedule.run_pending()
        time.sleep(50)


if __name__ == "__main__":
    main()
