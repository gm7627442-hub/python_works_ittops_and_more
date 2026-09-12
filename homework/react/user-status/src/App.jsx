import { useState } from 'react'
import UserStatus from './components/UserStatus'

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false)

  return (
    <div>
      <UserStatus isLoggedIn={isLoggedIn} />
      <button onClick={() => setIsLoggedIn(!isLoggedIn)}>
        Изменить статус
      </button>
    </div>
  )
}

export default App
