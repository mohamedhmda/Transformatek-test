from odoo import http
import json
from base64 import b64encode
import os
import imghdr

class Controller(http.Controller):
    @http.route('/reclamations/', type='http', auth='user', groups='reclamation.group_user', website=True)
    def website_route(self, **kwargs):
        records = http.request.env['ade.reclamation'].search([])
        return http.request.render('reclamations.template', { 'records' : records })

    @http.route('/reclamations/new', type='http', auth='user', groups='reclamation.group_manager', website=True)
    def createForm(self, **kwargs):
        return http.request.render('reclamations.form_template', {})
    
    @http.route('/reclamations/create', type='http', auth='user', groups='reclamation.group_manager', website=True, methods=['POST'])
    def createReclamation(self, **kwargs):
        data = http.request.params

        image_data = http.request.httprequest.files.get('images').read()
        base64_img = b64encode(image_data)

        new_record = http.request.env['ade.reclamation'].create({
            'source': data['source'],
            'type': data['type'],
            'localisation': data['localisation'],
            'images': base64_img
        })

        return http.request.redirect('/reclamations')

    @http.route('/reclamations/api', type='http', auth='user', groups='reclamation.group_user', csrf=False)
    def my_api(self):
        records = http.request.env['ade.reclamation'].search([])

        # serialzer
        data = [
            {
                'id': record.id, 
                'source': record.source,
                'type': record.type,
                'localisation': record.localisation,
                'images': record.images
                # 'date': record.create_date,
            } for record in records
        ]

        return http.Response(json.dumps(data), content_type='application/json')