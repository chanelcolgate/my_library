from odoo import models, fields, api

class LibraryBookRent(models.Model):
	_name = 'library.book.rent'

	book_id = fields.Many2one('library.book', 'Book', required=True)
	borrowed_id = fields.Many2one('res.partner', 'Borrower', required=True)
	state = fields.Selection([('ongoing', 'Ongoing'),
							  ('returned', 'Returned')],
							  'State', default='ongoing', required=True)
	rent_date = fields.Date(default=fields.Date.today)
	return_date = fields.Date()

	@api.model
	def create(self, vals):
		book_rec = self.env['library.book'].browse(vals['book_id'])
		book_rec.make_borrowed()
		return super(LibraryBookRent, self).create(vals)

	def book_return(self):
		self.ensure_one()
		self.book_id.make_available()
		self.write({
			'state': 'returned',
			'return_date': fields.Date.today()
		})

class LibraryRentStage(models.Model):
	_name = 'library.rent_stage'
	_order = 'sequence,name'

	name = fields.Char()
	sequence = fields.Integer()
	fold = fields.Boolean()
	book_state = fields.Selection(
		[('available', 'Available'),
		 ('borrowed', 'Borrowed'),
		 ('lost', 'Lost')],
		'State', default="available")