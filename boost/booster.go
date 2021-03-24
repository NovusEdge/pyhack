package main

import (
	gb "goboost/goboost"
	"time"

	"golang.org/x/sync/semaphore"
)

func main() {

	// defer flag.Parse()

	ps := &gb.PortScanner{
		IP:   "127.0.0.1",
		Lock: semaphore.NewWeighted(gb.Ulimit()),
	}

	ps.Start(1, 65535, 3*time.Millisecond)
}

// TODO: implement using flag lib:
/*
	./booster port_scan
*/
