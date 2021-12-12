package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, _ := os.Open("1112.txt")
	contents := bufio.NewScanner(file)
	for contents.Scan() {
		slice_of_fish := make([]int, 9)
		for _, e := range strings.Split(strings.TrimRight(contents.Text(), ","), ",") {
			e, _ := strconv.Atoi(e)
			slice_of_fish[e] += 1
		}
		day := 1
		sum := 0
		add := 0
		for day <= 256 {
			
			slice_of_new_fish := make([]int, 9)
			rank := 9
			for i, e := range slice_of_fish {
				if rank != 9 {
					slice_of_new_fish[i-1] += e
				} else {
					slice_of_new_fish[6] += e
					add += e
					slice_of_new_fish[8] += e
					slice_of_new_fish[0] = 0
					
				}
				rank -= 1
				
			}
			slice_of_fish = slice_of_new_fish
			day += 1
		}
		for i, _ := range slice_of_fish {
			sum+= slice_of_fish[i]
		}
		println(sum)
	}
}
