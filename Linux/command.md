## 记录一些常见的Linux命令
### 文件操作
#### cp
`cp` [文件名|文件目录] [目的文件名|文件目录]  
可以跟多个文件名 和**一个目的地址**，`-r`参数表示拷贝整个目录。`\cp -f file_path file_path` 强制覆盖同名文件。拷贝操作可能导致文件的权限、拥有者\组等发生变化，为此加入`-p`可将文件原原本本拷贝下来。

#### mv 
和`cp`用法十分相似。还可以用作文件重命名。

#### rm
`rm -R dir_path` 删除目录  
`rm -f file_name`不询问就删除

#### touch
`touch file_name` 如果文件已经存在，会修改文件的时间戳属性。