import unittest
import time


def test_should_see_button(language, browser):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(10)

    basket_class = browser.find_element_by_css_selector("#add_to_basket_form > button")
    basket = basket_class.get_attribute("class")
    assert basket == "btn btn-lg btn-primary btn-add-to-basket", "Element not found!!!"
    time.sleep(30)

if __name__ == "__main__":
    unittest.main()
