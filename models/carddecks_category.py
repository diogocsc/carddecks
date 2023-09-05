# -*- coding: utf-8 -*-
from odoo import fields, models

class Category(models.Model):
    _name = "carddecks.category"
    _description = "Category"

    name = fields.Char("Category", required=True, translate=True)
    cards = fields.One2many("carddecks.card", "category", "Cards")
    category_type = fields.Selection([('card', 'Card Category'),
                                      ('deck', 'Deck Category')],
                                     default='card')





