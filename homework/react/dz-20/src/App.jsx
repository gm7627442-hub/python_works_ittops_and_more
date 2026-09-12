import { useCallback, useState } from 'react'
import TodoItem from './components/TodoItem'
import './App.css'

const initialTodos = [
  { id: 1, text: 'Изучить useCallback', completed: false },
  { id: 2, text: 'Проверить React.memo', completed: false },
]

function App() {
  const [todos, setTodos] = useState(initialTodos)
  const [text, setText] = useState('')

  const addTodo = (event) => {
    event.preventDefault()
    if (!text.trim()) return
    setTodos((items) => [...items, { id: Date.now(), text: text.trim(), completed: false }])
    setText('')
  }
  const handleToggle = useCallback((id) => setTodos((items) => items.map((item) => item.id === id ? { ...item, completed: !item.completed } : item)), [])
  const handleDelete = useCallback((id) => setTodos((items) => items.filter((item) => item.id !== id)), [])

  return (
    <main className="app-shell"><section className="card wide">
      <span className="eyebrow">Домашнее задание 20</span><h1>Todo и useCallback</h1>
      <form className="actions" onSubmit={addTodo}><input value={text} onChange={(e) => setText(e.target.value)} placeholder="Текст новой задачи" /><button>Добавить</button></form>
      <ul className="list">{todos.map((todo) => <TodoItem key={todo.id} todo={todo} onToggle={handleToggle} onDelete={handleDelete} />)}</ul>
    </section></main>
  )
}
export default App
