import { BrowserRouter, NavLink, Route, Routes } from 'react-router-dom'
import Home from './pages/Home'
import About from './pages/About'
import Contacts from './pages/Contacts'
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <main className="app-shell">
        <section className="card wide">
          <span className="eyebrow">Домашнее задание 14</span>
          <nav>
            <NavLink to="/">Главная</NavLink>
            <NavLink to="/about">О нас</NavLink>
            <NavLink to="/contacts">Контакты</NavLink>
          </nav>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/contacts" element={<Contacts />} />
          </Routes>
        </section>
      </main>
    </BrowserRouter>
  )
}

export default App
