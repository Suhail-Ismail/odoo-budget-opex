# -*- coding: utf-8 -*-
{
    'name': "Operational Expenditure",
    'version': '0.1',
    'summary': 'OPEX Management',
    'sequence': 5,
    'description': """
Budget Operational Expenditure
===========
Specifically Designed for Etisalat-TBPC

Summary
---------------------
- Account Code
- Access Users
    - Account Code
        - Dependent - Can readonly
        - User - General Usage except delete power, can Edit recurrence but not create
        - Manager - All power to manipulate data
    - Cost Center
        - Dependent - Can readonly
        - User - General Usage except delete power, can Edit recurrence but not create
        - Manager - All power to manipulate data
- Validations
    - Account Code
- Tagging Feature
- Utilities
    """,
    'author': "Marc Philippe de Villeres",
    'website': "https://github.com/mpdevilleres",
    'category': 'TBPC Budget',
    'depends': [
        'budget_core'
    ],
    'data': [
        'security/budget_opex.xml',
        'security/ir.model.access.csv',

        'views/oear.xml',
#        'views/task_progress.xml',

        'views/budget_inherit.xml',
        'views/contract_inherit.xml',

#        'workflows/budget_capex_task.xml',

        'views/menu.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
