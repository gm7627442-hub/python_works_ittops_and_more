import Stopwatch from './components/Stopwatch'
import './App.css'

function App() {
  return (
    <main className="app-shell">
      <section className="card">
        <span className="eyebrow">Домашнее задание 17</span>
        <h1>Секундомер</h1>
        <Stopwatch />
      </section>
    </main>
  )
}
export default App
