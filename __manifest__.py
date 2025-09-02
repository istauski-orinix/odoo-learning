{
	'name': 'library_module',
	'depends': [
		'base',
        'mail',
	],
	'data':[
		'security/ir.model.access.csv',
        'security/library_security.xml',
        'reports/book_report_template.xml',
        'views/library_users_views.xml',
        'views/library_event_kanban.xml',
        'data/library_cron.xml',
        'data/borrowing_reminder_template.xml',
        'views/library_menus.xml',
	],
	'application': True
}
