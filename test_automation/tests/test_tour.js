odoo.define('test_automation.tour_example', function (require) {
    "use strict";
    const Tour = require('web_tour.tour');

    Tour.register('test_automation_frontend_tour', {
        test: true,
        url: '/web',
    }, [
        {
            content: "wait for main screen",
            trigger: '.o_app[data-menu-xmlid="base.menu_administration"]',
            run: function () {}
        },
        {
            content: "click settings",
            trigger: '.o_app[data-menu-xmlid="base.menu_administration"]',
            run: 'click',
        },
    ]);
});