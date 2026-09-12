import { useEffect, useRef, useState } from 'react'

function DataFetcher() {
  const [selectedId, setSelectedId] = useState('all')
  const [posts, setPosts] = useState([])
  const [loading, setLoading] = useState(true)
  const firstRender = useRef(true)

  useEffect(() => {
    console.log(firstRender.current ? 'Монтирование компонента' : 'Обновление компонента')
    firstRender.current = false
    const controller = new AbortController()

    async function loadPosts() {
      setLoading(true)
      try {
        const suffix = selectedId === 'all' ? '' : `/${selectedId}`
        const response = await fetch(`https://jsonplaceholder.typicode.com/posts${suffix}`, { signal: controller.signal })
        if (!response.ok) throw new Error('Ошибка загрузки данных')
        const data = await response.json()
        setPosts(Array.isArray(data) ? data.slice(0, 5) : [data])
      } catch (error) {
        if (error.name !== 'AbortError') console.error(error)
      } finally {
        if (!controller.signal.aborted) setLoading(false)
      }
    }

    loadPosts()
    return () => controller.abort()
  }, [selectedId])

  useEffect(() => () => console.log('Размонтирование компонента'), [])

  return (
    <div>
      <label>Выберите ID поста
        <select value={selectedId} onChange={(event) => setSelectedId(event.target.value)}>
          <option value="all">Первые 5 постов</option>
          {[1, 2, 3, 4, 5].map((id) => <option key={id} value={id}>Пост {id}</option>)}
        </select>
      </label>
      {loading ? <p>Загрузка…</p> : (
        <ol>{posts.map((post) => <li key={post.id}><p>{post.title}</p></li>)}</ol>
      )}
    </div>
  )
}

export default DataFetcher
