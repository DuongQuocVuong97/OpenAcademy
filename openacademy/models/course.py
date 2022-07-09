
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

        _sql_constraints = [
                ('name_description_check',
                 'CHECK(name != description)',
                 'The title of the course should not be the description'),
                ('name_unique',
                 'UNIQUE(name)',
                 'The course title must be unique'),
        ]

        @api.model
        def create(self, vals):
                if vals.get('name_seq','New') == 'New':
                        vals['name_seq'] = self.env['ir.sequence'].next_by_code('course.sequence') or 'New'
                result = super(Course, self).create(vals)
                return result


        def copy(self, default=None):
            default = dict(default or {})

            copied_count = self.search_count(
                [('name', '=like', u"Copy of {}%".format(self.name))])
            if not copied_count:
                new_name = u"Copy of {}" .format(self.name)
            else:
                new_name = u"Copy of {} {})".format(self.name, copied_count)

            default['name'] = new_name
            return super(Course, self).copy(default)








