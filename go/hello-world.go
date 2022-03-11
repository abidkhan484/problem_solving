package main
import (
    "fmt"
    "bufio"
    "os"
)

func main() {
 //Enter your code here. Read input from STDIN. Print output to STDOUT
 welcomeMsg := bufio.NewReader(os.Stdin)
 line, _ := welcomeMsg.ReadString('\n')
 fmt.Println("Hello, World.")
 fmt.Println(line)
}

