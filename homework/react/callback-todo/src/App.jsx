import { useCallback, useState } from 'react'
import TodoItem from './components/TodoItem'

function App() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Изучить useCallback', completed: false },
  ])
  const [text, setText] = useState('')

  function addTodo() {
    if (!text.trim()) return
    setTodos([...todos, { id: Date.now(), text, completed: false }])
    setText('')
  }

  const handleToggle = useCallback((id) => {
    setTodos((items) => items.map((item) =>
      item.id === id ? { ...item, completed: !item.completed } : item
    ))
  }, [])

  const handleDelete = useCallback((id) => {
    setTodos((items) => items.filter((item) => item.id !== id))
  }, [])

  return (
    <div>
      <input value={text} onChange={(event) => setText(event.target.value)} />
      <button onClick={addTodo}>Добавить</button>
      {todos.map((todo) => (
        <TodoItem key={todo.id} todo={todo} onToggle={handleToggle} onDelete={handleDelete} />
      ))}
    </div>
  )
}

export default App
