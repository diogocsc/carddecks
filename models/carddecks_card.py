# -*- coding: utf-8 -*-
from odoo import fields, models

class Card(models.Model):
    _name = "carddecks.card"
    _description = "Card"
    cardText = fields.Char("Card Text", required=True)
    url = fields.Char("Card Image URL")
    source = fields.Char("Card Source of Inspiration")
    category = fields.Many2one("carddecks.category", "Category")
    deck = fields.Many2one("carddecks.deck", "Deck")




