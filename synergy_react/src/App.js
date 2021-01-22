import { Component } from 'react';
import './App.css';
import Category from './components/Category';
import Share from './components/Share';
import Tip from './components/Tip';
import NoMore from './components/NoMore';
import Thanks from './components/Thanks';
import About from './components/About';


class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      tip_object : [],
      selected_category : 'current',
      selected_page : 'home',
    }
  }

  componentDidMount() {
    /* setTimeout(() => {
        this.setState({});
    }, 3000) */
    this._getTip();
}

_checkState = () => {
  if (this.state.selected_page === 'home') {

  }
  else if (this.state.selected_page === 'tip') {

  }
  else if (this.state.selected_page === 'about') {

  }
  else if (this.state.selected_page === 'thanks') {

  }
  else if (this.state.selected_page === 'nomore') {

  }
}
// 아래 _getMovies()를 통해 state에 넣어진(?) tip을 <Tip /> 컴포넌트로 display
_renderTip = () => {
  /* tip_object에 json object가 여러개면 mapping을 해줘야됨.
  const tip = this.state.tip_object.map((this_tip, index) => {
    return <Tip content={this_tip.text_content} source={this_tip.source} key={index} />
  }) 
  return tip[0] */
  const tip = this.state.tip_object
  return <Tip content={tip.text_content} source={tip.source} />
}

// 아래 _callApi()로 API를 가져오고, _getTip()로 이걸 state에 넣음(?)
_getTip = async () => {
  const tip = await this._callApi(); // this._callApi()가 끝나자마자(not succeed) 그 return값이 tip에 저장되고 아래 라인으로 넘어간다
  console.log(tip);
  this.setState({
    tip_object : tip
  })
}

// API 가져오기
_callApi = () => {
  return fetch("http://127.0.0.1:8000/api/home/")
  .then((response) => response.json())
  /* 만약 이 json 오브젝트 내에 또 다른 오브젝트가 있어서 거기에 access 하려면 json.data.tip 이런 식으로 명시해줘야 함.
  하지만 이 경우에는 그렇지 않기 때문에 json만 써주면 되고, 그럼 굳이 아래처럼 .then을 쓸 필요가 없는듯..
  .then((json) => json) */
  .catch((err) => console.log(err))
}

  render() {
    return (
      <div className="app">
        <h2>삶의 어느 부분에서 현타가 오나요?</h2>
        <Category></Category>
        <Share></Share>
        <div>
          {this.state.tip_object ? this._renderTip() : "Does not exist"}
        </div>
      </div>
    )
  }
}

export default App;
