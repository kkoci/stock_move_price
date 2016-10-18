# -*- coding: utf-8 -*-

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp 

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    price_unit = fields.Float(string='Precio', digits=dp.get_precision('Product Price'))
    price_unity = fields.Float(string="Precio", store=True, readonly=True, related="product_id.price")
