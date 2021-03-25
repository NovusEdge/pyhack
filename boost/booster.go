package main

import (
	"flag"
	gb "goboost/goboost"
	"time"

	"golang.org/x/sync/semaphore"
)

/*
TODO: try adding diff. binaries for different boosts
like, for port scanning:
ports -ip=<ip>
something like that :P
*/

func main() {
	// portScanFlag := flag.Bool("ports", false, "-ports=false (default false)")
	ipAddr := flag.String("ip", "127.0.0.1", "-ip=120.0.0.1\tSupplied for port scans.")

	flag.Parse()
	go portScan(*ipAddr)
}

func portScan(ipAddr string) {
	ps := &gb.PortScanner{
		IP:   ipAddr,
		Lock: semaphore.NewWeighted(gb.Ulimit()),
	}

	ps.Start(1, 65535, 3*time.Millisecond)
}
