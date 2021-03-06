# -*- coding: utf-8 -*-
{
	'name': "My Library", # Module title
	'summary': "Manage books easily", # Module subtitle phrase
	'description': """
Manage Library
==============
Description related to library.
	""", # Supports reStructuredText(RST) format
	'author': "Parth Gajjar",
	'website': "http://www.example.com",
	'category': 'Tools',
	'version': '14.0.1',
	'depends': ['base', 'contacts', 'website'],
	# This data files will be loaded at the installation (commented because file is not added in this example)
	 'data': [
	 	'security/groups.xml',
	 	'security/ir.model.access.csv',
		'views/library_book.xml',
		'views/library_book_categ.xml',
		'views/library_book_rent.xml',
		'views/templates.xml',
		'views/snippets.xml',
		'data/library_stage.xml',
		'report/book_rent_templates.xml',
		'report/book_rent_report.xml',
	],
	# This demo data files wll be loaded if db initialize with demo data (commented because file is not added in this example)
	'demo': [
		'data/demo.xml'
	],
}