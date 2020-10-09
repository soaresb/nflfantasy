import React from "react"

class DropDown extends React.Component {
    
    render() {
        return <div className="dropdown">
            <label className="nav-label" for={this.props.data.label}>{this.props.data.label}</label>
            <select onChange={(event) => this.props.handleNavigationChange(event.target.value)} name={this.props.data.label} id={this.props.data.label}>
                {this.props.data.values.map(value => (
                    <option value={value}>{value}</option>
                ))}
            </select>
        </div> 
  }
}

export default DropDown
