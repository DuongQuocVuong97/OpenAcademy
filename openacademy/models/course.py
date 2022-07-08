
from odoo import models, fields, api
class Course (models.Model):
        _name = 'course'
        _description = 'Open Academy Course'
        _rec_name = 'name_seq'

        # id_compute = fields.Integer(string="ID", default=0, compute='_compute_id')
        name_seq = fields.Char(string="Course ID", readonly=True, required=True, copy=False,
                               default=lambda self:self.env['ir.sequence'].next_by_code('course.sequence'))
        name = fields.Char(string = 'Title', required = True)
        description = fields.Text()
        course_img = fields.Image("Course Image")

        responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
        session_ids = fields.One2many('session', 'course_id', string="Sessions")

        @api.model
        def create(self, vals):
                if vals.get('name_seq','New') == 'New':
                        vals['name_seq'] = self.env['ir.sequence'].next_by_code('course.sequence') or 'New'
                result = super(Course, self).create(vals)
                return result









