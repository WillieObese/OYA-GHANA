from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@when(u'Home page')
def homePage(context):
    context.driver.get("https://test.oyaghana.com/")

@when(u'Click on footer "<footer>"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/p[1]").click()

@then(u'successful login')
def step_impl(context):
    text = context.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/nav/div[3]/h1").text
    if text == "home":
        context.driver.close()
        assert True, "Test passed"

