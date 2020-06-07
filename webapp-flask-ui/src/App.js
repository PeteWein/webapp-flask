import React from 'react';
import './App.css';

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            favoriteFoods: []
        }
    }

    async componentDidMount() {
        this.setState({
            favoriteFoods: await this.favoriteFoods()
        });
    }

    favoriteFoods = async () => {
        const favoriteFoods = await (await fetch('http://localhost:5000/api/favoriteFoods')).json();
        return favoriteFoods.foods;
    }

    render() {
        const { favoriteFoods } = this.state;
        return (
            <div>
                <h1>My Favorite Foods</h1>
                {favoriteFoods.map((food, index) => {
                    return (
                        <h2 key={index}>{food}</h2>
                    )
                })}
            </div>
        );
    }
}

export default App;
