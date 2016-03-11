/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function($, Mozilla) {
    'use strict';

    var $ffShowSignupForm = $('#ff-show-signup-form');
    var $ffSignupArea = $('#ff-signup');

    $ffShowSignupForm.on('click', function() {
        $ffShowSignupForm.addClass('invisible').off('click');

        // slide the form container down
        $ffSignupArea.slideDown('normal', function() {
            $('#id_email').focus();

            // scroll to top of revealed form
            Mozilla.smoothScroll({
                top: $ffSignupArea.offset().top - 60
            });
        });

        window.dataLayer.push({
            'event': 'firefox-sync-interaction',
            'interaction': 'display signup form'
        });
    });

    Mozilla.SVGImage.fallback();

    /*
    Unsure if this is necessary - think we already have tracking on this form?
    Waiting on comment from garethc in the bug.

    $('#footer_email_submit').on('click', function() {
        window.dataLayer.push({
            'event': 'firefox-sync-interaction',
            'interaction': 'signup form submit'
        });
    });
    */
})(window.jQuery, window.Mozilla);
