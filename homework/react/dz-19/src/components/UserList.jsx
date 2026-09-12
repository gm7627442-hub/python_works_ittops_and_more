import { useMemo, useState } from 'react'

const initialUsers = [
  { id: 1, name: 'Алексей' }, { id: 2, name: 'Мария' }, { id: 3, name: 'Иван' },
  { id: 4, name: 'Ольга' }, { id: 5, name: 'Дмитрий' },
]

function UserList() {
  const [users] = useState(initialUsers)
  const [search, setSearch] = useState('')
  const [unrelatedCounter, setUnrelatedCounter] = useState(0)

  const filteredUsers = useMemo(() => {
    console.log('Фильтрация списка пользователей')
    const query = search.trim().toLocaleLowerCase('ru')
    return users.filter((user) => user.name.toLocaleLowerCase('ru').includes(query))
  }, [search, users])

  return (
    <div className="stack">
      <input value={search} onChange={(e) => setSearch(e.target.value)} placeholder="Введите имя" />
      <button className="secondary" onClick={() => setUnrelatedCounter((n) => n + 1)}>Посторонний ререндер: {unrelatedCounter}</button>
      <ul className="list">{filteredUsers.map((user) => <li className="list-item" key={user.id}><span>{user.name}</span></li>)}</ul>
      {!filteredUsers.length && <p className="muted">Ничего не найдено</p>}
    </div>
  )
}
export default UserList
