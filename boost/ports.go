package main

import (
	"flag"
	gb "goboost/goboost"
	"time"

	"golang.org/x/sync/semaphore"
)

func main() {
	ipAddr := flag.String("domain", "google.com", "-domain=<domain>\tSupplied for port scans.")

	flag.Parse()

	go portScan(*ipAddr)
}

func portScan(ipAddr string) {

	ps := &gb.PortScanner{
		IP:   ipAddr,
		Lock: semaphore.NewWeighted(gb.Ulimit()),
	}

	ps.Start(1, 65535, 900*time.Millisecond)
}

// TODO: implement using flag lib:
/*
	./booster port_scan

	something similar to:  lsof -i
	reference: https://techspirited.com/linux-how-to-open-port-in-linux
*/
