import { Component } from 'react'

const quotes = [
  'Сложное становится простым, когда разбиваешь его на компоненты.',
  'Лучший способ научиться программировать — создавать проекты.',
  'Каждая ошибка делает следующий шаг понятнее.',
  'Хороший интерфейс помогает человеку, не отвлекая его.',
]

class QuoteViewer extends Component {
  state = { index: 0 }

  componentDidMount() { console.log('QuoteViewer: компонент смонтирован') }
  componentDidUpdate() { console.log('QuoteViewer: компонент обновлён') }
  componentWillUnmount() { console.log('QuoteViewer: компонент размонтирован') }

  showNext = () => {
    this.setState(({ index }) => {
      let next = index
      while (next === index && quotes.length > 1) next = Math.floor(Math.random() * quotes.length)
      return { index: next }
    })
  }

  render() {
    return <div><p>{quotes[this.state.index]}</p><button onClick={this.showNext}>Следующая цитата</button></div>
  }
}
export default QuoteViewer
