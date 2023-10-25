from flask import render_template, jsonify, make_response

class CollegeView:

    @staticmethod
    def renderCreateFormAsView():
        rendered_view = render_template('tab_contents/form_template.html', form_content="College")
        return rendered_view

    @staticmethod
    def renderTableAsJSON(model_response):
        headers = ["Code", "College"]
        content = render_template('tab_contents/table_template.html', headers=headers, rows=model_response['response'])
        data = {'content': content}
        return jsonify(data)
    
    @staticmethod
    def renderNoDataAsJSON():
        content = render_template('tab_contents/nodata_template.html', description="colleges", button_text="College")
        data = {'content': content}
        return jsonify(data)
    
    @staticmethod
    def setPayloadToJSON(status_code, payload={}):
        final_payload = payload
        if not final_payload:
            if status_code == 400:
                final_payload = {'response': 'Invalid request data', 'success': False}
            elif status_code == 403:
                final_payload = {'response': 'Forbidden', 'success': False}
        return make_response(jsonify(**final_payload), status_code)