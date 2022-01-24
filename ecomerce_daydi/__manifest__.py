# -*- coding: utf-8 -*-
{
    'name' : 'Daydi App',
    'version': '14.0.0.1',
    'category': 'Misc',
    'sequence':10,
    'website':'http://localhost:8069/',
    'depends' : ['base'],
    'description': """
       App test para probar funciones basicas de Odoo y crear un pequeño ecommerce
    """,
    'data': [
        'security/security.xml', 
        'security/ir.model.access.csv',
        'views/inventory.xml'
    ],
    'installable': True,
    'application': True,
}
