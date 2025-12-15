package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type cliCommand struct {
	name        string
	description string
	callback    func() error
}


func commandExit() error {
	fmt.Println("Closing the Pokedex... Goodbye!")
	os.Exit(0)
	return nil
}

func commandHelp() error {
	fmt.Println("Welcome to the Pokedex!")
	fmt.Println("Usage:")
	fmt.Println("")
	fmt.Println("help: Displays a help message")
	fmt.Println("exit: Exit the Pokedex")
	return nil
}

func startRepl() {
	reader := bufio.NewScanner(os.Stdin)
	for {
		fmt.Print("Pokedex > ")
		reader.Scan() 

		words := cleanInput(reader.Text())
		if len(words) == 0 {
			continue
		}
		commandName := words[0]
		
		var commands = map[string]cliCommand{
    		"exit": {
        		name:        "exit",
        		description: "Exit the Pokedex",
        		callback:    commandExit,
    		},
			"help": {
				name:        "help",
				description: "Displays a help message",
				callback:    commandHelp,
			},
		}
		
		command, exists := commands[commandName] 
		if !exists {
			fmt.Println("Unknown command")
			continue
		}
		err := command.callback()
		if err != nil {
			fmt.Println(err)
		}
	}
}

func cleanInput(text string) []string {
	lowerd := strings.ToLower(text)
	if lowerd == "" {
		return []string{}
	}
	trimmed := strings.TrimSpace(lowerd)
	words := strings.Fields(trimmed)
	return words
}

