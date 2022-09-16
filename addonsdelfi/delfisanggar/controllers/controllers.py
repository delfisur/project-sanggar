# -*- coding: utf-8 -*-
# from odoo import http


# class Delfisanggar(http.Controller):
#     @http.route('/delfisanggar/delfisanggar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delfisanggar/delfisanggar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delfisanggar.listing', {
#             'root': '/delfisanggar/delfisanggar',
#             'objects': http.request.env['delfisanggar.delfisanggar'].search([]),
#         })

#     @http.route('/delfisanggar/delfisanggar/objects/<model("delfisanggar.delfisanggar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delfisanggar.object', {
#             'object': obj
#         })
