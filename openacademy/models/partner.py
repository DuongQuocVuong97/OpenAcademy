from odoo import models, fields
class partner (models.Model):
    _inherit = 'res.partner'
    #instructors
    instructor = fields.Boolean('Instructor', default = False)
    session_ids = fields.Many2many('openacademy.session', string = 'Attended Sessions', readonly = True)

