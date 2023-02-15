# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Card(models.Model):

    _inherit = "carddecks.imageurl"
    _name = "carddecks.card"
    _description = "Card"
    cardText = fields.Char("Card Text", required=True, translate=True)
    url = fields.Char("Card Image URL")
    image = fields.Binary(string="Image", store=True, attachment=False)
    source = fields.Char("Card Source of Inspiration", translate=True)
    category = fields.Many2one("carddecks.category", "Category")
    deck = fields.Many2one("carddecks.deck", "Deck")

    @api.depends("url")
    @api.onchange('url')
    def _compute_image(self):
        for record in self:
            image = None
            if record.url:
                image = self.get_image_from_url(record.url)
            record.update({"image": image, })
