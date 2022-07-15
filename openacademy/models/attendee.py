from odoo import models, fields
class Attendee (models.Model):
    _name = 'attendee'

    name = fields.Char(string='Name Attenders', required=True)
    session_ids = fields.Many2many('session', string='Attended Sessions')

class AttendeeInfo(models.Model):
    _name = 'attendee'
    _inherit = 'attendee'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    instructor = fields.Boolean(string="Instructor", default=False)

    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, "{} {}".format(record.id, record.name)))
        return res

