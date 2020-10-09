import React from "react"
import PlayerCardImage from "./PlayerCardImage"
import PlayerCardDetails from "./PlayerCardDetails"

class PlayerCard extends React.Component {
 
  render() {
    return <tr className="player-card">
      <PlayerCardDetails player={this.props.player} />
  </tr>
  }
}

export default PlayerCard
