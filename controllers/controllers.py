# -*- coding: utf-8 -*-
from odoo import http

# class ApiInterface(http.Controller):
#     @http.route('/api_interface/api_interface/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/api_interface/api_interface/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('api_interface.listing', {
#             'root': '/api_interface/api_interface',
#             'objects': http.request.env['api_interface.api_interface'].search([]),
#         })

#     @http.route('/api_interface/api_interface/objects/<model("api_interface.api_interface"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('api_interface.object', {
#             'object': obj
#         })