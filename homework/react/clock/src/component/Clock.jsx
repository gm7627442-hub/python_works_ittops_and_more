import React, { Component } from 'react';

export class Clock extends Component {
  constructor(props) {
    super(props);
    this.state = {
      time: new Date().toLocaleTimeString()
    };
    this.timerID = null;
  }

  componentDidMount() {
    this.timerID = setInterval(() => this.tick(), 1000)
    }

   componentWillUnmount() {
    clearInterval(this.timerID);
   }
  
  tick() {
    this.setState({
         time: new Date().toLocaleTimeString()
    })
   }
   
   render() {
    return (
      <div>
        <h3>Текущее время: {this.state.time}</h3>
      </div>
    );
  }
}