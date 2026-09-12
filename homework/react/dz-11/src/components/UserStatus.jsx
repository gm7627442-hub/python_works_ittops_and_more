function UserStatus({ isLoggedIn }) {
  if (isLoggedIn) return <p className="status">Добро пожаловать, пользователь!</p>
  return <div className="status"><p>Чтобы продолжить, войдите в аккаунт.</p><button>Войти</button></div>
}

export default UserStatus
