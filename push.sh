###############################################################################
# 推送脚本
#
# · 作用：提交并推送主分支后，更新并推送 gh-pages 分支
# · 使用：`./push.sh <commit信息>`
###############################################################################
# 更新文档内容
gitbook build . docs

# 提交主目录
git add .
git commit -m $1
git push

# 提交文档到 gh-pages 分支
cd docs
git init
git add .
git commit -m $1
git push -f git@github.com:9527q/python-crash-course-note.git master:gh-pages
