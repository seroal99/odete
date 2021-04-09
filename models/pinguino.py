from odoo import models, fields, api, exceptions

class Pinguino(models.Model):
    _name = 'simuexamen.pinguino'

    name = fields.Char(string="Nombre")
    raza = fields.Char(string="Raza")
    habitat = fields.Selection([
            ('1.cautividad', 'Cautividad'),
            ('2.zoologico', 'Zoologico'),
        ], string='Habitat', default='1.cautividad')
    asociacion_id = fields.Many2one('simuexamen.asociacion_id', string="asociacion", ondelete='cascade', required=True)