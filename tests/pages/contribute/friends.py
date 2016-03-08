# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.contribute.base import ContributeBasePage


class ContributeFriendsPage(ContributeBasePage):

    _url = '{base_url}/{locale}/contribute/friends'

    _show_signup_form_button_locator = (By.ID, 'ff-show-signup-form')
    _signup_form_locator = (By.ID, 'newsletter-form')

    @property
    def is_signup_form_displayed(self):
        return self.is_element_displayed(self._signup_form_locator)

    def click_show_signup_form(self):
        self.find_element(self._show_signup_form_button_locator).click()
        self.wait.until(lambda s: self.is_signup_form_displayed)
