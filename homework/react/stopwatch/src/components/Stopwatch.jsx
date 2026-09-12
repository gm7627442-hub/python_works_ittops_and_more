import { useEffect, useRef, useState } from 'react'

function Stopwatch() {
  const [seconds, setSeconds] = useState(0)
  const intervalRef = useRef(null)

  const start = () => {
    if (intervalRef.current !== null) return
    intervalRef.current = window.setInterval(() => setSeconds((value) => value + 1), 1000)
  }

  const stop = () => {
    if (intervalRef.current === null) return
    window.clearInterval(intervalRef.current)
    intervalRef.current = null
  }

  const reset = () => {
    stop()
    setSeconds(0)
  }

  useEffect(() => () => {
    if (intervalRef.current !== null) window.clearInterval(intervalRef.current)
  }, [])

  return (
    <div>
      <p>{seconds} сек.</p>
      <button onClick={start}>Старт</button>
      <button onClick={stop}>Стоп</button>
      <button onClick={reset}>Сброс</button>
    </div>
  )
}
export default Stopwatch
