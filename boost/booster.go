package main

import (
	gb "goboost/goboost"
	"time"

	"golang.org/x/sync/semaphore"
)

func main() {
	ps := &gb.PortScanner{
		IP:   "182.237.9.10",
		Lock: semaphore.NewWeighted(gb.Ulimit()),
	}

	ps.Start(1, 65535, 3*time.Millisecond)
}
