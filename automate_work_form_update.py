from selenium import webdriver
from datetime import *
import calendar
import schedule
import time
import config
import smtplib

# hello
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
    try:
        driver = webdriver.Chrome(executable_path=r"C:\Program Files\chrome driver\chromedriver.exe")
        driver.get('https://mypayments.lsbu.ac.uk/vts/')
    except Exception as e:
        print(f"Upgrade your chrome driver \n {e}")
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
    driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstSess_ctl00__5"]').click()
    select_ok = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    select_ok.click()

    worked_hours = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstClm_ctl00_ctl04_fldWork"]')
    worked_hours.send_keys('3.00')

    sick_hours = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstClm_ctl00_ctl04_fldSick"]')
    sick_hours.send_keys('0.00')

    comment = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstClm_ctl00_ctl04_fldComment"]')
    comment.send_keys('Fundamentals of Computer Science Tutorial')

    okay = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    okay.click()
    driver.close()
    send_email('Fundamentals of Computer Science')
    print('\nFundamentals of Computer Science')


def fsd():
    initialization()

    driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstSess_ctl00__4"]').click()
    select_ok = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    select_ok.click()

    worked_hours = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstClm_ctl00_ctl04_fldWork"]')
    worked_hours.send_keys('3.00')

    sick_hours = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstClm_ctl00_ctl04_fldSick"]')
    sick_hours.send_keys('0.00')

    comment = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstClm_ctl00_ctl04_fldComment"]')
    comment.send_keys('Fundamentals of Software Development Tutorial')

    okay = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    okay.click()
    driver.close()
    send_email('Fundamentals of Software Development Tutorial')
    print('\nFundamentals of Software Development Tutorial')


def sfe():
    initialization()
    select_iot = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstSess_ctl00__3"]').click()
    select_OK = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    select_OK.click()

    worked_hours = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstClm_ctl00_ctl04_fldWork"]')
    worked_hours.send_keys('2.00')

    sick_hours = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstClm_ctl00_ctl04_fldSick"]')
    sick_hours.send_keys('0.00')

    comment = driver.find_element_by_xpath(xpath='//*[@id="ctl00_ContentPlaceHolder1_lstClm_ctl00_ctl04_fldComment"]')
    comment.send_keys('Software Engineering Tutorial')

    okay = driver.find_element_by_xpath(
        xpath='//*[@id="ctl00_ContentPlaceHolder1_RadToolBar1"]/div/div/div/ul/li[1]/a/span/span/span')
    okay.click()
    driver.close()
    send_email('Software Engineering Tutorial')
    print('\nSoftware Engineering Tutorial')


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


def main():
    global passwd

    passwd = config.passwd
    print('--------------------------------------------')
    print("Running Emeka's Script, Please do not close")
    print('--------------------------------------------')
    print('Program is active...')
    schedule.every().tuesday.at("12:10").do(fcs)
    schedule.every().tuesday.at("15:10").do(fsd)

    schedule.every().friday.at("11:10").do(sfe)

    while True:
        schedule.run_pending()
        time.sleep(50)


if __name__ == "__main__":
    main()


