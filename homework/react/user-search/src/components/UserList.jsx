import { useMemo, useState } from 'react'

const initialUsers = [
  { id: 1, name: 'Алексей' }, { id: 2, name: 'Мария' }, { id: 3, name: 'Иван' },
  { id: 4, name: 'Ольга' }, { id: 5, name: 'Дмитрий' },
]

function UserList() {
  const [users] = useState(initialUsers)
  const [search, setSearch] = useState('')
  const filteredUsers = useMemo(() => {
    console.log('Фильтрация списка пользователей')
    const query = search.trim().toLocaleLowerCase('ru')
    return users.filter((user) => user.name.toLocaleLowerCase('ru').includes(query))
  }, [search, users])

  return (
    <div>
      <input value={search} onChange={(e) => setSearch(e.target.value)} placeholder="Введите имя" />
      <ul>{filteredUsers.map((user) => <li key={user.id}>{user.name}</li>)}</ul>
      {!filteredUsers.length && <p>Ничего не найдено</p>}
    </div>
  )
}
export default UserList
