import { AuthProvider } from './context/AuthContext'
import Page from './components/Page'
import './App.css'

function App() {
  return (
    <AuthProvider>
      <main className="app-shell">
        <section className="card">
          <span className="eyebrow">Домашнее задание 16</span>
          <h1>Авторизация через Context</h1>
          <Page />
        </section>
      </main>
    </AuthProvider>
  )
}

export default App
