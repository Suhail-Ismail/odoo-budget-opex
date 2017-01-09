# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_core.models.utilities import choices_tuple


class BudgetInherit(models.Model):
    _inherit = 'budget.core.budget'

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------

    # RELATIONSHIPS
    # ----------------------------------------------------------
    account_code_ids = fields.One2many('budget.opex.account.code',
                                       'operation_id',
                                       string="Account Codes")

    # COMPUTE FIELDS
    # ----------------------------------------------------------
