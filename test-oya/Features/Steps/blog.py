import time
from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

@when(u'Go to Blog page')
def step_impl(context):
    context.driver.get("https://oyaghana.com/services")
    time.sleep(2)

@when(u'Click on readmore')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/article/div/div/section[2]/div/div[1]/div/section/div/div/div/div[4]/div/div/a/span/span").click()

@then(u'success read')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/nav/div[3]/h1").text
    if text == "home":
        context.driver.close()
        assert True, "Test passed"
