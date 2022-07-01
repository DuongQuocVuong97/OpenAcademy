
from odoo import models, fields
class course (models.Model):
        _name = 'openacademy.course'
        _description = 'Open Academy Course'

        name = fields.Char(string = 'Title' , required = 'True')
        description = fields.Text()

        responsible_id = fields.Many2one('res.user', ondelete = 'set null', string = 'Responsible', index = True)

class session (models.Model):
        _name = 'openacademy.session'
        _description = 'OpenAcademy Session'

        name = fields.Char(required=True)
        start_date = fields.Date()
        duration = fields.Float(digits = (6,2), help = 'Duration in days')
        seats = fields.Integer(string = 'Number of seats')

        instructor_id = fields.Many2one('res.partner', string = 'Instructor')
        course_id = fields.Many2one ('openacademy.course',ondelete = 'casade', string = 'Course', required = True)

