# -*- coding: utf-8 -*-
from openerp import http

# class Immo(http.Controller):
#     @http.route('/immo/immo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/immo/immo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('immo.listing', {
#             'root': '/immo/immo',
#             'objects': http.request.env['immo.immo'].search([]),
#         })

#     @http.route('/immo/immo/objects/<model("immo.immo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('immo.object', {
#             'object': obj
#         })