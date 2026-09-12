import { useReducer } from "react";

const reducer = (state, action) => {
  switch (action.type) {
    case "ADD_TODO":
      return [
        ...state,
        {
          id: crypto.randomUUID(),
          title: action.payload,
          isEditing: false,
          isCompleted: false,
        },
      ];

    case "REMOVE_TODO":
      return state.filter((todo) => todo.id !== action.payload);

    case "TOGGLE_EDIT":
      return state.map((todo) =>
        todo.id === action.payload
          ? { ...todo, isEditing: true }
          : todo
      );

    case "UPDATE_TODO":
      return state.map((todo) =>
        todo.id === action.payload.id
          ? {
              ...todo,
              title: action.payload.title,
              isEditing: false,
            }
          : todo
      );

    case "TOGGLE_TODO":
      return state.map((todo) =>
        todo.id === action.payload
          ? { ...todo, isCompleted: !todo.isCompleted }
          : todo
      );

    default:
      return state;
  }
};

function App() {
  const [todos, dispatch] = useReducer(reducer, []);

  const handleSubmit = (e) => {
    e.preventDefault();

    const value = e.target.todoText.value;

    if (!value.trim()) return;

    dispatch({
      type: "ADD_TODO",
      payload: value,
    });

    e.target.reset();
  };

  return (
    <div>
      <h1>Todo List</h1>

      <form onSubmit={handleSubmit}>
        <input name="todoText" placeholder="New todo..." />
        <button type="submit">Add</button>
      </form>

      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.isCompleted}
              onChange={() =>
                dispatch({
                  type: "TOGGLE_TODO",
                  payload: todo.id,
                })
              }
            />

            {todo.isEditing ? (
              <input
                defaultValue={todo.title}
                onKeyDown={(e) => {
                  if (e.key === "Enter") {
                    dispatch({
                      type: "UPDATE_TODO",
                      payload: {
                        id: todo.id,
                        title: e.target.value,
                      },
                    });
                  }
                }}
                onBlur={(e) =>
                  dispatch({
                    type: "UPDATE_TODO",
                    payload: {
                      id: todo.id,
                      title: e.target.value,
                    },
                  })
                }
                autoFocus
              />
            ) : (
              <span>{todo.title}</span>
            )}

            <button
              onClick={() =>
                dispatch({
                  type: "TOGGLE_EDIT",
                  payload: todo.id,
                })
              }
            >
              Edit
            </button>

            <button
              onClick={() =>
                dispatch({
                  type: "REMOVE_TODO",
                  payload: todo.id,
                })
              }
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;