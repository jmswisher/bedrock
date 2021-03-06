# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from selenium.common.exceptions import TimeoutException

from pages.home import HomePage
from pages.about import AboutPage
from pages.contribute.contribute import ContributePage
from pages.mission import MissionPage
from pages.firefox.all import FirefoxAllPage
from pages.firefox.desktop.desktop import DesktopPage
from pages.firefox.desktop.customize import CustomizePage
from pages.firefox.desktop.all import FirefoxDesktopBasePage
from pages.firefox.hello import HelloPage
from pages.firefox.sync import FirefoxSyncPage
from pages.plugincheck import PluginCheckPage
from pages.smarton.landing import SmartOnLandingPage
from pages.smarton.base import SmartOnBasePage


@pytest.mark.nondestructive
@pytest.mark.parametrize(('page_class', 'url_kwargs'), [
    pytest.mark.smoke((HomePage, None)),
    (AboutPage, None),
    pytest.mark.smoke((ContributePage, None)),
    (MissionPage, None),
    (FirefoxAllPage, None),
    pytest.mark.smoke((DesktopPage, None)),
    (CustomizePage, None),
    (FirefoxDesktopBasePage, {'slug': 'fast'}),
    (FirefoxDesktopBasePage, {'slug': 'trust'}),
    (FirefoxSyncPage, None),
    (HelloPage, None),
    pytest.mark.skip_if_not_firefox((PluginCheckPage, None),
        reason='https://bugzilla.mozilla.org/show_bug.cgi?id=1245208'),
    (SmartOnLandingPage, None),
    pytest.mark.skip_if_not_firefox((SmartOnBasePage, {'slug': 'tracking'}),
        reason='Newsletter is only shown to Firefox browsers.'),
    pytest.mark.skip_if_not_firefox((SmartOnBasePage, {'slug': 'security'}),
        reason='Newsletter is only shown to Firefox browsers.'),
    pytest.mark.skip_if_not_firefox((SmartOnBasePage, {'slug': 'surveillance'}),
        reason='Newsletter is only shown to Firefox browsers.')])
def test_newsletter_default_values(page_class, url_kwargs, base_url, selenium):
    url_kwargs = url_kwargs or {}
    page = page_class(base_url, selenium, **url_kwargs).open()
    page.newsletter.expand_form()
    assert '' == page.newsletter.email
    assert 'United States' == page.newsletter.country
    assert not page.newsletter.privacy_policy_accepted
    assert page.newsletter.is_privacy_policy_link_displayed


@pytest.mark.flaky(reruns=1, reason='https://bugzilla.mozilla.org/show_bug.cgi?id=1218451')
@pytest.mark.parametrize('page_class', [HomePage, ContributePage])
def test_newsletter_successful_sign_up(page_class, base_url, selenium):
    page = page_class(base_url, selenium).open()
    page.newsletter.expand_form()
    page.newsletter.type_email('noreply@mozilla.com')
    page.newsletter.select_country('United Kingdom')
    page.newsletter.select_text_format()
    page.newsletter.accept_privacy_policy()
    page.newsletter.click_sign_me_up()
    assert page.newsletter.sign_up_successful


@pytest.mark.nondestructive
@pytest.mark.parametrize('page_class', [HomePage, ContributePage])
def test_newsletter_sign_up_fails_when_missing_required_fields(page_class, base_url, selenium):
    page = page_class(base_url, selenium).open()
    page.newsletter.expand_form()
    with pytest.raises(TimeoutException):
        page.newsletter.click_sign_me_up()
