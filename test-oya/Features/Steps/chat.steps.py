from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@when(u'Go to homepage')
def step_impl(context):
    context.driver.get("https://oyaghana.com")


@when(u'open chat')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]").click()


@then(u'check if chat opens')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/div/div[1]").text
    if text == "Oya! Ghana":
        context.driver.close()
        assert True, "Test passed"
