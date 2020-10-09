import React from "react"
import {
    BrowserRouter as Router,
    Switch,
    Route,
  } from "react-router-dom";
import ReactDOM from "react-dom"
import "./App.css"
//component file
import PlayerCardContainer from "./components/player_card/PlayerCardContainer"
import Player from "./components/player/Player";

ReactDOM.render(
        <Router>
          <Switch>
            <Route exact path="/">
                <PlayerCardContainer />
            </Route>
            <Route path="/players/:id" component={Player} />
          </Switch>

        </Router>, document.getElementById("root")
    );