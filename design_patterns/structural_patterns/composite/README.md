# 组合模式

组合模式是一种结构型设计模式， 你可以使用它将对象组合成树状结构， 并且能像使用独立对象一样使用它们。

## 概念示例

让我们试着用一个操作系统文件系统的例子来理解组合模式。 文件系统中有两种类型的对象： 文件和文件夹。 在某些情形中， 文件和文件夹应被视为相同的对象。 这就是组合模式发挥作用的时候了。

想象一下， 你需要在文件系统中搜索特定的关键词。 这一搜索操作需要同时作用于文件和文件夹上。 对于文件而言， 其只会查看文件的内容； 对于文件夹则会在其内部的所有文件中查找关键词。

```go
package main

import "fmt"

// component
type component interface {
    search(string)
}

// file
type file struct {
    name string
}

func (f *file) search(keyword string) {
    fmt.Printf("Searching for keyword %s in file %s\n", keyword, f.name)
}

func (f *file) getName() string {
    return f.name
}

// folder
type folder struct {
    components []component
    name       string
}

func (f *folder) search(keyword string) {
    fmt.Printf("Serching recursively for keyword %s in folder %s\n", keyword, f.name)
    for _, composite := range f.components {
        composite.search(keyword)
    }
}

func (f *folder) add(c component) {
    f.components = append(f.components, c)
}

// main
func main() {
    file1 := &file{name: "File1"}
    file2 := &file{name: "File2"}
    file3 := &file{name: "File3"}

    folder1 := &folder{
        name: "Folder1",
    }

    folder1.add(file1)

    folder2 := &folder{
        name: "Folder2",
    }
    folder2.add(file2)
    folder2.add(file3)
    folder2.add(folder1)

    folder2.search("rose")
}
```
