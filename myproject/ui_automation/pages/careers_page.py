from pages.base_page import BasePage

class CareersPage(BasePage):

    our_locations = ("id", 'career-our-location')
    our_locations_area = ("xpath", '//*[@data-glide-el="track"]')
    teams = ("id", "career-find-our-calling")
    teams_area = ("xpath", '//*[text()="See all teams"]')
    life_at_insider = ("xpath", '//*[@data-id="87842ec"]')
    life_at_insider_area = ("xpath", '//*[@data-id="c06d1ec"]')

    def __init__(self, driver):
        self.driver = driver

    def our_locations_visibility(self):
        self.wait_for_element(self.our_locations)
        self.wait_for_element(self.our_locations_area)

    def teams_area_visibility(self):
        self.wait_for_element(self.teams)
        self.wait_for_element(self.teams_area)

    def life_at_insider_visibility(self):
        self.wait_for_element(self.life_at_insider)
        self.wait_for_element(self.life_at_insider_area)





