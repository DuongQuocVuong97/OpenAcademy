from odoo import models, fields
class session (models.Model):
    _name = 'openacademy.session'
    _description = 'Open Academy Session'

    name = fields.Char(string = 'Title',required = True)
    start_date = fields.Datetime()
    duration = fields.Float(digits=(6, 2), help = "Duration in days")
    seats = fields.Integer(string = "Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)