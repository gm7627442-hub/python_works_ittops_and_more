import { useCallback, useState } from 'react'
import TodoItem from './components/TodoItem'

function App() {
  const [todos, setTodos] = useState([])
  const [text, setText] = useState('')

  function addTodo() {
    if (!text.trim()) return
    setTodos([...todos, { id: Date.now(), text, completed: false }])
    setText('')
  }

  const toggleTodo = useCallback((id) => {
    setTodos((items) => items.map((item) =>
      item.id === id ? { ...item, completed: !item.completed } : item
    ))
  }, [])

  const deleteTodo = useCallback((id) => {
    setTodos((items) => items.filter((item) => item.id !== id))
  }, [])

  return (
    <div>
      <input value={text} onChange={(event) => setText(event.target.value)} />
      <button onClick={addTodo}>Добавить</button>
      {todos.map((todo) => (
        <TodoItem key={todo.id} todo={todo} onToggle={toggleTodo} onDelete={deleteTodo} />
      ))}
    </div>
  )
}

export default App
