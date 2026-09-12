import { createContext, useContext, useEffect, useState } from "react";

export const TodoContext = createContext(null);



export function TodoProvider({ children }) {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    const getTodos = async () => {
      const response = await fetch(
        "https://jsonplaceholder.typicode.com/todos"
      );

      const data = await response.json();

      setTodos(data);
    };

    getTodos();
  }, []);

  const changeCompleted = (id) => {
    setTodos((prevTodos) =>
      prevTodos.map((todo) =>
        todo.id === id
          ? { ...todo, completed: !todo.completed }
          : todo
      )
    );
  };

  return (
    <TodoContext.Provider value={{ todos, changeCompleted }}>
      {children}
    </TodoContext.Provider>
  );
}

export function useTodo() {
    return useContext(TodoContext)
}