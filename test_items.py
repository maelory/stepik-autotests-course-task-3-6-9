import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_cta_is_presented(browser):
    browser.get(link)
    assert browser.find_element_by_xpath("//button[contains(@class, 'btn-add-to-basket')]").is_displayed(), \
        "Add to basket button should be displayed"
    #time.sleep(30)
