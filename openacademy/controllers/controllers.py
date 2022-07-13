# -*- coding: utf-8 -*-
from odoo import http
import logging
import json

_logger = logging.getLogger(__name__)


class CourseController(http.Controller):
    @http.route('/api', auth='public', website=False, csrf=False, type='json', methods=['get', 'POST'])
    def create(self, **kw):
        # add information in database to API postman
        contacts = http.request.env['course'].search([])
        contact_list = []
        for contact in contacts:
            contact_list.append({
                'name_seq': contact.name_seq,
                'name': contact.name,
                'description': contact.description,
            })
        return contact_list

    @http.route('/api/insert', auth='public', website=False, csrf=False, type='json', methods=['get', 'POST'])
    def add(self, **kw):
        insert = http.request.env['course'].sudo().create({
            'name_seq': kw.get('name_seq'),
            'name': kw.get('name'),
            'description': kw.get('description')
        }).id
        return json.dumps(insert)

#     @http.route('/openacademy/openacademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacademy.listing', {
#             'root': '/openacademy/openacademy',
#             'objects': http.request.env['openacademy.openacademy'].search([]),
#         })

#     @http.route('/openacademy/openacademy/objects/<model("openacademy.openacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy.object', {
#             'object': obj
#         })
