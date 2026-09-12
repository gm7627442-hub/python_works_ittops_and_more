import { memo } from 'react'

const TodoItem = memo(function TodoItem({ todo, onToggle, onDelete }) {
  console.log(`Рендер TodoItem ${todo.id}`)
  return (
    <li className="list-item">
      <input style={{ width: 'auto' }} type="checkbox" checked={todo.completed} onChange={() => onToggle(todo.id)} />
      <span className={todo.completed ? 'done' : ''}>{todo.text}</span>
      <button className="danger" onClick={() => onDelete(todo.id)}>Удалить</button>
    </li>
  )
})
export default TodoItem
