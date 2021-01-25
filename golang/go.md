# Go

go1.15.6

## 入口

// asm_amd64.s:87
runtime·rt0_go

The bootstrap sequence is:

 call osinit
 call schedinit

 // proc.go:114
 // runtime.main

 // proc.go:3550
 // runtime·newproc

 make & queue new G

 // proc.go:1116
 call runtime·mstart

The new G calls runtime·main.

### GMP

### GC

### channel

### goroutine

### defer
