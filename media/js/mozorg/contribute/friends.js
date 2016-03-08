/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function($, Mozilla) {
    'use strict';

    var $ffShowSignupForm = $('#ff-show-signup-form');
    var $ffSignupArea = $('#ff-signup');
    //var $ffSignupButton = $('#footer_email_submit');

    function supportsSVG() {
        return document.implementation.hasFeature('http://www.w3.org/TR/SVG11/feature#Image', '1.1');
    }

    // fallback to .png for browsers that don't support .svg as an image.
    if (!supportsSVG()) {
        $('img[src*="svg"][data-fallback="true"]').attr('src', function() {
            return $(this).attr('data-png');
        });
    }

    $ffShowSignupForm.on('click', function() {
        $ffShowSignupForm.addClass('invisible').off('click');

        // slide the form container down
        $ffSignupArea.slideDown('normal', function() {
            // scroll to top of revealed form
            Mozilla.smoothScroll({
                top: $ffSignupArea.offset().top - 60
            });

            $('#id_email').focus();
        });

        window.dataLayer.push({
            'event': 'firefox-sync-interaction',
            'interaction': 'display signup form'
        });
    });

    /*
    Unsure if this is necessary - think we already have tracking on this form?
    Waiting on comment from garethc in the bug.

    $ffSignupButton.on('click', function() {
        window.dataLayer.push({
            'event': 'firefox-sync-interaction',
            'interaction': 'signup form submit'
        });
    });
    */
})(window.jQuery, window.Mozilla);
