from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class MainPage(BasePage):
    LOCATOR_CONTACTS = (By.CSS_SELECTOR, 'ul > li >a[href^="/contacts"]')
    LOCATOR_TENSOR_BANNER = (By.CSS_SELECTOR, 'div > a[href^="https://tensor.ru"')
    LOCATOR_REGION = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser > span')
    LOCATOR_PARTNERS_LIST = (By.CSS_SELECTOR, "div[name='itemsContainer']")
    LOCATOR_KAMCHATKA = (By.CSS_SELECTOR, "li > span[title='Камчатский край'] > span")
    LOCATOR_KAMCHATKA_PARTNERS = (By.CSS_SELECTOR, "div[name='itemsContainer'] > div > div > div")
    LOCATOR_LOCAL_PLUGINS = (By.CSS_SELECTOR, "li >  a[href='/download']")
    LOCATOR_DOWNLOAD = (By.CSS_SELECTOR, "a[href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")

    def click_contacts(self):
        self.find_element(MainPage.LOCATOR_CONTACTS).click()

    def click_tensor_banner(self):
        self.find_element(MainPage.LOCATOR_TENSOR_BANNER).click()

    def check_home_region(self):
        region = self.find_element(MainPage.LOCATOR_REGION)
        assert 'Костромская обл.' in region.text, 'Неверное отображение домашнего региона'

    def check_partners(self):
        assert self.find_element(MainPage.LOCATOR_PARTNERS_LIST), 'Не отображаются партнёры'

    def edit_region(self):
        self.find_element(MainPage.LOCATOR_REGION).click()
        self.find_element(MainPage.LOCATOR_KAMCHATKA).click()
        time.sleep(2)

    def check_kamchatka(self):
        region = self.find_element(MainPage.LOCATOR_REGION)
        partners = self.find_element(MainPage.LOCATOR_KAMCHATKA_PARTNERS)
        assert 'Камчатский край' in region.text, 'Неверное отображение Камчатского края'
        assert 'Петропавловск-Камчатский' in partners.text, 'Неверное отображение партнёров по региону'
        assert self.get_url() == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients', 'Неверный URL'
        assert self.get_title() == 'СБИС Контакты — Камчатский край', 'Неверный title'
