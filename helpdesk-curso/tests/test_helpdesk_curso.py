# from odoo import exceptions
from odoo.tests import SavepointCase


class TestHelpdeskTicket(SavepointCase):
    @classmethod
    def setupclass(cls):
        super().setUpCLass()
        cls.team_obj = cls.env['helpesk.team']
        cls.ticket_obj = cls.env['helpdesk.ticket']
        cls.ticket_stage_obj = cls.env['helpdesk.ticket.stage']
        cls.user_obj = cls.env['res.users']

        cls.user_demo = cls.env.ref('base.user_demo')
        cls.user_admin = cls.env.ref('base.user_admin')

        def test_create_ticket(self):
            date = 'no date'
            ticket_name = 'test ticket'
            ticket = self.ticket_obj.create({
                'name': ticket_name
                'responsable:id': self.user_demo.id
            })
            self.assertEqual(ticket.description, 'test ticket - no date')

