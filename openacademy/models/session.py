from odoo import models, fields
class Session (models.Model):
    _name = 'session'
    _description = 'Open Academy Session'

    name = fields.Char(string = 'Title',required = True)
    start_date = fields.Datetime()
    duration = fields.Float(digits=(6, 2), help = "Duration in days")
    seats = fields.Integer(string = "Number of seats")

    course_id = fields.Many2one('course', ondelete='cascade', string="Course")
    attendee_ids = fields.Many2many('attendee', string="Attendees")
    instructor_id = fields.Many2one('attendee', string="Instructor",domain="[('instructor','=',True)]")

    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
