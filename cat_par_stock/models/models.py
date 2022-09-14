
from odoo import  api, fields,models

class Picking(models.Model):
    _inherit = 'stock.picking'



class StockMove(models.Model):
    _inherit = 'stock.move'
    cus_account_stock= fields.Many2one('account.account',string='Account')





    
