import React from "react"

class PlayerCardDetails extends React.Component {
 
  render() {
    return <> 
      <td>{this.props.player.fantasy_pros_rank}</td> 
      <td>{this.props.player.fantasy_pros_position_rank}</td>  
      <td> <a href={`/players/${this.props.player._id}`}> <span className="player-card-name">{this.props.player.name}</span> </a> <small className="player-card-team">{this.props.player.current_team}</small> </td> 
      <td>{this.props.player.position}</td> 
    </>
  }
}

export default PlayerCardDetails
