# -*- coding: utf-8 -*-

from odoo import models


class ResUsers(models.Model):
    _inherit = 'res.users'

    _defaults = {
        'notify_email': 'none',
        'email': 'test@test.com'
    }
