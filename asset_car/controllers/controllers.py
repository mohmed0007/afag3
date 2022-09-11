# -*- coding: utf-8 -*-
# from odoo import http


# class AssetCar(http.Controller):
#     @http.route('/asset_car/asset_car', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asset_car/asset_car/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('asset_car.listing', {
#             'root': '/asset_car/asset_car',
#             'objects': http.request.env['asset_car.asset_car'].search([]),
#         })

#     @http.route('/asset_car/asset_car/objects/<model("asset_car.asset_car"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asset_car.object', {
#             'object': obj
#         })
