from selenium import webdriver

driver = webdriver.Chrome()  # Replace with Firefox() for Firefox
driver.get("https://infyspringboard.onwingspan.com/auth/realms/infyspringboard/protocol/openid-connect/auth?client_id=portal&redirect_uri=https%3A%2F%2Finfyspringboard.onwingspan.com%2Fweb%2Fen%2F%2Fpage%2Fhome&state=ce5f804e-1f7b-48cd-8f85-28b2ab34208e&response_mode=fragment&response_type=code&scope=openid&nonce=d9389d00-578b-45ae-818b-058efd13ff17")
print(driver.title)
driver.quit()
