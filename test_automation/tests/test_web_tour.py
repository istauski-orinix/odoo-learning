from odoo.tests import HttpCase


class TestWebTour(HttpCase):
    post_install = True

    def test_01_frontend_tour(self):
        self.browser_js(
            url_path="/web",
            code="""odoo.__DEBUG__.services['web_tour.tour'].run('test_automation_frontend_tour');""",
            ready="odoo.__DEBUG__.services['web_tour.tour'].tours.test_automation_frontend_tour.ready",
        )
