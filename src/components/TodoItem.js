import React from "react"

class TodoItem extends React.Component {
  componentWillUnmount() {
    alert("Item about to be deleted!");
  }
  render() {
    return <li className="todo-item">
    <input
      type="checkbox"
      checked={this.props.todo.completed}
      onChange={() => this.props.handleChangeProps(this.props.todo.id)}
    />
    <button onClick={() => this.props.deleteTodoProps(this.props.todo.id)}>
      Delete
    </button>
  
    {this.props.todo.title}
  </li>
  }
}

export default TodoItem