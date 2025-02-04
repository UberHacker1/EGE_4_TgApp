// Инициализация Telegram Web App
const tg = window.Telegram.WebApp;

// Показываем кнопку "Закрыть"
tg.MainButton.setText("Закрыть");
tg.MainButton.show();
tg.MainButton.onClick(() => tg.close());

// Пример данных
const tasks = [
    {
        question: "Укажите варианты ответов, в которых верно выделена буква, обозначающая ударный гласный звук. Запишите номера ответов.",
        options: [
            "1)  созЫв",
            "2)  Отзыв (посла из страны)",
            "3)  дОнизу",
            "4)  оптОвый",
            "5)  аэропортЫ"
        ],
        correctAnswers: [2, 5] // Номера правильных ответов
    },
    {
        question: "Укажите варианты ответов, в которых верно выделена буква, обозначающая ударный гласный звук. Запишите номера ответов.",
        options: [
            "1)  звонИт",
            "2)  красИвее",
            "3)  кУхонный",
            "4)  тОрты",
            "5)  средствА"
        ],
        correctAnswers: [1, 2, 5]
    },
    // Добавьте больше заданий по аналогии
];

// Функция для отображения всех заданий
function displayTasks() {
    const tasksElement = document.getElementById('tasks');
    tasksElement.innerHTML = tasks
        .map((task, taskIndex) => `
            <div class="task">
                <h3>Задание ${taskIndex + 1}:</h3>
                <p>${task.question}</p>
                <div class="options">
                    ${task.options
                        .map((option, index) => `
                            <div class="option">
                                <input type="checkbox" id="task${taskIndex}-option${index + 1}" value="${index + 1}">
                                <label for="task${taskIndex}-option${index + 1}">${option}</label>
                            </div>
                        `)
                        .join('')}
                </div>
            </div>
        `)
        .join('');
}

// Функция для проверки всех ответов
function checkAllAnswers() {
    let correctCount = 0;

    tasks.forEach((task, taskIndex) => {
        const selectedOptions = Array.from(
            document.querySelectorAll(`input[type="checkbox"][id^="task${taskIndex}-"]:checked`)
        ).map(checkbox => parseInt(checkbox.value));

        // Проверяем, совпадают ли выбранные ответы с правильными
        const isCorrect = selectedOptions.length === task.correctAnswers.length &&
            selectedOptions.every(option => task.correctAnswers.includes(option));

        if (isCorrect) {
            correctCount++;
        }
    });

    const resultElement = document.getElementById('result');
    resultElement.textContent = `Правильных ответов: ${correctCount} из ${tasks.length}`;
    resultElement.style.color = correctCount === tasks.length ? "green" : "red";
}

// Инициализация приложения
document.addEventListener('DOMContentLoaded', () => {
    displayTasks();
    document.getElementById('submit').addEventListener('click', checkAllAnswers);
});