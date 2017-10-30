# -*- coding: utf-8 -*-
{
    'name': "Operational Expenditure",
    'version': '11.0.0.1',
    'summary': 'OPEX Management',
    'sequence': 5,
    'description': """
    """,
    'author': "Marc Philippe de Villeres",
    'website': "https://github.com/mpdevilleres",
    'category': 'TBPC Budget',
    'depends': [
        'budget_enduser',
        'budget_core',
        'budget_contractor'
    ],
    'data': [
        'security/budget_opex.xml',
        'security/ir.model.access.csv',

        'views/oear.xml',

        'views/budget_inherit.xml',
        'views/contract_inherit.xml',

        'views/menu.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
