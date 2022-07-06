from odoo import models, fields
class course (models.Model):
        _name = 'openacademy.course'
        _description = 'Open Academy Course'

        name = fields.Char(string = 'Title', required = True)
        description = fields.Text()
        course_img = fields.Image("Course Image")

        responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
        session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")





