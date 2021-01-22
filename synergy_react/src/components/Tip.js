import React, { Component } from 'react'

class Tip extends Component {
    constructor(props) {
        super(props);
        this.state = {
            tip_object : [], // 초깃값을 이렇게 array로 해도 되나?
            source : '✍',
            content : '화이팅'
        }
    }

    render() {
        return (
            <div>
                <h2>이게 도움이 될지는 모르겠지만...</h2>
                <div>
                    {this.props.content}
                </div>
                <div>
                    {this.props.source}
                </div>
            </div>
        )
    }
}

export default Tip
