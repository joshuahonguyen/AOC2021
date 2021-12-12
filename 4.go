package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	contents, _ := os.Open("34.txt")
	scanner := bufio.NewScanner(contents)

	var hor, dep, aim int
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(line)
		if strings.Contains(line, "up") {
			num, _ := strconv.Atoi(strings.Replace(line, "up ", "", -1))
			aim -= num
		} else if strings.Contains(line, "down") {
			num, _ := strconv.Atoi(strings.Replace(line, "down ", "", -1))
			aim += num
		} else {
			num, _ := strconv.Atoi(strings.Replace(line, "forward ", "", -1))
			hor += num
			dep = dep + aim*num
		}
	}
	fmt.Println(hor * dep)
}
