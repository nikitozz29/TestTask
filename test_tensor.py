from MainPage import *
from TensorPage import *


def test_photo_size(chrome):
    sbis_page = MainPage(chrome)
    sbis_page.go_to_main_page()
    sbis_page.click_contacts()
    sbis_page.click_tensor_banner()
    tensor_page = TensorPage(chrome)
    tensor_page.check_power_in_staff()
    tensor_page.click_about()
    tensor_page.check_url()
    tensor_page.check_images_size()


def test_region(chrome):
    sbis_page = MainPage(chrome)
    sbis_page.go_to_main_page()
    sbis_page.click_contacts()
    sbis_page.check_home_region()
    sbis_page.check_partners()
    sbis_page.edit_region()
    sbis_page.check_kamchatka()

