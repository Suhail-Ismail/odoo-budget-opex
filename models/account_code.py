# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_core.models.utilities import choices_tuple


class AccountCode(models.Model):
    _name = 'budget.opex.account.code'
    _rec_name = 'account_code'
    _description = 'Account Code'
    _inherit = ['mail.thread']

    # CHOICES
    # ----------------------------------------------------------
    year_now = fields.Datetime.from_string(fields.Date.today()).year
    YEARS = [(year, year) for year in range(year_now - 10, year_now + 10)]
    STATES = choices_tuple(['draft', 'under process', 'authorized', 'closed'], is_sorted=False)

    # BASIC FIELDS
    # ----------------------------------------------------------
    state = fields.Selection(STATES, default='draft')

    year = fields.Selection(string='Year', selection=YEARS, default=year_now)
    account_code = fields.Char(string="Account Code", required=True)
    start_date = fields.Date(string="Start Date")
    expenditure_amount = fields.Monetary(currency_field='company_currency_id',
                                         string='Expenditure Amount')

    description = fields.Text(string="Description")
    remarks = fields.Text(string="Remarks")

    # RELATIONSHIPS
    # ----------------------------------------------------------
    company_currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)
    operation_id = fields.Many2one('budget.core.budget',
                                 domain=[('is_operation', '=', True),
                                         ('state', 'not in', ['draft'])],
                                 string='Cost Center'
                                 )
