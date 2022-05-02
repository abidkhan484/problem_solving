package main
import "fmt"

func split_string(text string) {
	length := len(text)
	odd_string := ""
	even_string := ""
    for i:=0; i<length; i++ {
		char := string(text[i])
		if i&1 == 0 {
			even_string = even_string + char
		} else {
			odd_string = odd_string + char
		}
	}
	fmt.Println(even_string, odd_string)
}

func main() {
	var T int
	var text string
	fmt.Scan(&T)

	for i:=0; i<T; i++ {
		fmt.Scan(&text)
		// text := "hackerrank"
		split_string(text)	
	}

}