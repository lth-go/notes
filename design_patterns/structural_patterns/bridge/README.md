# 桥接模式

桥接模式是一种结构型设计模式， 可将一个大类或一系列紧密相关的类拆分为抽象和实现两个独立的层次结构， 从而能在开发时分别使用。

## 概念示例

假设你有两台电脑： 一台 Mac 和一台 Windows。 还有两台打印机： 爱普生和惠普。 这两台电脑和打印机可能会任意组合使用。 客户端不应去担心如何将打印机连接至计算机的细节问题。

如果引入新的打印机， 我们也不会希望代码量成倍增长。 所以， 我们创建了两个层次结构， 而不是 2x2 组合的四个结构体：

+ 抽象层： 代表计算机
+ 实施层： 代表打印机

这两个层次可通过桥接进行沟通， 其中抽象层 （计算机） 包含对于实施层 （打印机） 的引用。 抽象层和实施层均可独立开发， 不会相互影响。

```go
package main

import (
    "fmt"
)

// Computer
type computer interface {
    print()
    setPrinter(printer)
}

// Printer
type printer interface {
    printFile()
}

// Mac
type mac struct {
    printer printer
}

func (m *mac) print() {
    fmt.Println("Print request for mac")
    m.printer.printFile()
}

func (m *mac) setPrinter(p printer) {
    m.printer = p
}

// Windows
type windows struct {
    printer printer
}

func (w *windows) print() {
    fmt.Println("Print request for windows")
    w.printer.printFile()
}

func (w *windows) setPrinter(p printer) {
    w.printer = p
}

// Epson
type epson struct {
}

func (p *epson) printFile() {
    fmt.Println("Printing by a EPSON Printer")
}

// Hp
type hp struct {
}

func (p *hp) printFile() {
    fmt.Println("Printing by a HP Printer")
}

// Main

func main() {
    hpPrinter := &hp{}
    epsonPrinter := &epson{}

    macComputer := &mac{}

    macComputer.setPrinter(hpPrinter)
    macComputer.print()
    fmt.Println()

    macComputer.setPrinter(epsonPrinter)
    macComputer.print()
    fmt.Println()

    winComputer := &windows{}

    winComputer.setPrinter(hpPrinter)
    winComputer.print()
    fmt.Println()

    winComputer.setPrinter(epsonPrinter)
    winComputer.print()
    fmt.Println()
}
```
