package main

import (
	"strings"
)

func cleanInput(text string) []string {
	lowered := strings.ToLower(text)
	trimmed := strings.TrimSpace(lowered)
	if trimmed == "" {
		return []string{}
	}
	words := strings.Fields(trimmed)
	return words
}

