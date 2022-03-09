#!/bin/bash

red="\e[31m"
rred="31"
gre="\e[32m"
ggre="32"
yel="\e[33m"
blu="\e[34m"
mag="\e[35m"
cya="\e[36m"
ccya="36"
gry="\e[90m"
ggry="90"
bold="\033[1m"
Bred="\e[1;${rred}m"
Bgre="\e[1;${ggre}m"
Bcya="\e[1;${ccya}m"
Igry="\e[3;${ggry}m"
end="\e[0m"

#create log files
touch .log-original-repo
touch .log-fork-repo
echo -e "${gre}log-original-repo & log-fork-repo ... [done]${end}"

#to .gitignore
echo "upstream.sh" >>.gitignore
echo ".log-original-repo" >>.gitignore
echo ".log-fork-repo" >>.gitignore

function upstream() {
  read -p "Assurez-vous que 'upstream.sh' est bien dans le dossier de votre depot local pour le mettre a jour ainsi son fork par rapport au depot original ? appuyez sur [ENTRER] pour continuer ..." tmp

  #core
  echo ""
  echo "Entrer le URL(SSH) du depot original ... (Ex: git@github.com:RajaRakoto/gitvers-tool.git)"
  echo ""
  echo -e "[original-repository]---------------[log]"
  tail -n 5 .log-original-repo
  echo -e "-----------------------------------------"
  echo -e "${Bgre}"
  read -p "[URL(SSH)> " origin
  echo -e "${end}"
  echo "=> $origin" >>.log-original-repo
  echo ""
  user=`whoami`
  echo "Entrer le URL(SSH) du depot fork ... (Ex: git@github.com:$user/gitvers-tool.git)"
  echo ""
  echo -e "[fork-repository]-------------------[log]"
  tail -n 5 .log-fork-repo
  echo -e "-----------------------------------------"
  echo -e "${Bgre}"
  read -p "[URL(SSH)> " fork
  echo -e "${end}"
  echo "=> $fork" >>.log-fork-repo

  #verification remote branch
  git remote -v
  echo -e "${gre}verify remote branch ... [done]${end}"
  sleep 0.35

  #add upstream original url
  git remote add upstream $origin
  echo -e "${gre}upstream added ... [done]${end}"
  sleep 0.35

  #verify upstream branch
  git remote -v
  echo -e "${gre}verify upstream branch ... [done]${end}"
  sleep 0.35

  #fetch upstream
  git fetch upstream
  echo -e "${gre}fetch upstream ... [done]${end}"
  sleep 0.35s

  #merge changes from upstream/master
  git merge upstream/master
  echo -e "${gre}merge upstream/master ... [done]${end}"
  sleep 0.35s

  #push changes to update your fork master on server
  git push $fork master
  echo -e "${gre}push changes to update your fork master on server ... [done]${end}"
  sleep 0.35s

  echo ""
  echo -e "${gre}\nSUCCESSFUL !${end}"
}

upstream
