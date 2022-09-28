# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PickingInfoExtended(models.Model):
    _inherit = "stock.picking"

    x_declaration = fields.Char('Declaración de Importación')
    x_itr = fields.Boolean('Requirió ITR')
    x_reempaque = fields.Boolean('Requirió Reempaque')
    x_adicional = fields.Selection([("1", "Reetiquetado"),
                                    ("2", "Reestibado"),
                                    ("3", "Vinipelado"),
                                    ("4", "Zunchado"),
                                    ],"Requirió procesos logísticos adicionales")
    x_contenedor = fields.Char('Contenedor No.')
    x_patio = fields.Char('Patio Devolución Contenedor')
    x_cantidad = fields.Char('Cantidad')
    x_conductor = fields.Char('Conductor')
    x_placa = fields.Char('Placa')
    x_remolque = fields.Char('Remolque')
    x_transportadora = fields.Char('Transportadora')
    x_cedula = fields.Char('Cédula')
    x_celular = fields.Char('Celular')
    required_process_ids = fields.Many2many('stock.required_process')

class StockMoveExtended(models.Model):
    _inherit = "stock.move"

    x_estibas = fields.Integer('Estibas')

class RequiredProcess(models.AbstractModel):

    _name = 'stock.required_process'

    name = fields.Char()

