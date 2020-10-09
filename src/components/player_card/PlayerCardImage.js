import React from "react"

class PlayerCardImage extends React.Component {
 
  render() {
    return <td><img style={{"height": "45px"}} src={this.props.player.photo_url} 
        alt={this.props.player.name}>

        </img></td>
    
  }
}

export default PlayerCardImage
