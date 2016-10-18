# -*- coding: utf-8 -*-

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp 

class product(models.Model):
    _inherit = 'product.product'
    _rec_name = 'price_unidad'

    price_unidad = fields.One2many('product.product','price', string="Precio", readonly=True)

class StockMove(models.Model):
    #_inherit = 'product.product'
    _inherit = 'stock.move'

    @api.model
    def create(self,vals):
        _logger.info(vals)
        #if 'linked_move_operation_ids' in vals:
        #    move = vals['linked_move_operation_ids'][0].move_id
        #    if move.procurement_id.sale_line_id:
        #        vals['operation_line_tax_ids'] = move.move_line_tax_ids.ids
        #        vals['price_untaxed'] = move.price_untaxed
        #        vals['price_unit'] = move.price_unit
        #        vals['discount'] = move.discount
        #        vals['subtotal'] = 0
        return super(StockMove,self).create(vals)

    #@api.onchange('name','product_id','move_line_tax_ids','product_uom_qty')

    price_unit = fields.Float(string='Precio', digits=dp.get_precision('Product Price'))
    price_unity = fields.Many2one("product", string="Precio", readonly=True)
    #price_unity = fields.Float(related="product.price", string="Precio", readonly=True)
