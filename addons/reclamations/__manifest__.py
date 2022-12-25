{
    'name': 'Reclamations',
    'version': '1.0',
    'category': 'Tools',
    'sequence': -100,
    'description': 'Gestion de reclamation d eau',
    'depends': ['website'],
    'installable': True,
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/form.xml',
        'views/template.xml',
    ],
}