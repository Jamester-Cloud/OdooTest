#importing all odoo basic fields
from odoo import api, fields, models

class Inventory(models.Model):
    #odoo basic name
    _name="inventory.app"
    _description="this is for test purpose"
    #Imagen para el producto
    imagen = fields.Binary()
    #Campo name para los registros
    name=fields.Char("Producto")
    #cantidad del producto, determinara su valor final
    cantidad=fields.Integer("Cantidad")
    #calculo del valor
    valor = fields.Integer("valor")
    #calculando el valor total de la mercancia
    total = fields.Integer("Valor total", compute="_compute_valor")
    @api.depends('cantidad')
    def _compute_valor(self):
        self.total = self.cantidad * self.valor


        
