from flask import render_template, jsonify, make_response

class StudentView:

    @staticmethod
    def renderCreateFormAsView(action, **data):
        rendered_view = render_template('tab_contents/form_template.html', form_content="Student", action=action, **data)
        return rendered_view

    @staticmethod
    def renderTableAsJSON(render_model):
        headers = ["ID", "First Name", "Last Name", "Course", "Year", "Gender"]
        content = render_template('tab_contents/table_template.html', button_id='Student', headers=headers, rows=render_model)
        buttons = render_template('tab_contents/button_controls_template.html', button_id='Student')
        data = {'content': content, 'buttons': buttons}
        return jsonify(data)
    
    @staticmethod
    def renderNoDataAsJSON():
        content = render_template('tab_contents/nodata_template.html', description="students", button_text="Student")
        data = {'content': content}
        return jsonify(data)
    
    @staticmethod
    def setPayloadToJSON(status_code, payload={}):
        final_payload = payload
        if not final_payload:
            if status_code == 400:
                final_payload = {'results': 'Invalid request data', 'success': False}
            elif status_code == 403:
                final_payload = {'results': 'Forbidden', 'success': False}
        return make_response(jsonify(**final_payload), status_code)