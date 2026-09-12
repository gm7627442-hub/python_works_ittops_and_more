import { AuthProvider } from './context/AuthContext'
import Page from './components/Page'

function App() {
  return (
    <AuthProvider>
      <Page />
    </AuthProvider>
  )
}

export default App
