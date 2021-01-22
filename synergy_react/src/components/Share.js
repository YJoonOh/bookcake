import React, { Component } from 'react'

class Share extends Component {
    render() {
        return (
            <div>
                <form action="" method="post"
                onSubmit={function(e){

                }.bind(this)}>
                    <h3>혹시,</h3>
                    <h3>현타를 다루는 나만의 방법이 있나요? 공유해주세요! 😀</h3>
                    <div>
                        <span>카테고리</span>
                        <input type="radio"></input>
                    </div>
                    <div><textarea name="share_tip" placeholder="이거는 플레이스홀더"></textarea></div>
                    <div><input type="submit"></input></div>
                </form>    
            </div>
        )
    }
}

export default Share
