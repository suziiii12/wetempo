const dataToSend = {
    key: "value",
    anotherKey: "anotherValue"
};

fetch('/getdata/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')  // CSRF 토큰을 헤더에 추가
    },
    body: JSON.stringify(dataToSend),  // 데이터를 JSON으로 변환해 전송
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);  // Django에서 보낸 응답을 출력
})
.catch((error) => {
    console.error('Error:', error);
});

// CSRF 토큰을 가져오는 함수
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
