package main


import (
  "fmt"
  "os"
  "bufio"
  "strconv"
)

func main() {
  	var _ = strconv.Itoa // Ignore this comment. You can still use the package "strconv".
  
    var i uint64 = 4
    var d float64 = 4.0
    var s string = "HackerRank "

    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    j, _ := strconv.ParseUint(scanner.Text(), 10, 64)
    fmt.Println(i+j)
    
    scanner.Scan()
    e, _ := strconv.ParseFloat(scanner.Text(), 64)
    fmt.Printf("%.1f\n", d+e)
    
    scanner.Scan()
    t := scanner.Text()
    fmt.Println(s+t)

}
