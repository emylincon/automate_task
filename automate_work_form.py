from selenium import webdriver
from datetime import *
import calendar
import schedule
import time
import config
import smtplib

# improving the project deadlock
__author__ = 'Emmanuel'
passwd = config.passwd
d = date.today()


def _day():
    x = calendar.day_name[d.weekday()]
    return x.lower()


def get_time():
    _time = str(datetime.now()).split(' ')[1]


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


def fcs():
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
    if datetime.now().hour == 11:
        start_time.send_keys('09:00')
        finish_time.send_keys('11:00')
        comment.send_keys('Fundamentals of Computer Science')
        hours_worked.send_keys('2')
    elif datetime.now().hour == 18:
        start_time.send_keys('17:00')
        finish_time.send_keys('18:00')

        hours_worked.send_keys('1')
    else:
        start_time.send_keys(input("Enter Start Time: "))
        finish_time.send_keys(input("Enter Finish Time: "))
        hours_worked.send_keys(input("Hours Worked: "))

    comment.send_keys('Fundamentals of Computer Science')
    sick_hours.send_keys('0')
    okay = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    okay.click()
    driver.close()
    send_email('Fundamentals of Computer Science')
    print('\nFundamentals of Computer Science')


def fsd():
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

    if datetime.now().hour == 11:
        start_time.send_keys('12:00')
        finish_time.send_keys('14:00')
        hours_worked.send_keys('2')
    elif datetime.now().hour == 18:
        start_time.send_keys('16:00')
        finish_time.send_keys('17:00')
        hours_worked.send_keys('1')
    else:
        start_time.send_keys(input("Enter Start Time: "))
        finish_time.send_keys(input("Enter Finish Time: "))
        comment.send_keys('Fundamentals of Computer Science')
        hours_worked.send_keys(input("Hours Worked: "))

    sick_hours.send_keys('0')
    comment.send_keys('Fundamentals of Software Development Tutorial')
    okay = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    okay.click()
    driver.close()
    send_email('Fundamentals of Software Development Tutorial')
    print('\nFundamentals of Software Development Tutorial')


def mixed_learning():
    mixed_list = [fsd, fcs]
    for module in mixed_list:
        module()


def sfe():
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
    start_time.send_keys('09:00')
    finish_time.send_keys('11:00')
    hours_worked.send_keys('2')
    sick_hours.send_keys('0')
    comment.send_keys('Software Engineering')
    okay = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    okay.click()
    driver.close()
    send_email('Software Engineering')
    print('\nSoftware Engineering')


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
#francis()
#lucia()
#lucia_prepare()
#iot() update


def main():
    global passwd

    passwd = config.passwd
    print('--------------------------------------------')
    print("Running Emeka's Script, Please do not close")
    print('--------------------------------------------')
    print('Program is active...')
    schedule.every().tuesday.at("11:10").do(fcs)
    schedule.every().tuesday.at("14:10").do(fsd)
    schedule.every().tuesday.at("18:10").do(mixed_learning)
    schedule.every().friday.at("11:10").do(sfe)

    while True:
        schedule.run_pending()
        time.sleep(50)


if __name__ == "__main__":
    main()


