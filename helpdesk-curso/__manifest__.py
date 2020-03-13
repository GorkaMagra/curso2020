{
	"name": "HelpDesk Curso",
	"summary":
		"Module to support Teams",
	"version": "13.0.1.0.0",
	"category": "Customer Rleationship Management",
	"website": "",
	"author": "Gorka Magra Tolosa <gorkamagra@digital5.es>",
	"license": "AGPL-3",

	"depends": [
		"base",
		"mail",
	],

	"data": [
		"security/helpdesk_security.xml",
		"security/ir.model.access.csv",

		"views/menu_views.xml",
		"wizards/helpdesk_set_responsable_views.xml",
		"views/helpdesk_ticket_views.xml",
		"views/helpdesk_ticket_stage_views.xml",
		"views/helpdesk_team_views.xml",
		"views/res_users_views.xml",
	],

	"application": True,
	"installable": True,
}
