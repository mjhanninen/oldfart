'use strict';

function makeDelayer(delay) {
    var clock = 0;
    return function(func) {
        var postedOn = ++clock;
        var passedArguments = Array.prototype.slice.call(arguments, 1);
        window.setTimeout(function() {
            if (clock === postedOn) {
                func.apply(null, passedArguments)
            };
        }, delay);
    };
}

function makeDelayed(func, delay) {
    var delayer = makeDelayer(delay);
    return function() {
        var args = Array.prototype.slice.call(arguments);
        args.unshift(func);
        delayer.apply(null, args);
    };
}
