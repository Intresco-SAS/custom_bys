# -*- coding: utf-8 -*-
{
    'name': "Módulo Personalizado B&S Transportes",

    'summary': """
        Módulo Personalizado B&S Transportes""",

    'description': """
        Módulo Personalizado B&S Transportes para la gestión de los procesos de transporte y logística.
    """,

    'author': "Intresco SAS",
    'website': "http://www.intresco.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'stock',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_bys.xml',
        'reports/report_delivery_inherit.xml',
        'views/stock_move_bys.xml',
        'data/record_required_process.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}