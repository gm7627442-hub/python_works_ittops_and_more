import { useCallback, useState } from 'react'
import TodoItem from './components/TodoItem'
import './App.css'

const initialTodos = [
  { id: 1, text: 'Повторить React.memo', completed: false },
  { id: 2, text: 'Открыть консоль браузера', completed: true },
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
  const toggleTodo = useCallback((id) => setTodos((items) => items.map((item) => item.id === id ? { ...item, completed: !item.completed } : item)), [])
  const deleteTodo = useCallback((id) => setTodos((items) => items.filter((item) => item.id !== id)), [])

  return (
    <main className="app-shell"><section className="card wide">
      <span className="eyebrow">Домашнее задание 18</span><h1>Список задач с React.memo</h1>
      <form className="actions" onSubmit={addTodo}><input value={text} onChange={(e) => setText(e.target.value)} placeholder="Новая задача" /><button>Добавить</button></form>
      <ul className="list">{todos.map((todo) => <TodoItem key={todo.id} todo={todo} onToggle={toggleTodo} onDelete={deleteTodo} />)}</ul>
    </section></main>
  )
}
export default App
