import { useState } from "react";

function App() {
  const [tasks, setTasks] = useState([]);
  const [text, setText] = useState("");

  function addTask() {
    const newTask = {
      id: Date.now(),
      text: text,
      completed: false,
    };

    setTasks([
      ...tasks,
      newTask,
    ]);

    setText("");
  }

  function toggleTask(id) {
    setTasks(
      tasks.map((task) => {
        if (task.id === id) {
          return {
            ...task,
            completed: !task.completed,
          };
        } else {
          return task;
        }
      })
    );
  }

  function deleteTask(id) {
    setTasks(
      tasks.filter((task) => {
        return task.id !== id;
      })
    );
  }

  const completedTasks = tasks.filter((task) => {
    return task.completed;
  }).length;

  return (
    <div>
      <h1>Todo List</h1>

      <input
        value={text}
        onChange={(event) => {
          setText(event.target.value);
        }}
      />

      <button onClick={addTask}>
        Добавить
      </button>


      <h3>
        Выполнено {completedTasks} из {tasks.length}
      </h3>


      {tasks.length === 0 ? (
        <p>Нет задач</p>
      ) : (
        tasks.map((task) => {
          return (
            <div key={task.id}>

              <input
                type="checkbox"
                checked={task.completed}
                onChange={() => {
                  toggleTask(task.id);
                }}
              />

              <span>
                {task.text}
              </span>

              <button
                onClick={() => {
                  deleteTask(task.id);
                }}
              >
                Удалить
              </button>

            </div>
          );
        })
      )}

    </div>
  );
}

export default App;