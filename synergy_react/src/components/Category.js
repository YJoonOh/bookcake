import React, { Component } from 'react'

class Category extends Component {
    constructor(props){
        super(props);
        this.state={
            
        }
    }
    render() {
        return (
            <div>
                <ul>
                    <li>
                        <a href="/this-might-help"><button value="현 상황" onClick={function(e){
                            e.preventDefault();
                        }.bind(this)}></button></a>
                    </li>
                    <li>
                        <a href="/this-might-help"><button value="인간관계" onClick={function(e){
                            e.preventDefault();
                        }.bind(this)}></button></a>
                    </li>
                    <li>
                        <a href="/this-might-help"><button value="사랑" onClick={function(e){
                            e.preventDefault();
                        }.bind(this)}></button></a>
                    </li>
                    <li>
                        <a href="/this-might-help"><button value="기타" onClick={function(e){
                            e.preventDefault();
                        }.bind(this)}></button></a>
                    </li>
                </ul>
            </div>
        )
    }
}

export default Category
