from odoo import models, fields
class Course (models.Model):
        _name = 'course'
        _description = 'Open Academy Course'

        name = fields.Char(string = 'Title', required = True)
        description = fields.Text()
        course_img = fields.Image("Course Image")

        responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
        session_ids = fields.One2many('session', 'course_id', string="Sessions")





