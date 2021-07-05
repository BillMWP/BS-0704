# -*- coding: utf-8 -*-

from odoo import http

from odoo.addons.website_sale.controllers.main import WebsiteSale


class ProductAttribute(WebsiteSale):
    @http.route()
    def shop(self, page=0, category=None, search="", ppg=False, **post):
        response = super(ProductAttribute, self).shop(
            page=page, category=category, search=search, ppg=ppg, **post
        )
        response.qcontext["attributes"] = response.qcontext["attributes"].filtered(
            "show_in_attribute_filter"
        )
        return response
