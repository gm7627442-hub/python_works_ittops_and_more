function UserStatus({ isLoggedIn }) {
  if (isLoggedIn) return <p>Добро пожаловать, пользователь!</p>
  return <button>Войти</button>
}

export default UserStatus
