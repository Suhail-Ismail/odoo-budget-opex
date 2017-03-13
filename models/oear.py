# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple


class Oear(models.Model):
    _name = 'budget.opex.oear'
    _rec_name = 'request_no'
    _description = 'OEAR'
    _inherit = ['mail.thread']

    # CHOICES
    # ----------------------------------------------------------
    year_now = fields.Datetime.from_string(fields.Date.today()).year
    YEARS = [(year, year) for year in range(year_now - 10, year_now + 10)]
    STATES = choices_tuple(['draft', 'active', 'closed'], is_sorted=False)

    # BASIC FIELDS
    # ----------------------------------------------------------
    state = fields.Selection(STATES, default='draft')

    request_no = fields.Char(string="Request No")
    approval_no = fields.Char(string="Approval No")
    budget_type = fields.Char(string="Budget Type")
    reference = fields.Char(string="Reference")
    originator = fields.Char(string="Originator")
    title = fields.Char(string="Title")
    expenditure_amount = fields.Monetary(currency_field='company_currency_id',
                                         string='Expenditure Amount')
    justification = fields.Text(string="Justification")
    purchase_order = fields.Char(string="Purchase Order")

    received_date = fields.Date(string="Received Date")
    approval_date = fields.Date(string="Approval Date")

    remark = fields.Text(string="Remarks")

    # RELATIONSHIPS
    # ----------------------------------------------------------
    company_currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)

    section_id = fields.Many2one('budget.enduser.section')
    sub_section_id = fields.Many2one('budget.enduser.sub.section')

    operation_id = fields.Many2one('budget.core.budget',
                                 domain=[('is_operation', '=', True),
                                         ('state', 'not in', ['draft'])],
                                 string='CC - AC'
                                 )
