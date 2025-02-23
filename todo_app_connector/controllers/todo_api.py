from odoo import http
from odoo.http import request, Response
import json
import logging

_logger = logging.getLogger(__name__)

class TodoApiController(http.Controller):
    
    @http.route('/todo/api/tasks', auth='public', methods=['GET'], csrf=False)
    def get_tasks(self):
        try:
            tasks = request.env['todo.task'].sudo().search([])


            print(f'tasks: {len(tasks)}')

            task_data = tasks.read(['id', 'name', 'description', 'deadline', 'state', 'priority'])
            
            return Response(json.dumps({"error": False, "data": task_data},default=str), content_type='application/json')
        except Exception as e:
            _logger.error(e)
            return Response(json.dumps({'error': True, "message": str(e)}, default=str), content_type='application/json', status=500)
                
    @http.route('/todo/api/tasks', auth='public', methods=['POST'], csrf=False)
    def create_task(self, **kwargs):
        try:
            body = request.get_json_data()
            task = request.env['todo.task'].sudo().create(body)
            task = task.read(['id', 'name', 'description', 'deadline', 'state', 'priority'])
            return Response(json.dumps({"error": False, "data": task},default=str), content_type='application/json')
        except Exception as e:
            _logger.error(e)
            return Response(json.dumps({'error': True, "message": str(e)}, default=str), content_type='application/json', status=500)
                
    @http.route('/todo/api/tasks/<int:task_id>', auth='public', methods=['PUT'], csrf=False)
    def update_task(self, task_id):
        try:
            task = request.env['todo.task'].sudo().search([('id', '=', task_id)])
            if not task:
                return Response(json.dumps({'error': True, "message": "Task not found"}, default=str), content_type='application/json', status=404)
            body = request.get_json_data()
            task.write(body)
            task = task.read(['id', 'name', 'description', 'deadline', 'state', 'priority'])
            return Response(json.dumps({"error": False, "data": task},default=str), content_type='application/json')

        except Exception as e:
            _logger.error(e)
            return Response(json.dumps({'error': True, "message": str(e)}, default=str), content_type='application/json', status=500)
        
    @http.route('/todo/api/tasks/<int:task_id>', auth='public', methods=['DELETE'], csrf=False)
    def delete_task(self, task_id):
        try:
            task = request.env['todo.task'].sudo().search([('id', '=', task_id)])
            if not task:
                return Response(json.dumps({'error': True, "message": "Task not found"}, default=str), content_type='application/json', status=404)
            task.unlink()
            return Response(json.dumps({"error": False, "message": "Task deleted"},default=str), content_type='application/json')
        except Exception as e:
            _logger.error(e)
            return Response(json.dumps({'error': True, "message": str(e)}, default=str), content_type='application/json', status=500)