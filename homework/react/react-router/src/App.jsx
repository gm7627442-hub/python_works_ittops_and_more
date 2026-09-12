import { BrowserRouter, Link, Route, Routes } from 'react-router-dom'
import Home from './pages/Home'
import About from './pages/About'
import Contacts from './pages/Contacts'

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Главная</Link>{' '}
        <Link to="/about">О нас</Link>{' '}
        <Link to="/contacts">Контакты</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contacts" element={<Contacts />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
