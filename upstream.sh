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

#create log file
touch .log-server
echo -e "${gre}log-server ... [done]${end}"

#to .gitignore
echo "upstream.sh" >>.gitignore
echo ".log-server" >>.gitignore

function upstream() {
  read -p "Assurez-vous que 'upstream.sh' est bien dans le dossier de votre depot local pour le mettre a jour ainsi son fork par rapport au depot original ? appuyez sur [ENTRER] pour continuer ..." tmp

  #core
  echo ""
  echo "Entrer le URL(SSH) du depot original que vous avez forkE ... (Ex: git@github.com:RajaRakoto/gitvers-tool.git)"
  echo ""
  echo -e "Les 5 derniers depots deja utilisEs par ce script"
  echo -e "[server]--------------------"
  tail -n 5 .log-server
  echo -e "----------------------------"
  echo -e "${Bgre}"
  read -p "[URL(SSH)> " url
  echo -e "${end}"
  echo "=> $url" >>.log-server

  #verification remote branch
  git remote -v
  echo -e "${gre}verify remote branch ... [done]${end}"
  sleep 0.35

  #add upstream original url
  git remote add upstream $url
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
  git push $origin master
  echo -e "${gre}push changes to update your fork master on server ... [done]${end}"
  sleep 0.35s

  echo ""
  echo -e "${gre}\nSUCCESSFUL !${end}"
}
