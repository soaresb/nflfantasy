import React from "react"
import PlayerCard from "./PlayerCard"

class PlayerCardTable extends React.Component {
  render() {
    return (
      <table className="player-card-table">
        <tr><th>Rank</th> <th>Pos. Rank</th> <th>Name</th><th>Position</th></tr>
        {this.props.players.map(player => (
            <PlayerCard
                player={player}
            />
        ))}
      </table>
    )
  }
}

export default PlayerCardTable