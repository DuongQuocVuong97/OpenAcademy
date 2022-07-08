from odoo import models, fields, api
class Session (models.Model):
    _name = 'session'
    _description = 'Open Academy Session'

    name = fields.Char(string = 'Title', required = True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help = "Duration in days")
    seats = fields.Integer(string = "Number of seats")
    active = fields.Boolean(default=True)

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

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': 'Incorrect seats value',
                    'message': 'The number of availabale seats can not be negative',
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': 'Too many attendees',
                    'message': 'Increase seats or remove excess attendees',
                },
            }