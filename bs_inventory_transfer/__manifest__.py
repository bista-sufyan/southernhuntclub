# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################
{
    'name': "BS Inventory Transfer(Stock)",

    'summary': """
        stock related modification""",

    'description': """
        This module contains customization over Stock and it's relavent objects.
    """,

    'author': "Bista Solutions",
    'website': "http://www.bistasolutions.com",

    'category': 'Hidden',
    'version': '1',

    # Dependent module required for this module to be installed
    'depends': ['base','stock','sale_stock','bs_sales'],
    # always loaded
    'data': [
        'security/security_view.xml',
        'security/ir.model.access.csv',
        'views/stock_picking_view.xml',
        'report/pending_delivery_order_view.xml',
    ],
    
    'installable': True,
    'auto_install': False,
    'application': True
}
