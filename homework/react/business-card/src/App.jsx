import './App.css'

function App() {
  const name = 'Павел'

  return (
    <div>
      <h1 style={{ color: 'blue' }}>{name}</h1>
      <h2>React-разработчик</h2>
      <p className="description">Изучаю React и создаю приложения.</p>
      <p>Учиться программировать нужно на практике.</p>
    </div>
  )
}

export default App
