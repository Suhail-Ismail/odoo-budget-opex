# -*- coding: utf-8 -*-
from odoo import http

# class BudgetOpex(http.Controller):
#     @http.route('/budget_opex/budget_opex/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/budget_opex/budget_opex/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('budget_opex.listing', {
#             'root': '/budget_opex/budget_opex',
#             'objects': http.request.env['budget_opex.budget_opex'].search([]),
#         })

#     @http.route('/budget_opex/budget_opex/objects/<model("budget_opex.budget_opex"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('budget_opex.object', {
#             'object': obj
#         })