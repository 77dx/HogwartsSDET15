霍格沃滋实战课程项目
1.git关联远程项目 
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/77dx/HogwartsSDET15.git
    设置默认远程项目地址，新增token
    git remote set-url origin https://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@github.com/77dx/HogwartsSDET15.git
    git push -u origin main
    
    git remote -v
    echo XX/ >> .gitignore  忽略上传某些文件
2.进入/退出虚拟环境
    cd venv/bin
    source activate
    deactivate  退出虚拟环境
3.selenium 浏览器复用启动命令
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

4.获取当前文件所在的绝对路径：os.path.abspath(__file__)
5.获取当前文件的上一层目录的绝对路径：os.path.dirname(os.path.abspath(__file__))
6.获取项目的跟路径：root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
