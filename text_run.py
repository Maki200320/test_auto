import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/search?q=weSchool&oq=weSchool&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDQ2NTBqMGoyqAIAsAIB&sourceid=chrome&ie=UTF-8")
    page.get_by_role("link", name="W3Schools Online Web").click()
    page.get_by_role("link", name="PYTHON", exact=True).click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Try it Yourself »").click()
    page1 = page1_info.value
    page1.get_by_role("button", name="Run ❯").click()
    time.sleep(5)
    
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
