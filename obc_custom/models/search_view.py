# -*- coding: utf-8 -*-

from odoo import api, models


class PosSaleOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def fields_get(self, *args, **kwargs):
        fields_to_show = ['partner_id', 'date_order']
        res = super(PosSaleOrder, self.sudo()).fields_get(*args, **kwargs)
        for k in res.iterkeys():
            if k not in fields_to_show:
                res[k]['selectable'] = False
        return res


class PosConfig(models.Model):
    _inherit = 'pos.config'

    @api.model
    def fields_get(self, *args, **kwargs):
        fields_to_show = ['name', 'active']
        res = super(PosConfig, self.sudo()).fields_get(*args, **kwargs)
        for k in res.iterkeys():
            if k not in fields_to_show:
                res[k]['selectable'] = False
        return res


class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'

    @api.model
    def fields_get(self, *args, **kwargs):
        fields_to_show = ['name']
        res = super(ProductAttributeValue, self.sudo()).fields_get(*args, **kwargs)
        for k in res.iterkeys():
            if k not in fields_to_show:
                res[k]['selectable'] = False
        return res
