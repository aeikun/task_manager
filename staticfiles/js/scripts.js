document.addEventListener("DOMContentLoaded", () => {
    const taskForm = document.getElementById('task-form');
    const taskList = document.getElementById('task-list');

    // Function to fetch tasks from API and display them
    function loadTasks() {
        fetch('/api/tasks/')
            .then(response => response.json())
            .then(data => {
                taskList.innerHTML = ''; // Clear the list before adding tasks
                data.forEach(task => {
                    const taskItem = document.createElement('div');
                    taskItem.className = 'card mb-2';
                    taskItem.innerHTML = `
                        <div class="card-body">
                            <h5 class="card-title">${task.title}</h5>
                            <p class="card-text">${task.description}</p>
                            <p class="card-text"><small class="text-muted">Due: ${task.due_date}</small></p>
                            <p class="card-text"><strong>Status:</strong> ${task.status}</p>
                        </div>
                    `;
                    taskList.appendChild(taskItem);
                });
            })
            .catch(error => console.error('Error fetching tasks:', error));
    }

    // Event listener for task form submission
    taskForm.addEventListener('submit', (event) => {
        event.preventDefault();
        
        const taskData = {
            title: document.getElementById('title').value,
            description: document.getElementById('description').value,
            due_date: document.getElementById('due_date').value,
            priority: document.getElementById('priority').value
        };

        // Send the new task to the API
        fetch('/api/tasks/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(taskData)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Task created:', data);
            loadTasks(); // Reload tasks after creation
        })
        .catch(error => console.error('Error creating task:', error));
    });

    // Load tasks on page load
    loadTasks();
});
