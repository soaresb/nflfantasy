import React from "react"
import DropDown from "./DropDown"

class Navigation extends React.Component {
 
  render() {
    return <div className="nav">
      <DropDown data={this.props.teamNavigation} handleNavigationChange={this.props.handleTeamNavigationChange} />
      <DropDown data={this.props.positionNavigation} handleNavigationChange={this.props.handlePositionNavigationChange} />
      </div>
  }
}

export default Navigation
