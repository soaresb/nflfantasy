import React from "react"
import PlayerImage from "./PlayerImage"
import PlayerDetails from "./PlayerDetails"


class PlayerHeader extends React.Component {
 
  render() {
    return <div className="player-header">
        <PlayerImage player={this.props.player} />
        <PlayerDetails player={this.props.player} />
    </div>
    
  }
}

export default PlayerHeader
