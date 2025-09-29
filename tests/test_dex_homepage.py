import allure
from selene import browser
from pages.dex_homepage import HomePage

allure.feature("UI test")
@allure.title("dex-it.ru Homepage Tests")
@allure.description("""
This test checks dex-it.ru homepage.
""")
def test_dex_homepage():
    home_page = HomePage()

    with allure.step("Open homepage"):
        home_page.open()

    with allure.step("Check homepage title"):
        home_page.check_title("DEX - Digital интегратор")
    
    with allure.step("Check header phone number"):
        home_page.check_header_phone("+7 499 348-11-07")

    with allure.step("Check h1 header visibility"):
        home_page.check_h1()

    with allure.step("Check typing text sequence"):
        home_page.typing_text_sequence(
            ["АНАЛИТИКА", "ДИЗАЙН", "РАЗРАБОТКА", "ПОДДЕРЖКА", "РАЗВИТИЕ"]
        )

    with allure.step("Check client section visibility and logos count"):
        home_page.check_client_section_logos(logos_count=16)

        with allure.step("Client section screenshot"):
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name="Client section",
                attachment_type=allure.attachment_type.PNG
                )

    with allure.step("Check footer links"):
        home_page.check_footer_links(
            "УСЛУГИ", "КЕЙСЫ", "ВАКАНСИИ"
        )

        with allure.step("Footer screenshot"):
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name="Footer",
                attachment_type=allure.attachment_type.PNG
                )