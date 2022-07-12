from odoo import models, fields, api
class Wizard (models.TransientModel):
    _name = 'wizard'
    _description = 'Wizard: Quick Registration of Attendees to Sessions'

    def _default_session(self):
        return self.env['session'].browse(self._context.get('active_id'))

    session_id = fields.Many2one('session', string='Session', required=True)
    attendee_ids = fields.Many2many('attendee', string='Attendees')

    def subscribe(self):
        self.session_id.attendee_ids |= self.attendee_ids
        return {}
