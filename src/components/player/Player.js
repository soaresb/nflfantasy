import React from 'react';
import axios from "axios";
import { v4 as uuidv4 } from 'uuid'
import PlayerHeader from './PlayerHeader';

class Player extends React.Component {

    state = {
        player: {}
    }

    fetchPlayer() {
        let url = `http://localhost:8082/player/${this.props.match.params.id}`
        let params = {}
        axios.get(url, {
          params: params
        })
          .then(response => this.setState({ player: response.data.results }));
      }
    componentDidMount() {
        this.fetchPlayer()
    }

    
    render() {
        return (
          <div className="container">
            <PlayerHeader player={this.state.player} />
          </div>
        );
    }
}

export default Player