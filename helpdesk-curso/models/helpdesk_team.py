from odoo import api, fields, _, models


class HelpdeskTeam(models.Model):
    _name = "helpdesk.team"

    name = fields.Char(string="Name", required=True)
    ticket_ids = fields.One2many(comodel_name="helpdesk.ticket", inverse_name="team_id", string="Tickets")
