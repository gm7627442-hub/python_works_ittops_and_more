import { useState } from 'react'
import UserStatus from './components/UserStatus'
import './App.css'

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  return (
    <main className="app-shell">
      <section className="card">
        <span className="eyebrow">Домашнее задание 11</span>
        <h1>Условный рендеринг</h1>
        <UserStatus isLoggedIn={isLoggedIn} />
        <button onClick={() => setIsLoggedIn((value) => !value)}>{isLoggedIn ? 'Выйти' : 'Изменить состояние'}</button>
      </section>
    </main>
  )
}

export default App
