import ResizableBox from './components/ResizableBox'
import './App.css'

function App() {
  return (
    <main className="app-shell">
      <section className="card wide">
        <span className="eyebrow">Домашнее задание 7</span>
        <h1>useEffect и useLayoutEffect</h1>
        <p className="lead">Измените размер окна. Оба варианта измеряют один DOM-элемент, но useLayoutEffect выполняется до отрисовки кадра.</p>
        <ResizableBox />
      </section>
    </main>
  )
}

export default App
