from odoo import models, fields, api, exceptions
from datetime import timedelta


class Session(models.Model):
    _name = 'session'
    _description = 'Open Academy Session'

    name = fields.Char(string='Title', required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)

    course_id = fields.Many2one('course', ondelete='cascade', string="Course")
    attendee_ids = fields.Many2many('attendee', string="Attendees")
    instructor_id = fields.Many2one('attendee', string="Instructor", domain="[('instructor','=',True)]")

    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')

    end_date = fields.Date(string="End Date", store=True,
                           compute='_get_end_date', inverse='_set_end_date')

    state = fields.Selection([
        ('in_progress', 'In_Progress'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, default='in_progress')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_notify(self):
        for rec in self:
            rec.doctor_id.user_id.notify_warning(message='Appointment is Confirmed')

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
                    'message': 'The number of available seats can not be negative',
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': 'Too many attendees',
                    'message': 'Increase seats or remove excess attendees',
                },
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            r.duration = (r.end_date - r.start_date).days + 1
