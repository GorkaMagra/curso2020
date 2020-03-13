from odoo import api, fields, _, models


class HelpdeskTicketStage(models.Model):
    _name = "helpdesk.ticket.stage"

    name = fields.Char(string="Name", required=True)
