from flask import render_template, jsonify, make_response

class StudentView:

    @staticmethod
    def renderTableAsJSON(model_response):
        headers = ["ID", "First Name", "Last Name", "Course", "Year", "Gender"]
        data = {'content': render_template('content/table_template.html', headers=headers, rows=model_response['response'])}
        return jsonify(data)
    
    @staticmethod
    def renderNoDataAsJSON():
        data = {'content': render_template('content/nodata_template.html', description="students", button_text="Student")}
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