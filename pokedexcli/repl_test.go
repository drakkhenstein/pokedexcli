package main

import (
	"testing"
)

func TestCleanInput(t *testing.T) {
	tests := []struct {
		input    string
		expected []string
	}{
		{
			input:    "  hello  world  ",
			expected: []string{"hello", "world"},
		},
		{
			input:    "",
			expected: []string{},
		},
		{
			input:    "   ",
			expected: []string{},
		},
		{
			input:    "charmander pickachu jigglypuff",
			expected: []string{"charmander", "pickachu", "jigglypuff"},
		},
		{
			input:    "  charmander pickachu jigglypuff pidgey  ",
			expected: []string{"charmander", "pickachu", "jigglypuff", "pidgey"},
		},
		{
			input:    "charmander",
			expected: []string{"charmander"},
		},
	}

	for _, test := range tests {
		result := cleanInput(test.input)
		if len(result) != len(test.expected) {
			t.Errorf("cleanInput(%q) = %v; want %v", test.input, result, test.expected)
			continue
		}
		for i := range result {
			word := result[i]
			expectedWord := test.expected[i]
			if word != expectedWord {
				t.Errorf("cleanInput(%q)[%d] = %q; want %q", test.input, i, word, expectedWord)
			}
		}
	}
}