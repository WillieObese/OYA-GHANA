import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

@when(u'Open register page')
def registrationPage(context):
    context.driver.get("https://accounts.test.oyaghana.com/signup")


@when(u'Enter firstname "William" and lastname "Obese"')
def Names(context):
    context.driver.find_element(By.ID, 'first_name').send_keys("William")
    context.driver.find_element(By.ID, "last_name").send_keys("Obese")


@when(u'Select Ghana')
def step_impl(context):
    dropdwn=context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div/form/div[2]/div/div/div[2]/div/div/div/div/select")
    dd = Select(dropdwn)
    dd.select_by_value("GH")


@when(u'Enter Phone number')
def step_impl(context):
    context.driver.find_element(By.ID, 'phone').send_keys("0508038271")

@when(u'Enter Pin')
def step_impl(context):
    context.driver.find_element(By.NAME, 'pin1').send_keys("1996")
    context.driver.find_element(By.ID, "pin2").send_keys("1996")



@when(u'Click on Cintinue')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[1]/div/form/button").click()

@then(u'Enter first "{first}" and second {second}"')
def step_impl(context, first, second):
    context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[1]/div/form/div[1]/div/div[2]/div/div/div/input').send_keys(first)
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div/form/div[2]/div/div[2]/div/div/div/input").send_keys(second)


@then(u'Click on Submit')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div/form/button").click()


@then(u'Redirection to Login page')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div/div/h3").text
    if text == "Sign in to continue traveling with ease":
        context.driver.close()
        assert True, "Test passed"




