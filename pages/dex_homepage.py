
from selene import browser, have, be, command
from selene.support.shared import config

class HomePage():

    def open(self):
        """
        Open homepage
        """
        browser.open("/")
        return self

    def check_title(self, value):
        """
        Check meta information
        """
        browser.should(have.title(value))
        return self

    def check_h1(self):
        """
        Check h1 header is not empty
        """
        h1 = browser.element("h1")
        h1.should(be.not_.blank)
        return self
    
    def check_header_phone(self, phone_number):
        """
        Check header phone number
        """
        header_phone = browser.element(".tn-elem__4984737541666082087310")
        header_phone.should(have.exact_text(phone_number))
        return self
        
    def typing_text_sequence(self, values):
        """
        Check typing text sequence
        """
        typing_text = browser.element(".t635__typing-text").should(be.visible)

        for value in values:
            typing_text.should(have.text(value))
        return self

    def check_client_section_logos(self, logos_count):
        """
        Check client section visibility and logos count
        """
        client_section = browser.element("#rec498919765")
        client_section_logos = browser.all("#rec498919765 .t-img")

        # Scroll to the client section
        client_section.perform(command.js.scroll_into_view)
        # Adjust scroll position
        browser.driver.execute_script("window.scrollBy(0, -100);")

        client_section.should(be.visible)
        for logo in client_section_logos:
            logo.should(be.visible)
        client_section_logos.should(have.size(logos_count))
        return self

    def check_footer_links(self, services, cases, job):
        """
        Check footer links
        """
        services_link = browser.element("[data-elem-id='1666099691481'] a")
        cases_link = browser.element("[data-elem-id='1666099733290'] a") 
        jobs_link = browser.element("[data-elem-id='1668678701878'] a")

        services_link.perform(command.js.scroll_into_view)

        services_link.should(be.visible)
        cases_link.should(be.visible) 
        jobs_link.should(be.visible)

        services_link.should(
            have.exact_text(services).and_(
            have.attribute("href").value(f"{config.base_url}/services"))
            )
        cases_link.should(
            have.exact_text(cases).and_(
            have.attribute("href").value(f"{config.base_url}/cases"))
            )
        jobs_link.should(
            have.exact_text(job).and_(
            have.attribute("href").value(f"{config.base_url}/job"))
            )
        return self
    
