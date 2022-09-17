# -*- coding: utf-8 -*-
{
    'name': "delfisanggar",

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
    'application': True,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/datapenyewaan.xml',
        'data/datapeserta.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/pendaftaran_view.xml',
        'views/materi_view.xml',
        'views/kelas_view.xml',
        'views/pelatih_view.xml',
        'views/jadwal_view.xml',
        'views/session_view.xml',
        'views/kostum_view.xml',
        # 'views/alatmusik_view.xml',
        'views/penyewaan_view.xml',
        'views/pengembalian_view.xml',
        'views/nonpeserta_view.xml',


        'report/report.xml',
        'report/kwitansi_penyewaan.xml',

        'wizzard/kostumbaru_wizzard_view.xml'












    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
