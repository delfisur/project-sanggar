# -*- coding: utf-8 -*-
# from odoo import http


# class Delficourse(http.Controller):
#     @http.route('/delficourse/delficourse/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delficourse/delficourse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delficourse.listing', {
#             'root': '/delficourse/delficourse',
#             'objects': http.request.env['delficourse.delficourse'].search([]),
#         })

#     @http.route('/delficourse/delficourse/objects/<model("delficourse.delficourse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delficourse.object', {
#             'object': obj
#         })
