# -*- coding: utf-8 -*-
from odoo import http


class Openacademy(http.Controller):
     @http.route('/api/session/', auth='public', website=True)
     def create_session(self, **kw):
     new_session: = http.request.env['session'].create({
         'name': 'New Session',
         'course_id': ,
         'instructor_id': ,


     })
     return "A class has been created"




     #     session_data = http.request.env['session'].search([])
     #
     #     return http.request.render('odoo_controller.index', {
     #         'session': session_data,
     #     })




         # output = "<h1>Session Data</h1><ul>"
         #
         # for session in session_data:
         #     output += '<li>' + session['name'] + '</li>'
         # output += "</ul>"
         # return output

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
