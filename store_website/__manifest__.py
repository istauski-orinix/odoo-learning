{
    "name": "store_website",
    "version": "1.0",
    "category": "Website",
    "depends": ["base", "website"],
    "data": [
        "views/store_website_templates.xml",
        "views/store_website_inherit_home.xml",
        "views/store_website_restricted_template.xml",
        "views/store_website_form.xml",
        "security/ir.model.access.csv",
        "security/store_website_security.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "/store_website/static/src/css/store_style.scss",
            "/store_website/static/src/js/script.js",
            "/store_website/static/src/xml/templates.xml",
            "/store_website/static/src/js/owl/MyCounter.js",
            "/store_website/static/src/js/owl/MountMyCounter.js",
        ],
    },
    "installable": True,
    "application": False,
}
