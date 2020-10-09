import React from 'react';
import axios from "axios";
import PlayerCardTable from "./PlayerCardTable"
import Navigation from './navigation/Navigation';
import { v4 as uuidv4 } from 'uuid'

class PlayerCardContainer extends React.Component {
    state = {
      players: [],
      currentValue: "",
      allPositions: ["QB", "RB", "WR", "TE", "K"],
      teamNavigation: {
        id: uuidv4(),
        values: [
          "ALL", 
          "ARI", 
          "ATL", 
          "BAL", 
          "BUF", 
          "CAR", 
          "CHI", 
          "CIN", 
          "CLE", 
          "DAL", 
          "DEN", 
          "DET", 
          "GB", 
          "HOU", 
          "IND", 
          "JAX", 
          "KC", 
          "LAC", 
          "LAR", 
          "LV", 
          "MIA", 
          "MIN", 
          "NE", 
          "NO", 
          "NYG", 
          "NYJ", 
          "PHI", 
          "PIT", 
          "SEA", 
          "SF", 
          "TB", 
          "TEN", 
          "WAS"
      ],
        label: "Team",
        currentTeam: "ALL"
      },
      positionNavigation: {
        id: uuidv4(),
        values: [
          "ALL", 
          "QB", 
          "RB", 
          "WR", 
          "TE"
        ],
        label: "Position",
        currentPosition: "ALL"
      }
    }
    handleTeamNavigationChange = val => {
      if (val !== this.state.currentTeam) {
        this.setState(prevState => ({
          teamNavigation: {                   // object that we want to update
              ...prevState.teamNavigation,    // keep all other key-value pairs
              currentTeam: val       // update the value of specific key
          }
        }), () => this.fetchPlayers()
    
      )}

    }

    handlePositionNavigationChange = val => {
      if (val !== this.state.currentPosition) {
        this.setState(prevState => ({
          positionNavigation: {                   // object that we want to update
              ...prevState.positionNavigation,    // keep all other key-value pairs
              currentPosition: val       // update the value of specific key
          }
        }), () => this.fetchPlayers()
    
      )}

    }
    fetchPlayers() {
      let url = "http://localhost:8082/players"
      let params = {}
      params.team = this.state.teamNavigation.currentTeam
      params.position = this.state.positionNavigation.currentPosition
      params.sort = this.state.positionNavigation.currentPosition !== "ALL" ? "player" : "all"
      axios.get(url, {
        params: params
      })
        .then(response => this.setState({ players: response.data.results }));
    }
    componentDidMount() {
      this.fetchPlayers()
    }
    render() {
        return (
          <div className="container">
            <Navigation teamNavigation={this.state.teamNavigation}
              handleTeamNavigationChange={this.handleTeamNavigationChange}
              positionNavigation={this.state.positionNavigation}
              handlePositionNavigationChange={this.handlePositionNavigationChange}
              
             />
            <PlayerCardTable 
              players={this.state.players} 
            />
              
          </div>
        );
    }
}

export default PlayerCardContainer