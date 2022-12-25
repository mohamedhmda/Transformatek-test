from odoo import models, fields, api

class Reclamation(models.Model):
    _name = 'ade.reclamation'
    _description= 'Reclamation'

    source = fields.Selection([
        ('telephone','telephone'), ('email','email'), ('social media','social media'), ('autre','autre')
        ], string="Source", default="telephone")
    localisation = fields.Char('Localisation', required=True)
    type = fields.Selection([
        ('eaux potable','eaux potable'),('assainissement','assainissement')
        ], string="Type", default="eaux potable")
    images = fields.Char('images')