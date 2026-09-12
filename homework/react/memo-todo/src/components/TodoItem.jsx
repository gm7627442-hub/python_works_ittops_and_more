import { memo } from 'react'

const TodoItem = memo(function TodoItem({ todo, onToggle, onDelete }) {
  console.log(`Рендер TodoItem: ${todo.text}`)
  return (
    <div>
      <input type="checkbox" checked={todo.completed} onChange={() => onToggle(todo.id)} />
      <span>{todo.text} — {todo.completed ? 'выполнено' : 'не выполнено'}</span>
      <button onClick={() => onDelete(todo.id)}>Удалить</button>
    </div>
  )
})
export default TodoItem
