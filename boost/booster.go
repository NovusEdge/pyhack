package main

import (
<<<<<<< HEAD
=======
	"flag"
>>>>>>> 83fb59409a68bf66d8db4a8f26537cb9743fa890
	gb "goboost/goboost"
	"time"

	"golang.org/x/sync/semaphore"
)

func main() {
	portScanFlag := flag.Bool("ports", false, "-ports=false (default false)")
	ipAddr := flag.String("ip", "127.0.0.1", "--ip=120.0.0.1\tSupplied for port scans.")

	flag.Parse()
	if *portScanFlag {
		go portScan(*ipAddr)
	}
}

func portScan(ipAddr string) {
	ps := &gb.PortScanner{
		IP:   ipAddr,
		Lock: semaphore.NewWeighted(gb.Ulimit()),
	}

<<<<<<< HEAD
	// defer flag.Parse()

	ps := &gb.PortScanner{
		IP:   "127.0.0.1",
		Lock: semaphore.NewWeighted(gb.Ulimit()),
	}

=======
>>>>>>> 83fb59409a68bf66d8db4a8f26537cb9743fa890
	ps.Start(1, 65535, 3*time.Millisecond)
}

// TODO: implement using flag lib:
/*
	./booster port_scan
*/
