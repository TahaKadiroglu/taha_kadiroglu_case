from pages.base_page import BasePage

class OpenPositionsPage(BasePage):

    quality_assurance_text_in_department = ("xpath","//*[@title ='Quality Assurance']")
    filter_by_location = ("id", "select2-filter-by-location-container")
    istanbul_turkiye_locator = ("xpath", "//ul[@id='select2-filter-by-location-results']/li[2]")
    job_posts = ("xpath", "//div[@class='position-list-item-wrapper bg-light']")
    quality_assurance_jobs = ("xpath", "//span[@class='position-department text-large font-weight-600 text-primary'][text()= 'Quality Assurance']")
    position_titles = ("xpath", "(//p[@class='position-title font-weight-bold'])[1]")
    department_titles = ("xpath", "//span[@class='position-department text-large font-weight-600 text-primary']")
    locations = ("xpath", "//div[@class='position-location text-large']")
    first_view_role_button = ("xpath", "(//*[text() = 'View Role'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_qa_department_filter(self):
        self.wait_for_element(self.quality_assurance_text_in_department, timeout=20)
        self.scroll_page()

    def click_filter_by_location(self):
        self.click_element(self.filter_by_location)

    def select_istanbul_turkiye(self):
        self.click_element(self.istanbul_turkiye_locator)

    def wait_for_presence_of_qa_jobs(self):
        self.wait_for_element(self.quality_assurance_jobs)

    def check_job_posts_content(self):

        job_elements = self.find_elements(self.job_posts)
        for job in job_elements:
            position = self.get_element_text(self.position_titles)
            department = self.get_element_text(self.department_titles)
            location = self.get_element_text(self.locations)
            assert "Quality Assurance" in position, f"Wrong position {position}"
            assert "Quality Assurance" in department, f"Wrong department {department}"
            assert "Istanbul, Turkiye" in location, f"Wrong location {location}"

    def click_first_view_role_button(self):
        self.click_element(self.first_view_role_button)