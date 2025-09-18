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
            "store_website/static/src/**/*",
        ],
    },
    "installable": True,
    "application": False,
}
