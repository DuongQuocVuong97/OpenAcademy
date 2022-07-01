from odoo import models, fields
class course (models.Model):
        _name = 'openacademy.course'
        _description = 'Open Academy Course'

        name = fields.Char(string = "Title" , required = "True")
        description = fields.Text()