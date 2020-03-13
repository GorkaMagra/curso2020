from odoo import api, fields, _, models


class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"

    _inherit = ["mail.thread.cc", "mail.activity.mixin"]

    name = fields.Char(string="Name", required=True)
    description = fields.Text('Description')
    date_deadline = fields.Datetime('Date limit')
    stage_id = fields.Many2one(comodel_name='ticket.stage', string='Stage', required=False)
    team_id = fields.Many2one(comodel_name="helpdesk.team", string="Team")
    user_ids = fields.Many2many(comodel_name="res.users", relation="helpdesk_ticket_users_rel",
                                column1="ticket_id", column2="user_id", string="Users")
    responsable_id = fields.Many2one(comodel_name="res.users", String="Responsable")

    ticket_qty = fields.Integer(string="TIckets Qty", compute="_compute_tickets_qty")

    @api.depends('responsable_id')
    def _compute_tickets_qty(self):
        ticket_obj = self.env['helpdesk.ticket']
        for ticket in self:
            tickets = ticket_obj.search_count([('responsable_id', '=', ticket.responsable_id.id)])
            ticket.ticket_qty = tickets

    def set_responsable(self):
        self.ensure_one()
        self.responsable_id = self.env.user

    @api.onchange('name', 'date_deadline')
    def _onchange_description(self):
        if self.name and self.description:
            self.description = "{} - {}".format(self.name, self.date_deadline)
