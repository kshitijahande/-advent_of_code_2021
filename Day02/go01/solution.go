package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Node struct {
	Action string
	val    int
}

func GetInputData() []Node {
	slice := make([]Node, 0, 3)

	file, err := os.Open("../input.txt")
	if err != nil {
		fmt.Println("Error opening input file ", err)
	}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		s := strings.Split(scanner.Text(), " ")
		intVal, err := strconv.Atoi(s[1])
		if err != nil {
			fmt.Println("Error converting to int ", intVal, ". Error ", err)
			os.Exit(2)
		}
		node := Node{s[0], intVal}
		// fmt.Println(node)
		slice = append(slice, node)
	}

	file.Close()
	return slice
}

// Problem1
func partone() {
	inputData := GetInputData()
	var fp int // track forward position
	var dp int // track depth position

	for _, node := range inputData {
		switch node.Action {
		case "forward":
			fp += node.val
		case "down":
			dp += node.val
		case "up":
			dp -= node.val
		}
	}
	fmt.Println("partone result", fp*dp)
}

// Problem2
func parttwo() {
	inputData := GetInputData()
	var fp int  // track forward position
	var dp int  // track depth position
	var aim int // track aim position

	for _, node := range inputData {
		switch node.Action {
		case "forward":
			fp += node.val
			dp += node.val * aim
		case "down":
			aim += node.val
		case "up":
			aim -= node.val
		}
	}
	fmt.Println("parttwo result", fp*dp)
}

func main() {
	partone()
	parttwo()
}

// Exec command to run the code
// go run solution.go
