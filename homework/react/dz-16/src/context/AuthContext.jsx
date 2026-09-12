import { useState } from 'react'
import { AuthContext } from './authStore'

export function AuthProvider({ children }) {
  const [userName, setUserName] = useState('')
  const login = (name) => setUserName(name.trim())
  const logout = () => setUserName('')

  return <AuthContext.Provider value={{ userName, login, logout }}>{children}</AuthContext.Provider>
}
