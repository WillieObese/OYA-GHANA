import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@when(u'Open ticket page')
def step_impl(context):
    context.driver.get("https://app.test.oyaghana.com/buy-ticket")
    time.sleep(2)
    context.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/span/label/span[2]/h4').click()


@when(u'Select who you are buying for')
def step_impl(context):
    context.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/span/label/span[2]/h4').click()

@when(u'Enter origin, destination, date, minors')
def step_impl(context):
    context.driver.find_element(By.ID, 'from').send_keys("Accra")
    context.driver.find_element(By.ID, "to").send_keys("Obese")
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/div/form/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div').send_keys("26 July,2023")
    context.driver.find_element(By.ID, "minor").send_keys("2")


@then(u'Proceed to next page')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/nav/div[3]/h1").text
    if text == "home":
        context.driver.close()
        assert True, "Test passed"

