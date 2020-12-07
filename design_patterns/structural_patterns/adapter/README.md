# 适配器模式

适配器是一种结构型设计模式， 它能使不兼容的对象能够相互合作。

```go
package main

import (
    "fmt"
)

type computer interface {
    insertIntoLightningPort()
}

// Client
type client struct {
}

func (c *client) insertLightningConnectorIntoComputer(com computer) {
    fmt.Println("Client inserts Lightning connector into computer.")
    com.insertIntoLightningPort()
}

// Mac
type mac struct {
}

func (m *mac) insertIntoLightningPort() {
    fmt.Println("Lightning connector is plugged into mac machine.")
}

// Windows
type windows struct{}

func (w *windows) insertIntoUSBPort() {
    fmt.Println("USB connector is plugged into windows machine.")
}


// WindowsAdapter
type windowsAdapter struct {
    windowMachine *windows
}

func (w *windowsAdapter) insertIntoLightningPort() {
    fmt.Println("Adapter converts Lightning signal to USB.")
    w.windowMachine.insertIntoUSBPort()
}

// Main
func main() {

    client := &client{}
    mac := &mac{}

    client.insertLightningConnectorIntoComputer(mac)

    windowsMachine := &windows{}
    windowsMachineAdapter := &windowsAdapter{
        windowMachine: windowsMachine,
    }

    client.insertLightningConnectorIntoComputer(windowsMachineAdapter)
}
```
