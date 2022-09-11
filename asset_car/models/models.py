# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountAsset(models.Model):
    _inherit = "account.asset"
    
    car_is = fields.Boolean(
        string='Is Car', default=False
    )

    
    vehicle_registration_expired = fields.Date(
        string='Vehicle registration expired',
        default=fields.Date.context_today
    )

    # Date of the periodic examination

    date_of_the_periodic_examination = fields.Date(
        string='Date Of The Periodic Examination',
        default=fields.Date.context_today
    )

    # Periodic maintenance history
    
    periodic_maintenance_history = fields.Date(
        string='Periodic Maintenance History',
        default=fields.Date.context_today
    )
    






