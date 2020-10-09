import React from "react"

class PlayerDetails extends React.Component {
 
  render() {
    return  <div className="player-details" >
      <h2 className="player-name" >
        {this.props.player.name}
      </h2>
      <div className="player-team-position" > 
        <span> {this.props.player.position}, {this.props.player.team} </span>
      </div>
      <div className="player-position-rank" > 
        <span> Fantasy Pros Position Rank: {this.props.player.fantasy_pros_position_rank} </span>
      </div>
      <div className="player-rank" > 
        <span> Fantasy Pros Rank: {this.props.player.fantasy_pros_rank} </span>
      </div>
    </div>

  }
}

export default PlayerDetails
