# 外观模式

外观是一种结构型设计模式， 能为复杂系统、 程序库或框架提供一个简单 （但有限） 的接口。

## 概念示例

人们很容易低估使用信用卡订购披萨时幕后工作的复杂程度。 在整个过程中会有不少的子系统发挥作用。 下面是其中的一部分：

+ 检查账户
+ 检查安全码
+ 借记/贷记余额
+ 账簿录入
+ 发送消息通知

在如此复杂的系统中， 可以说是一步错步步错， 很容易就会引发大的问题。 这就是为什么我们需要外观模式， 让客户端可以使用一个简单的接口来处理众多组件。
客户端只需要输入卡片详情、 安全码、 支付金额以及操作类型即可。 外观模式会与多种组件进一步地进行沟通， 而又不会向客户端暴露其内部的复杂性。

```go
package main

import (
    "fmt"
    "log"
)

type walletFacade struct {
    account      *account
    wallet       *wallet
    securityCode *securityCode
    notification *notification
    ledger       *ledger
}

func newWalletFacade(accountID string, code int) *walletFacade {
    fmt.Println("Starting create account")
    walletFacacde := &walletFacade{
        account:      newAccount(accountID),
        securityCode: newSecurityCode(code),
        wallet:       newWallet(),
        notification: &notification{},
        ledger:       &ledger{},
    }
    fmt.Println("Account created")
    return walletFacacde
}

func (w *walletFacade) addMoneyToWallet(accountID string, securityCode int, amount int) error {
    fmt.Println("Starting add money to wallet")
    err := w.account.checkAccount(accountID)
    if err != nil {
        return err
    }
    err = w.securityCode.checkCode(securityCode)
    if err != nil {
        return err
    }
    w.wallet.creditBalance(amount)
    w.notification.sendWalletCreditNotification()
    w.ledger.makeEntry(accountID, "credit", amount)
    return nil
}

func (w *walletFacade) deductMoneyFromWallet(accountID string, securityCode int, amount int) error {
    fmt.Println("Starting debit money from wallet")
    err := w.account.checkAccount(accountID)
    if err != nil {
        return err
    }

    err = w.securityCode.checkCode(securityCode)
    if err != nil {
        return err
    }
    err = w.wallet.debitBalance(amount)
    if err != nil {
        return err
    }
    w.notification.sendWalletDebitNotification()
    w.ledger.makeEntry(accountID, "credit", amount)
    return nil
}

type account struct {
    name string
}

func newAccount(accountName string) *account {
    return &account{
        name: accountName,
    }
}

func (a *account) checkAccount(accountName string) error {
    if a.name != accountName {
        return fmt.Errorf("Account Name is incorrect")
    }
    fmt.Println("Account Verified")
    return nil
}

type securityCode struct {
    code int
}

func newSecurityCode(code int) *securityCode {
    return &securityCode{
        code: code,
    }
}

func (s *securityCode) checkCode(incomingCode int) error {
    if s.code != incomingCode {
        return fmt.Errorf("Security Code is incorrect")
    }
    fmt.Println("SecurityCode Verified")
    return nil
}

type wallet struct {
    balance int
}

func newWallet() *wallet {
    return &wallet{
        balance: 0,
    }
}

func (w *wallet) creditBalance(amount int) {
    w.balance += amount
    fmt.Println("Wallet balance added successfully")
    return
}

func (w *wallet) debitBalance(amount int) error {
    if w.balance < amount {
        return fmt.Errorf("Balance is not sufficient")
    }
    fmt.Println("Wallet balance is Sufficient")
    w.balance = w.balance - amount
    return nil
}

type ledger struct {
}

func (s *ledger) makeEntry(accountID, txnType string, amount int) {
    fmt.Printf("Make ledger entry for accountId %s with txnType %s for amount %d\n", accountID, txnType, amount)
    return
}

type notification struct {
}

func (n *notification) sendWalletCreditNotification() {
    fmt.Println("Sending wallet credit notification")
}

func (n *notification) sendWalletDebitNotification() {
    fmt.Println("Sending wallet debit notification")
}

func main() {
    fmt.Println()
    walletFacade := newWalletFacade("abc", 1234)
    fmt.Println()

    err := walletFacade.addMoneyToWallet("abc", 1234, 10)
    if err != nil {
        log.Fatalf("Error: %s\n", err.Error())
    }

    fmt.Println()
    err = walletFacade.deductMoneyFromWallet("abc", 1234, 5)
    if err != nil {
        log.Fatalf("Error: %s\n", err.Error())
    }
}
```
