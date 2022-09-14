# -*- coding: utf-8 -*-
# from odoo import http


# class CatParStock(http.Controller):
#     @http.route('/cat_par_stock/cat_par_stock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cat_par_stock/cat_par_stock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cat_par_stock.listing', {
#             'root': '/cat_par_stock/cat_par_stock',
#             'objects': http.request.env['cat_par_stock.cat_par_stock'].search([]),
#         })

#     @http.route('/cat_par_stock/cat_par_stock/objects/<model("cat_par_stock.cat_par_stock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cat_par_stock.object', {
#             'object': obj
#         })
