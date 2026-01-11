{
    "name": "Export Template Visibility Restriction",
    "description": "Restricts visibility of ir.exports templates to users and admin.",
    "version": "17.0",
    "author": "Nioses Business Consulting and Services",
    "company": "Nioses Business Consulting and Services",
    "maintainer": "Nioses Business Consulting and Services",
    "website": "https://nioses.com/",
    "category": "Tools",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "view/ir_custom_model_fields_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "ir_restiction_module/static/src/js/common.js",
        ],
    },
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}
