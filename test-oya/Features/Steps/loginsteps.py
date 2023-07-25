from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'Launch chrome browser')
def openBrowser(context):
    context.driver = webdriver.Chrome()

@when(u'Open login page')
def openLoginPage(context):
    context.driver.get("https://accounts.test.oyaghana.com/login")


@when(u'Enter phone "{phone}" and pin {pin}"')
def step_impl(context, phone, pin):
    context.driver.find_element(By.ID,'phone').send_keys(phone)
    context.driver.find_element(By.ID, "pin").send_keys(pin)


@when(u'Click on Enter')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[1]/div/form/button").click()


@then(u'success')
def step_impl(context):
    text = context.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/nav/div[3]/h1").text
    if text == "home":
        context.driver.close()
        assert True, "Test passed"
