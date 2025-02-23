{
    'name': 'To-Do Application',
    'version': '1.0',
    'summary': 'Manage personal tasks',
    'description': """
        Advanced To-Do application with dashboard and REST API
    """,
    'category': 'Productivity',
    'author': 'Thet Myoe Khaing',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}