# 更新文档内容
gitbook build . docs

# 提交主目录
git add .
git commit -m $1
git push

# 提交文档到 gh-pages 分支
cd docs
git add .
git commit -m $1
git push 