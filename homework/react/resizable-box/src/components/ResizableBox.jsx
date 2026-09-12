import { useEffect, useLayoutEffect, useRef, useState } from 'react'

function ResizableBox() {
  const effectRef = useRef(null)
  const layoutRef = useRef(null)
  const [effectSize, setEffectSize] = useState({ width: 0, height: 0 })
  const [layoutSize, setLayoutSize] = useState({ width: 0, height: 0 })

  useEffect(() => {
    const updateSize = () => {
      const { width, height } = effectRef.current.getBoundingClientRect()
      console.log('useEffect: измерение блока')
      setEffectSize({ width: Math.round(width), height: Math.round(height) })
    }
    updateSize()
    window.addEventListener('resize', updateSize)
    return () => window.removeEventListener('resize', updateSize)
  }, [])

  useLayoutEffect(() => {
    const updateSize = () => {
      const { width, height } = layoutRef.current.getBoundingClientRect()
      console.log('useLayoutEffect: измерение блока')
      setLayoutSize({ width: Math.round(width), height: Math.round(height) })
    }
    updateSize()
    window.addEventListener('resize', updateSize)
    return () => window.removeEventListener('resize', updateSize)
  }, [])

  return (
    <div>
      <div ref={effectRef}>
        <h2>useEffect</h2>
        <p>{effectSize.width} × {effectSize.height} px</p>
        <p>Запускается после отображения кадра.</p>
      </div>
      <div ref={layoutRef}>
        <h2>useLayoutEffect</h2>
        <p>{layoutSize.width} × {layoutSize.height} px</p>
        <p>Запускается синхронно перед отрисовкой.</p>
      </div>
    </div>
  )
}

export default ResizableBox
