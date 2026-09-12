import { useState } from 'react'
import QuoteViewer from './components/QuoteViewer'
import './App.css'

function App() {
  const [visible, setVisible] = useState(true)
  return (
    <main className="app-shell"><section className="card">
      <span className="eyebrow">Домашнее задание 21</span><h1>Случайные цитаты</h1>
      <button onClick={() => setVisible((value) => !value)}>{visible ? 'Скрыть цитаты' : 'Показать цитаты'}</button>
      {visible && <QuoteViewer />}
    </section></main>
  )
}
export default App
