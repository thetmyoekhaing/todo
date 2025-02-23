from odoo import models, fields

class TodoModel(models.Model):
    _name = "todo.task"
    _description = "Todo Model"
    _order = 'priority desc, deadline asc'

    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    deadline = fields.Date("Deadline")
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], default='new', string="Status")
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], default='medium', string="Priority")
    
    