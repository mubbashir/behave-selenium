from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@when('we visit google')
def step_impl(context):
    context.browser.get('http://www.google.com')


@when(u'search for "{text}"')
def step_impl(context, text):
    search_box = context.browser.find_element_by_name("q")
    search_box.send_keys(text)
    search_box.submit()
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "resultStats"))
    )


@then(u'it should have a title "{text}"')
def step_impl(context, text):
	print( "" + text +" "+ context.browser.title)
	assert text in context.browser.title
