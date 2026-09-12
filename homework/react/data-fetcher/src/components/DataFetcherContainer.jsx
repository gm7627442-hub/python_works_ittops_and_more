import { useState } from 'react'
import DataFetcher from './DataFetcher'

function DataFetcherContainer() {
  const [visible, setVisible] = useState(true)
  return (
    <div>
      <button onClick={() => setVisible((value) => !value)}>{visible ? 'Скрыть' : 'Показать'} DataFetcher</button>
      {visible && <DataFetcher />}
    </div>
  )
}

export default DataFetcherContainer
