import { useState } from 'react'
import QuoteViewer from './components/QuoteViewer'

function App() {
  const [visible, setVisible] = useState(true)

  return (
    <div>
      <button onClick={() => setVisible(!visible)}>Показать/скрыть цитаты</button>
      {visible && <QuoteViewer />}
    </div>
  )
}

export default App
