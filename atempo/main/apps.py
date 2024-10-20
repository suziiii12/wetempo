# from django.apps import AppConfig
# import os
# import icalendar
# from datetime import datetime


# class MainConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'main'

# app = Flask(__name__)

# # 파일 경로 설정
# BASE_DIR = 'D:\\wetempo'  # 폴더 경로
# ICS_FILE = os.path.join(BASE_DIR, 'user1.ics')

# # 사용자 ICS 파일 생성 및 로드
# def load_ics_file():
#     if not os.path.exists(ICS_FILE):
#         with open(ICS_FILE, 'wb') as f:
#             f.write(b'BEGIN:VCALENDAR\nVERSION:2.0\nEND:VCALENDAR\n')  # 빈 VCALENDAR 생성

# def save_event_to_ics(event):
#     load_ics_file()
    
#     with open(ICS_FILE, 'rb') as f:
#         gcal = icalendar.Calendar.from_ical(f.read())

#     # 새 이벤트 추가
#     ical_event = icalendar.Event()
#     ical_event.add('summary', event['title'])
#     ical_event.add('dtstart', datetime.fromisoformat(event['start']))
#     ical_event.add('dtend', datetime.fromisoformat(event['end']))
#     ical_event.add('location', event.get('location', ''))
#     ical_event.add('description', event.get('description', ''))

#     gcal.add_component(ical_event)

#     with open(ICS_FILE, 'wb') as f:
#         f.write(gcal.to_ical())

# @app.route('/save_event', methods=['POST'])
# def save_event():
#     try:
#         event = request.json
#         save_event_to_ics(event)
#         return jsonify({"message": "Event saved successfully."}), 200
#     except Exception as e:
#         return jsonify({"error": f"Error saving event: {str(e)}"}), 400

# @app.route('/get_events/<username>', methods=['GET'])
# def get_events(username):
#     load_ics_file()
#     with open(ICS_FILE, 'rb') as f:
#         ics_data = f.read()
#     return ics_data, 200, {'Content-Type': 'text/calendar'}

# if __name__ == '__main__':
#     app.run(debug=True)
