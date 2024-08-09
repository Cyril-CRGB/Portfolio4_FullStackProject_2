let nav = 0;
let clicked = null;
let events = localStorage.getItem('events') ? JSON.parse(localStorage.getItem('events')) : [];

const calendar = document.getElementById('calendar');
// const newEventModal = document.getElementById('newEventModal');
// const deleteEventModal = document.getElementById('deleteEventModal');
// const backDrop = document.getElementById('modalBackDrop');
// const eventTitleInput = document.getElementById('eventTitleInput');
const weekdays = ['Sunday', 'Monday', 'Tuesday', "Wednesday", 'Thursday', 'Friday', 'Saturday'];

function openModal(date){
    clicked = date;
    const eventForDay = events.find(e => e.date === clicked);
    if (eventForDay) {
        if (eventForDay.title === userName || isStaff === 'True'){
            // User is allowed to delete the event
            const confirmDelete = confirm("Do you want to delete the booking?");
            if (confirmDelete){
                events = events.filter(e => e.date !== clicked);
                localStorage.setItem('events', JSON.stringify(events));
            }

        } else {
            // User is not allowed to delete the event
            alert("You can only unbook your own booking.");
            return; // Exit the function to prevent deletion
        }

    } else {
        // If the event does not exist, add it (user's name is not there, so add it)
        events.push({
            date: clicked,
            title: userName, // Use the globally available userName
        });
        localStorage.setItem('events', JSON.stringify(events));
    }

    load(); // Reload the calendar to sho the updated events
}

function load() {
    const dt = new Date();

    if (nav !== 0) {
        dt.setMonth(new Date().getMonth() + nav);
    }

    const day = dt.getDate();
    const month = dt.getMonth();
    const year = dt.getFullYear();

    const firstDayOfMonth = new Date(year, month, 1);
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    const dateString = firstDayOfMonth.toLocaleDateString('en-us', {
        weekday: 'long',
        year: 'numeric',
        month: 'numeric',
        day: 'numeric',
    });
    const paddingDays = weekdays.indexOf(dateString.split(',')[0]);

    document.getElementById('monthDisplay').innerText = `${dt.toLocaleDateString('en-us', { month: 'long'})} ${year}`;
    
    calendar.innerHTML = '';

    // Calculate total squares
    const totalSquares = paddingDays + daysInMonth;
    const rows = Math.ceil(totalSquares / 7);
    const totalGridSquares = rows * 7;

    for (let i = 1; i <= totalGridSquares; i++) {
        const daySquare = document.createElement('div');
        daySquare.classList.add('day');

        if (i > paddingDays && i <= paddingDays + daysInMonth) {
            const dayString = `${month + 1}/${i - paddingDays}/${year}`;
            daySquare.innerText = i - paddingDays;

            if (i - paddingDays === day && nav === 0) {
                daySquare.id = 'currentDay';
                daySquare.innerText += " Today";
            }

            const eventForDay = events.find(e => e.date === dayString);
            if (eventForDay) {
                const eventDiv = document.createElement('div');
                eventDiv.classList.add('event');
                eventDiv.innerText = eventForDay.title;
                daySquare.appendChild(eventDiv);
            }

            daySquare.addEventListener('click', () => openModal(dayString));
        } else {
            daySquare.classList.add('padding');
        }
        calendar.appendChild(daySquare);
    }
}
   
function initButtons() {
    document.getElementById('nextButton').addEventListener('click', () => {
        nav++;
        load();
    });

    document.getElementById('backButton').addEventListener('click', () => {
        nav--;
        load();
    });


}

initButtons();
load();

console.log("Script Loaded successfully!")

