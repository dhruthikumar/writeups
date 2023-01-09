package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

var (
	m, n = 21, 22
)

func op(word string, key int) string {
	out := ""
	for i := 0; i < len(word); i++ {
		out += string(int(word[i]) ^ key)
	}
	return out
}

func main() {
	content, err := ioutil.ReadFile("cipher.txt")
	if err != nil {
		log.Panicf("failed reading data from file: %s", err)
	}
	fmt.Println("Contents: ", string(content))
	x2, y2 := string(content[:len(content)/2]), string(content[len(content)/2:])

	x := op(string(y2), 0)
	y := ""
	for i := 0; i < len(x2); i++ {
		y += string(int(op(string(x), n)[i]) ^ int(x2[i]))
	}
	R := op(string(y), 0)
	fmt.Println(R)
	L := ""
	for i := 0; i < len(x); i++ {
		L += string(int(op(string(R), m)[i]) ^ int(x[i]))
	}
	fmt.Println(L)
	fmt.Println(L + R)
}
