
document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        timeZone: 'UTC',
        initialView: 'dayGridMonth',
        events: [],
        headerToolbar: {
            center: 'addEventButton icsUploadButton icsDownloadButton'
        },
        customButtons: {
            addEventButton: {
                text: "일정 추가",
                click: function () {
                    $("#calendarModal").modal("show");

                    $("#addCalendar").on("click", function () {
                        var content = $("#calendar_content").val();
                        var start_date = $("#calendar_start_date").val();
                        var start_time = $("#calendar_start_time").val();
                        var end_date = $("#calendar_end_date").val();
                        var end_time = $("#calendar_end_time").val();
                        var location = $("#calendar_location").val();
                        var description = $("#calendar_description").val();

                        if (content == null || content == "") {
                            alert("내용을 입력하세요.");
                        } else if (start_date == "" || end_date == "" || start_time == "" || end_time == "") {
                            alert("날짜와 시간을 입력하세요.");
                        } else if (new Date(end_date + ' ' + end_time) - new Date(start_date + ' ' + start_time) < 0) {
                            alert("종료일이 시작일보다 먼저입니다.");
                        } else {
                            var startDateTime = new Date(start_date + ' ' + start_time);
                            var endDateTime = new Date(end_date + ' ' + end_time);
                            var eventData = {
                                "title": content,
                                "start": startDateTime.toISOString(),
                                "end": endDateTime.toISOString(),
                                "location": location,
                                "description": description,
                                "username": localStorage.getItem("username")  // 유저명 저장
                            };

                            // 캘린더에 일정 추가
                            calendar.addEvent(eventData);

                            // 백엔드로 일정 저장 요청
                            $.ajax({
                                url: 'http://localhost:5000/save_event',
                                method: 'POST',
                                contentType: 'application/json',
                                data: JSON.stringify(eventData),
                                success: function (response) {
                                    alert('일정이 저장되었습니다.');
                                    $("#calendarModal").modal("hide");
                                },
                                error: function (xhr, status, error) {
                                    alert('일정 저장에 실패했습니다.');
                                }
                            });
                        }
                    });
                }
            }
        },
        editable: true,
        displayEventTime: true
    });
    
    calendar.render();

    // 페이지 로드 시 사용자명 입력받기
    var username = prompt("사용자명을 입력하세요:", "user1");
    localStorage.setItem("username", username);  // 유저명 로컬에 저장

    // 해당 유저의 일정 불러오기
    $.ajax({
        url: `http://localhost:5000/get_events/${username}`,
        method: 'GET',
        success: function (data) {
            if (data.ics) {
                var parsedEvents = parseICS(data.ics);
                parsedEvents.forEach(function (event) {
                    calendar.addEvent({
                        title: event.summary,
                        start: event.start.toISOString(),
                        end: event.end.toISOString(),
                        location: event.location,
                        description: event.description
                    });
                });
            }
        },
        error: function (xhr, status, error) {
            console.error('일정 불러오기에 실패했습니다.', error);
        }
    });

    function parseICS(icsData) {
        var jcal = ICAL.parse(icsData);
        var comp = new ICAL.Component(jcal);
        var vevents = comp.getAllSubcomponents('vevent');
        var events = [];

        vevents.forEach(function (vevent) {
            var event = {
                summary: vevent.getFirstPropertyValue('summary'),
                start: vevent.getFirstPropertyValue('dtstart').toJSDate(),
                end: vevent.getFirstPropertyValue('dtend').toJSDate(),
                location: vevent.getFirstPropertyValue('location'),
                description: vevent.getFirstPropertyValue('description')
            };
            events.push(event);
        });

        return events;
    }
});
