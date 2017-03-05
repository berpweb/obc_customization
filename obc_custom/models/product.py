# -*- coding: utf-8 -*-

from odoo import api, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.multi
    def write(self, vals):
        if 'available_in_pos' in vals:
            vals['active'] = vals['available_in_pos']
        return super(ProductTemplate, self).write(vals)

    @api.model
    def fields_get(self, *args, **kwargs):
        fields_to_show = ['name']
        res = super(ProductTemplate, self.sudo()).fields_get(*args, **kwargs)
        for k in res.iterkeys():
            if k not in fields_to_show:
                res[k]['selectable'] = False
        return res

    _defaults = {
        'list_price': 0,
    }


class PosProductCategory(models.Model):
    _inherit = 'pos.category'

    @api.model
    def fields_get(self, *args, **kwargs):
        fields_to_show = ['name', 'parent_id']
        res = super(PosProductCategory, self.sudo()).fields_get(*args, **kwargs)
        for k in res.iterkeys():
            if k not in fields_to_show:
                res[k]['selectable'] = False
        return res
