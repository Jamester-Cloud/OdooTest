from odoo import api,fields,models


class Inventory(models.Model):
    #module name
    _name='inventory.app'
    #module descrition
    _description='modelo del inventario'
    #Self env for relational field description in draw app
    #draw_description=fields.One2many('', '', string='')
    #using a def function on it
    #
    #id de pago
    cantidad = fields.Integer(string='cantidad')
    #Mayorista, minorista
    tipoventa=fields.Char("tipo de venta", compute='_compute_something')
    #imagen producto
    imagen = fields.Binary("ingrese imagen del producto")
    #valor del producto
    valor=fields.Integer('Valor del producto')
    #total de entre el valor y la cantidad
    total = fields.Char("total", compute='_compute_valor')

    #mayor o menor
    @api.depends('cantidad')
    def _compute_something (self):
        if  self.cantidad < 13:
            self.tipoventa='Minorista'
        else:
            self.tipoventa="Mayorista"
    #valores de venta
    @api.onchange('valor')
    def _compute_valor (self):
            self.total = self.valor * self.cantidad
