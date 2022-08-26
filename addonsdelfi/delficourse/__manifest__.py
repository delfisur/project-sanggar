# -*- coding: utf-8 -*-
{
    'name': "delficourse",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/coursependaftaran_view.xml',
        'views/pendaftaranlevel_view.xml',
        'views/bahasa_view.xml',
        'views/pesertadidik_view.xml',
        'views/tutor_view.xml',
        'views/admin_view.xml',
        'views/sessionpemprograman_view.xml',
        'views/sessionbahasa_view.xml',
        'views/keterampilan_view.xml',
        'views/sessionketerampilan_view.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
