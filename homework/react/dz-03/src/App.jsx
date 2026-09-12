import './App.css'

function App() {
  const name = 'Павел'

  return (
    <main className="app-shell">
      <section className="card" style={{ borderTop: '7px solid #3157d5' }}>
        <span className="eyebrow">Домашнее задание 3</span>
        <h1 style={{ color: '#3157d5' }}>Привет, {name}!</h1>
        <h2>Начинающий React-разработчик</h2>
        <p className="lead">Изучаю компоненты, JSX и современную стилизацию интерфейсов. Люблю превращать идеи в работающие приложения.</p>
        <p className="status">💡 «Большие результаты начинаются с маленького компонента».</p>
      </section>
    </main>
  )
}

export default App
