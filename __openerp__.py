# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'license': 'LGPL-3',
    "name" : "Stock Move Price",
    "version" : "1.9.2",
    "author" : "Kristian Koci",
    'category': 'Inventory Management',
    "summary": "Agrega precio a las lineas de stock.picking",
    'description': "Inspirado en el addon para Odoo v9 Enterprise de Bista solutions, modificado para Odoo v9 Community",
    'maintainer': "Kristian Koci",
    'website': 'https://kkoci.github.io',
    "depends" : ["base","stock","product"],
    "init_xml" : [],
    "demo_xml" : [],
    "data" : [
        'views/stock_move.xml',
    ],
    "test" : [
    ],
    "auto_install": False,
    "application": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
