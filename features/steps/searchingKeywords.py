from behave import given, when, then
from selenium import webdriver


@given("I launch firefox browser")
def launchBrowser(context):
    context.driver = webdriver.Firefox(
        executable_path="./resources/drivers/geckodriver"
    )


@when("I go on google web site")
def goToGoogleWebSite(context):
    context.driver.get("https://www.google.com/")
    context.driver.find_element_by_id("L2AGLb").click()


@when('I enter the keyword "{keywords}" in the search bar')
def enterKeywordsValue(context, keywords):
    search_xpath = context.driver.find_element_by_xpath(
        "//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]"
    )
    search_xpath.send_keys(keywords)


@when("I click on Google search button")
def clickOnSearchButton(context):
    search_button_xpath = context.driver.find_element_by_xpath(
        "//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[3]/center[1]/input[1]"
    )
    search_button_xpath.click()


@then(
    "The google web site displays the results of the search containing the keyword {keywords}"
)
def is_keyword_search_results_displayed(context, keywords):
    search_results = context.driver.find_element_by_xpath(
        '//div[@id="rso"]/div[contains(div, "Publicis Sapient")]'
    ).text
    assert keywords in search_results
    context.driver.close()
