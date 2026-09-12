import { useContext } from "react";
import { TodoContext, useTodo } from "./context/TodoContext";
import "./index.css";

function App() {
  const { todos, changeCompleted } = useTodo();

  return (
    <div className="container">
      <h1>Список задач</h1>

      {todos.map((todo) => (
        <div className="todo" key={todo.id}>
          <input
            type="checkbox"
            checked={todo.completed}
            onChange={() => changeCompleted(todo.id)}
          />

          <span className={todo.completed ? "completed" : ""}>
            {todo.title}
          </span>

          <p>
            {todo.completed ? "Сделано" : "Не сделано"}
          </p>
        </div>
      ))}
    </div>
  );
}

export default App;