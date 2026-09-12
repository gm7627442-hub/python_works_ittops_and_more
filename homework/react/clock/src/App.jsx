import { Component } from 'react';
import { Clock } from './component/Clock';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showClock: true
    };
  }

  toggleClock = () => {
    this.setState((prevState) => ({
      showClock: !prevState.showClock
    }));
  };

  render() {
    return (
      <div>
        <h2>Жизненный цикл компонента</h2>
        <button onClick={this.toggleClock} style={{ marginBottom: '15px', padding: '5px 10px' }}>
          {this.state.showClock ? 'Скрыть часы' : 'Показать часы'}
        </button>
        {this.state.showClock && <Clock/>}
      </div>
    );
  }
}

export default App;
