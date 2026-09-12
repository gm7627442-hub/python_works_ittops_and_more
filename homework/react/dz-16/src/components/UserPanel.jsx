import { useState } from 'react'
import { useAuth } from '../hooks/useAuth'

function UserPanel() {
  const [name, setName] = useState('')
  const { userName, login, logout } = useAuth()

  const submit = (event) => {
    event.preventDefault()
    login(name)
    setName('')
  }

  return (
    <div><p className="muted">Уровень 3: UserPanel</p>
      {userName ? (
        <><h2>Добро пожаловать, {userName}!</h2><button onClick={logout}>Выйти</button></>
      ) : (
        <form className="stack" onSubmit={submit}>
          <input value={name} onChange={(event) => setName(event.target.value)} placeholder="Введите имя" required />
          <button type="submit">Войти</button>
        </form>
      )}
    </div>
  )
}
export default UserPanel
