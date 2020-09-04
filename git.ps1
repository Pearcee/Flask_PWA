

$comment = $args[0]
git status
git add --all .
git commit -m $comment
git push -u origin master