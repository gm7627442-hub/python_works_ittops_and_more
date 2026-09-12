import './App.css'

const files = [
  ['index.html', 'Содержит корневой элемент #root и подключает main.jsx как модуль. Он почти пустой, потому что интерфейс создаёт React.'],
  ['main.jsx', 'Точка входа: находит #root и с помощью createRoot монтирует главный компонент App.'],
  ['App.jsx', 'Главный компонент приложения. Здесь шаблон Vite заменён страницей с ответами на вопросы ДЗ.'],
  ['package.json', 'Хранит имя проекта, зависимости и команды scripts, необходимые для разработки и сборки.'],
]

function App() {
  return (
    <main className="app-shell">
      <section className="card wide">
        <span className="eyebrow">Домашнее задание 2</span>
        <h1>Как устроен React-проект</h1>
        <p className="lead">Основные файлы работают вместе: HTML предоставляет точку монтирования, main.jsx запускает React, а App.jsx описывает интерфейс.</p>
        <div className="grid">
          {files.map(([name, text]) => (
            <article className="info-card" key={name}>
              <h2>{name}</h2>
              <p>{text}</p>
            </article>
          ))}
        </div>
        <h2>Команды scripts</h2>
        <ul>
          <li><code>npm run dev</code> — запускает сервер разработки.</li>
          <li><code>npm run build</code> — создаёт production-сборку.</li>
          <li><code>npm run preview</code> — локально показывает готовую сборку.</li>
        </ul>
      </section>
    </main>
  )
}

export default App
