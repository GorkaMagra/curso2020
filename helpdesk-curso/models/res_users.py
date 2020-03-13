from odoo import fields, api, _, models


class Users(models.Model):
    _inherit = "res.users"

    helpdesk_code = fields.Char(string="Helpdesk Code")
    ticket_ids = fields.Many2many(comodel_name="helpdesk.ticket", relation="helpdesk_ticket_users_rel",
                                  column1="user_id", column2="ticket_id", string="Tickets")
