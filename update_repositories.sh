
for file in `ls -d pe-*`
do
  echo updating repository $file
  cd $file
  git checkout develop
  git pull
  cd ..
done

