import React, { Component } from 'react';
import './App.css';
import axios from 'axios';
import ApiAi from './ApiAi';
const client = new ApiAi.ApiAiClient({accessToken: '47da946ec0f441728422eb1a61d2ff20'});

class App extends Component {
  constructor() {
    super();
    this.toggle = true;
  }
  
  speech = () => {
    var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 5;
    if(this.toggle)
      recognition.start();
    else
      recognition.stop();
    this.toggle = !this.toggle;
    recognition.onresult = function(event) {
      client.textRequest(event.results[0][0].transcript).then(result => {
        console.log(result)
        let callUrl = "http://localhost:8000/parse/"
        let instance = axios.create({
          baseURL: callUrl,
        });
        instance.post(callUrl, result, {withCredentials: true}).then((response) => {
          console.log('done')
        })
      });
    };
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h1>Speech To Code</h1>  
        </div>
        <div className="App-Body">
          <div>
            <h2>Tap To Begin</h2>
            <div className="speech-btn"><button onClick={this.speech}></button></div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
