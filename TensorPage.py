from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TensorPage(BasePage):
    LOCATOR_POWER_IN_STAFF = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')
    LOCATOR_ABOUT = (By.CSS_SELECTOR, 'p > a[href^="/about"]')
    LOCATOR_IMAGES = (By.CSS_SELECTOR, '.tensor_ru-About__block3-image-filter')


    def check_power_in_staff(self):
        self.switch()
        element = self.find_element(TensorPage.LOCATOR_POWER_IN_STAFF)
        self.scroll_to_element(element)
        return element

    def click_about(self):
        self.find_element(TensorPage.LOCATOR_ABOUT).click()

    def check_url(self):
        assert self.get_url() == 'https://tensor.ru/about', "Неверный URL"

    def check_images_size(self):
        images = self.find_elements(TensorPage.LOCATOR_IMAGES)
        for i in range(0, len(images)-1):
            assert images[i].size == images[i+1].size

