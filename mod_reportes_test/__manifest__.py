{
    'name': "report test module",
    'version': '1.0',
    'depends': ['base'],
    'author': "Ivan R",
    'category': 'misc',
    'description': """
    Just a simple report module
    """,
    # data files always loaded at installation
    'data': [
        'views/inventory.xml',
        'security/ir.model.access.csv',
        'reports/report.xml',
        'reports/inventory_report.xml'
    ],
    'application':True,
    'installable':True,
}