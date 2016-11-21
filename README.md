# Code Your Own Quiz Project
Second project of Udacity's "Intro to Programming" Nanodegree

## Overview
This project includes a SQL module that creates a database for storing data on a "swiss pairings" style tournament, as well as a Python code module for creating records of tournament players, matches and results to be stored in the database.

## Instructions for testing the modules:
* Follow [Udacity's guide to installing and running Vagrant] (https://www.udacity.com/wiki/ud197/install-vagrant?_ga=1.62732204.1876431276.1456523634).
* Open GitBash and navigate to the Vagrant directory (i.e. cd fullstack/vagrant/tournament)
* Enter vagrant up, then enter vagrant ssh
* Navigate to tournament directory (i.e. cd /vagrant/tournament) and enter psql
* Enter \i tournament.sql. Confirm following output:
		
		DROP DATABASE 
		CREATE DATABASE 
		You are now connected to database "tournament" as user "vagrant". 
		CREATE TABLE 
		CREATE TABLE 
		CREATE VIEW
* Enter \q
* Enter python tournament_test.py.  Confirm following output:

		1. countPlayers() returns 0 after initial deletePlayers() execution.
		2. countPlayers() returns 1 after one player is registered.
		3. countPlayers() returns 2 after two players are registered.
  		4. countPlayers() returns zero after registered players are deleted.
  		5. Player records successfully deleted.
  		6. Newly registered players appear in the standings with no matches.
  		7. After a match, players have updated standings.
  		8. After match deletion, player standings are properly reset.
  		9. Matches are properly deleted.
  		10. After one match, players with one win are properly paired.
  		Success!  All tests pass!
