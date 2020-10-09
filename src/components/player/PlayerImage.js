import React from "react"

class PlayerImage extends React.Component {
 
  render() {
    return <div className="player-image-container"><img className="player-image" style={{"width": "65px"}} src={this.props.player.photo_url} 
        alt={this.props.player.name}>

        </img></div>
    
  }
}

export default PlayerImage
