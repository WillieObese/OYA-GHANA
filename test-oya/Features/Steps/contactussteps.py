import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@when(u'Navigate to contact us page')
def step_impl(context):
    context.driver.get("https://oyaghana.com/contact")
    time.sleep(2)


@when(u'Phen Enter  fullname "William Obese", second "williamgyau248@gmail.com", phone"0208033577", message "test"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/article/div/div/section[2]/div/div[1]/div/div/div/div/div/div/div[4]/form/div/div[2]/nf-fields-wrap/nf-field[1]/div/div[2]/div/div[2]/input").send_keys("William Obese")
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/article/div/div/section[2]/div/div[1]/div/div/div/div/div/div/div[4]/form/div/div[2]/nf-fields-wrap/nf-field[2]/div/div[2]/div/div[2]/input").send_keys("williamgyau248@gmail.com")
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/article/div/div/section[2]/div/div[1]/div/div/div/div/div/div/div[4]/form/div/div[2]/nf-fields-wrap/nf-field[3]/div/div[2]/div/div[2]/input').send_keys("0208033577")
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/article/div/div/section[2]/div/div[1]/div/div/div/div/div/div/div[4]/form/div/div[2]/nf-fields-wrap/nf-field[4]/div/div[2]/div/div[2]/textarea").send_keys("test")

@then(u'Click Submit')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/article/div/div/section[2]/div/div[1]/div/div/div/div/div/div/div[4]/form/div/div[2]/nf-fields-wrap/nf-field[5]/div/div[2]/div/div[2]/input").click()

@then(u'Message Sent')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/article/div/div/section[2]/div/div[1]/div/div/div/div/div/div/div[1]/p[1]").text
    if text == "Form submitted successfully":
        context.driver.close()
        assert True, "Test passed"


