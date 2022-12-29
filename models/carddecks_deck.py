# -*- coding: utf-8 -*-
from odoo import fields, models

class Deck(models.Model):
    _name = "carddecks.deck"
    _description = "Deck"
    name = fields.Char(required=True)
    cards = fields.One2many("carddecks.card", "category", "Cards")