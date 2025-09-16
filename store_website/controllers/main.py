# main.py
from odoo import http
from odoo.http import request


class StoreWebsiteController(http.Controller):
    @http.route("/store", type="http", auth="public", website=True)
    def store_homepage(self, **kw):
        # Проверяем, является ли текущий пользователь публичным (гостем)
        is_user_logged_in = request.env.user and not request.env.user._is_public()

        # Готовим данные для передачи в шаблон
        template_values = {
            "user_logged_in": is_user_logged_in,
            "user_name": request.env.user.name if is_user_logged_in else "",
        }

        # Отображаем шаблон с нашими данными
        return request.render("store_website.store_website_homepage", template_values)


class StoreHomepageWebsiteController(http.Controller):
    @http.route("/store/contact", type="http", auth="public", website=True)
    def store_homepage_inherit(self, **kw):
        return request.render("store_website.inherit_homepage", kw)


class StoreContactsWebsiteController(http.Controller):

    @http.route(
        "/store/contact/submit",
        type="http",
        auth="public",
        website=True,
        methods=["POST"],
    )
    def store_contact_submit(self, **kwargs):
        name = kwargs.get("name")
        message = kwargs.get("message")
        request.env["store.contact"].sudo().create(
            {
                "name": name,
                "message": message,
            }
        )
        return request.redirect("/thanks")


class StoreManagerController(http.Controller):
    @http.route("/store/manager", type="http", auth="user", website=True)
    def manager_page(self, **kwargs):
        if not request.env.user.has_group("store_website.group_store_manager"):
            return request.redirect("/1231ismfwkfow")
        return http.request.render("store_website.restricted_content")
