'use strict';

function _e(elemId) {
    return document.getElementById(elemId)
}

function _v(elemId) {
    return _e(elemId).value;
}

function fetchQrNow() {
    _e('qr-image').src = '/qr/' + MD5(_v('qr-seed')) + '.png';
}

var fetchQrSoon = makeDelayed(fetchQrNow, 250);
