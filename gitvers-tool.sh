#!/bin/bash

###COLOR CLASS (ANSI escape codes) - note: with -e (echo option)

  #BASE
  red="\e[31m"
  rred="31" #bold dep
  gre="\e[32m"
  ggre="32" #bold dep
  yel="\e[33m"
  blu="\e[34m"
  mag="\e[35m"
  cya="\e[36m"
  ccya="36" #bold dep
  gry="\e[90m"
  ggry="90" #gry dep

  #BOLD
  bold="\033[1m"
  Bred="\e[1;${rred}m"
  Bgre="\e[1;${ggre}m"
  Bcya="\e[1;${ccya}m"

  #ITALIC
  Igry="\e[3;${ggry}m"

  #No COLOR
  end="\e[0m"

###FUNCTIONS
  function allDone(){
    echo -e "${gre}\nSuccessful !${end}"
    read -p "[ENTRER] pour retourner au menu..." example
  }

  function note(){
    echo -e "${cya}[note local working]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ${end}"
    echo "
    - Deplacer un ou plusieurs fichier(s) dans le dossier tmp pour etre ignorer de git
    - Editer le fichier README.md pour ajouter des informations a propos de votre projet
    - Il est fortement recommandE creer une nouvelle branche avant de travailler
    - N'oubliez pas de faire un sauvegarde a partir du script 'backup' si vous n'etes pas sur de vos manipulations
    "
    echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ${end}"
  }

  function gitConfigShow(){
    echo -e "${cya}\n[config-status-global]------------------------------------------ ${end}"
    git config --list
    echo -e "${cya}---------------------------------------------------------------- ${end}"
  }

  function listProj(){
    echo -e "${gre}Liste de projet: ${end}"
    #core
    echo -e "${cya}`ls ~/Project`${end}"
  }

  function clone(){
    echo -e "\nEntrer l'URL (HTTPS/SSH) du depot a cloner..."
    echo -e "${Bgre}"
    read -p "[URL> " clone
    echo -e "${end}"
    #core
    cd ~/Project/ && git clone $clone
    allDone
  }

  function config(){
    #email
    echo "Entrer un adresse e-mail valide..."
    echo -e "${Bgre}"
    read -p "[EMAIL> " newMail
    echo -e "${end}"
    #core
    git config --global user.email $newMail
    echo -e "${gre}e-mail ... [done] ${end}"
    sleep 0.35

    #name
    echo -e "\nEntrer votre nom..."
    echo -e "${Bgre}"
    read -p "[NAME> " newName
    echo -e "${end}"
    #core
    git config --global user.name $newName
    echo -e "${gre}name ... [done] ${end}"
    sleep 0.35

    #branch
    echo -e "\nEntrer la branche principale (par defaut = master)..."
    echo -e "${Bgre}"
    read -p "[BRANCH> " branch
    echo -e "${end}"
    #core
    git config --global init.defaultBranch $branch
    echo -e "${gre}init branch name is '$branch' now ... [done] ${end}"
    sleep 0.35

    #color syntax
    #core
    git config --global color.ui true
    echo -e "\n${gre}color syntax activated ... [done] ${end}"
    sleep 0.35

    #rebase
    #core
    git config --global branch.autosetuprebase always
    echo -e "\n${gre}rebase all pull (request) ... [done] ${end}"
    sleep 0.35

    #check config
    gitConfigShow
    allDone
  }

  function preConf(){
    echo -e "${Bcya} \n>>> REMOTE CONFIG <<<\n ${end}"
    sleep 2

    #local config
    cd ~/Project/$projectName && git init
    echo -e "${gre}git init ... [done] ${end}"
    echo -e "${gre}Generate .git ... [done] ${end}"
    sleep 1

    #gitignore
    cd ~/Project/$projectName && touch .gitignore
    echo -e "${gre}Generate .gitignore ... [done] ${end}"
    sleep 1

    #tmp
    cd ~/Project/$projectName && mkdir -p tmp && echo 'tmp' > .gitignore && echo 'tmp/*' >> .gitignore && echo '.gitignore' >> .gitignore
    echo -e "${gre}Generate tmp folder ... [done] ${end}"
    sleep 1

    #check .gitignore
    cd ~/Project/$projectName && cat .gitignore
    echo -e "${gre}Checking .gitignore ... [done] ${end}"
    sleep 1

    echo -e "\n"
    echo -e "${gre}all LOCAL config ... [done] ${end}"
    sleep 2
  }

  function create(){

    #project generator + config
    echo -e "${Bcya} \n>>> REMOTE PROJECT GENERATOR <<<\n ${end}"
    sleep 2

    #gen server
    mkdir -p ~/Project/Server/$projectName
    echo -e "${gre}Generate server '~/Project/Server/$projectName' ... [done] ${end}"
    sleep 1

    #git init --bare
    cd ~/Project/Server/$projectName && git init --bare
    echo -e "${gre}git init --bare ... [done] ${end}"
    sleep 1

    #preconf
    preConf
    note
    echo -e "${Igry} Vous pouvez maintenant entrer en mode 'REMOTE' pour valider ce vous avez creer...${end}"
    allDone
  }

  function genssh(){
    echo "Entrer votre adresse mail, SSH va utiliser l'adresse comme une etiquette pour la cle..."
    echo -e "${Bgre}"
    read -p "[EMAIL>" tag
    echo -e "${end}"
    #core
    ssh-keygen -t rsa -b 4096 -C "$tag"
    echo -e "${gre}Generate ssh-key (private|public) ... [done] ${end}"
    sleep 0.35
    allDone
  }

  function pubkey(){
    echo -e "${cya}[SSH-KEY (public)]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
    cat ~/.ssh/id_rsa.pub
    echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
    sleep 0.35
    allDone
  }

  function purge(){
    echo -e "\nEntrer le nom du projet a supprimer..."
    echo -e "${Bgre}"
    read -p "[PROJECT> " purge
    echo -e "${end}"
    echo -e "${red}"
    read -p "Vous etes en train de supprimer le projet '$purge', appuyez sur [ENTRER] pour continuer..." temp
    echo -e "${end}"
    #core
    cd ~/Project/$purge && git reset --hard && git clean -dffx && cd .. && rm -rf $purge
    echo "Suppression de $purge"
    sleep 0.35
    cd ~/Project/Server/ && rm -r $purge
    echo "Suppression de ~/Project/Server/$purge"
    sleep 0.35
    allDone
  }

  function backup(){
    echo -e "${mag}"
    read -p "Appuyez sur [ENTER] pour lancer le processus de sauvegarde, [CTRL + C] pour l'annuler..." temp
    echo -e "${end}"
    echo -e "${gre}All project/server backup ... [loading] ${end}"
    sleep 1
    #delete old backup
    echo -e "${gre}Deletion old backup (if exist) ... [Loading] ${end}"
    sleep 1
    cd ~/Project/ && rm -rf ALL-PROJECT-SERVER-BACKUP.tar.gz
    #compression
    echo -e "${gre}Compression all project ... [Loading] ${end}"
    sleep 1
    cd ~/Project/ && tar cvfz ALL-PROJECT-SERVER-BACKUP.tar.gz *
    echo -e "${Bgre}All project/server backup ... [done] ${end}"
    sleep 1
    allDone
  }

  function serverList(){
    echo -e "${bold}\n[SERVER LIST (used)]-------------------------------------------------------- ${end}"
    #core
    touch ~/Project/.remote.log && cat ~/Project/.remote.log
    echo -e "${Igry}\nNOTE: Entrer 'clear' pour nettoyer la liste du serveur enregistrEe ${end}"
    echo -e "${bold}---------------------------------------------------------------------------- ${end}"
  }

  function status(){
    echo -e "${bold}====================================== ${end}"
    #core
    cd ~/Project/$work && git status
    echo -e "${bold}====================================== ${end}"
    allDone
  }

  function status0(){
    echo -e "${bold}====================================== ${end}"
    cd ~/Project/$work && git status
    echo -e "${bold}====================================== ${end}"
  }

  function log(){
    echo -e "${bold}====================================== ${end}"
    #core
    cd ~/Project/$work && git log --graph --pretty='%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'
    echo -e "${bold}====================================== ${end}"
    allDone
  }

  function branchShow(){
    echo -e "${mag}Votre branche actuelle est =>${end} $branch "
  }

  function commit(){
    #commit model
    echo -e "${cya}[COMMIT model]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
    echo -e "[add]: message => ${Igry}ajout d'un ou plusieurs fichier${end}"
    echo -e "[del]: message => ${Igry}supression d'un ou plusieurs fichier${end}"
    echo -e "[fix]: message => ${Igry}correction de bug${end}"
    echo -e "[feature]: message => ${Igry}ajout fonctionnalitE${end}"
    echo -e "[docs]: message => ${Igry}mise a jour documentation${end}"
    echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n${end}"

    #git status
    status0

    #commit core
    echo -e "\n"
    branchShow
    echo -e "${bold}\nAjouter le nom du fichier a indexer (* pour tout ajouter)${end}"
    echo -e "${Bgre}"
    read -p "[ADD> " index
    echo -e "${end}"
    #core
    cd ~/Project/$work && git add $index
    sleep 0.35

    #git status
    status0

    #commit message
    echo -e "${Bgre}"
    read -p "[MESSAGE> " msg
    echo -e "${end}"
    #core
    cd ~/Project/$work && git commit -m "$msg"
    sleep 0.35

    echo -e "\n"
    status0
    allDone
  }

  function diff(){
    echo -e "${bold}====================================== ${end}"
    #core
    cd ~/Project/$work && git diff
    echo -e "${bold}====================================== ${end}"
    allDone
  }

###MAIN

  #blobal variable
  origin="origin"
  work="n/a"
  server="127.0.0.1"
  branch="n/a"

  while [ true ]; do
    echo -e "\n"
    echo -e "${Bred}            GITVERS-TOOL simple version${end}"
    sleep 1
    echo "========================================================="
    echo -e "${yel}Version: 1.0"
    #sleep 0.5
    echo -e "Author: Raja"
    #sleep 0.5
    git --version
    #sleep 0.5
    echo -e "${red}------------[PROJECT]------------${end}"
    #sleep 0.5
    listProj
    echo -e "${red}-------------[INIT]--------------${end}"
    #sleep 0.5
    echo -e "${blu}0.${end} enter un projet existant en mode remote"
    echo -e "${blu}1.${end} cloner un projet"
    echo -e "${blu}2.${end} configurer votre profil git"
    echo -e "${blu}3.${end} creer un projet (remote)"
    echo -e "${blu}4.${end} generer une cle ssh"
    echo -e "${blu}5.${end} afficher votre cle public"
    echo -e "${blu}${red}-------------[GIT]---------------${end}"
    #sleep 0.5
    echo -e "${blu}s.${end} git status ${Igry}[voir le status de votre projet]${end}"
    echo -e "${blu}l.${end} git log ${Igry}[voir l'historique]${end}"
    echo -e "${blu}c.${end} git commit ${Igry}[valider vos modifications]${end}"
    echo -e "${blu}m.${end} git merge ${Igry}[fusionner 2 branches]${end}"
    echo -e "${blu}df.${end} git diff ${Igry}[difference entre 2 etats de fichier]${end}"
    echo -e "${blu}cbr.${end} create branch ${Igry}[creer une branche]${end}"
    echo -e "${blu}dbr.${end} delete branch ${Igry}[supprimer une branche]${end}"
    echo -e "${blu}sbr.${end} switch branch ${Igry}[changer d'une branche]${end}"
    echo -e "${blu}lbr.${end} list branch (local + remote) ${Igry}[lister les branches existantes]${end}"
    echo -e "${blu}push.${end} send data ${Igry}[envoyer vos donnees vers le serveur]${end}"
    echo -e "${blu}pull.${end} receive data ${Igry}[recevoir des donnees depuis le serveur]${end}"
    echo -e "${blu}upt.${end} fast forward ${Igry}[mettre a jour rapidement le depot]${end}"

    echo -e "${red}------------[OTHERS]-------------${end}"
    #sleep 0.5
    echo -e "77. purge"
    echo -e "88. backup"
    echo -e "99. EXIT"
    echo "========================================================="
    if [ $work = "n/a" ]; then
      echo -e "${yel}[STATUS] =>${end} work: $work ${yel}|${end} branch: $branch ${yel}|${end} server: $server"
    else
      branch=`cd ~/Project/$work && git branch | grep -i '*'`
      echo -e "${yel}[STATUS] =>${end} work: $work ${yel}|${end} branch: $branch ${yel}|${end} server: $server"
    fi

    echo -e "${Bgre}"
    read -p "[INPUT> " input
    echo -e "${end}"

    #INPUT CASE
    case $input in

      0) #OK
        echo "Entrer le nom de votre projet..."
        echo -e "${Bgre}"
        read -p "[PROJECT> " work
        echo -e "${end}"

        #create ./gitvers-tool/tmp folder (if not exist)
        mkdir -p tmp
        echo -e "${gre}Generate 'tmp' in gitvers-tool folder ... [done] ${end}"
        sleep 1

        #re-exec & re-config .gitignore (specialy for gitvers-tool)
        #ignore .gitignore
        echo 'tmp' > .gitignore && echo 'tmp/*' >> .gitignore && echo 'gitignore' >> .gitignore
        echo -e "${gre}re-exec & re-config .gitignore ... [done] ${end}"
        sleep 1

        serverList

        #server input
        echo -e "\nEntrer le lien du serveur GIT (SSH/HTTPS)..."
        echo "Exemple: git@github.com:RajaRakoto/gitvers-tool.git"
        echo -e "${Bgre}"
        read -p "[SERVER> " server
        echo -e "${end}"

        #cleaning server log
        if [ $server = "clear" ] || [ $server = "CLEAR" ]; then
          echo -e "\n"
          cd tmp && rm -rf remote_tmp.log && touch remote_tmp.log
          cd ~/Project && rm -rf .remote.log && touch .remote.log
          echo -e "${gre}all server list cleared ... [done] ${end}"
          sleep 0.5
          serverList

          #server input
          echo -e "\nEntrer le lien du serveur GIT (SSH/HTTPS)..."
          echo "Exemple: git@github.com:RajaRakoto/gitvers-tool.git"
          echo -e "${Bgre}"
          read -p "[SERVER> " server
          echo -e "${end}"

          while [ $server = "clear" ] || [ $server = "CLEAR" ]; do
            echo -e "${mag}\nLa liste du serveur est deja vide...${end}"

            #server input
            echo -e "\nEntrer le lien du serveur GIT (SSH/HTTPS)..."
            echo "Exemple: git@github.com:RajaRakoto/gitvers-tool.git"
            echo -e "${Bgre}"
            read -p "[SERVER> " server
            echo -e "${end}"
          done
        fi

        #server log
        touch ./tmp/remote_tmp.log
        echo "[server]-> $server" >> ./tmp/remote_tmp.log
        cat ./tmp/remote_tmp.log > ~/Project/.remote.log
        echo -e "${gre}Server update to .remote.log ... [done] ${end}"
        sleep 1
        #origin
        echo -e "${gre}Config origin ... [done] ${end}"
        sleep 0.5
        cd ~/Project/$work && git remote add $origin $server
        #checking
        cd ~/Project/$work && git remote -v
        echo -e "${gre}Checking origin ... [done] ${end}"
        sleep 1
        echo -e "${Bgre}\nAll REMOTE config ... [done] ${end}"
        sleep 1.5


        allDone;;

      1) #OK
        clone;;

      2) #OK
        config;;

      3) #OK
        #creation du repertoire de travail Project
        mkdir -p ~/Project
        echo -e "\n${gre}generate '~/Project' folder ... [done] ${end}"
        echo -e "\n"

        #project name
        echo -e "${bold}\nPas d'espace sur le nom du projet... ${end}"
        echo -e "${Bgre}"
        read -p "[PROJET> " projectName
        echo -e "${end}"
        #core
        cd ~/Project/ && mkdir -p $projectName
        echo -e "Generate project '$projectName' folder ... [done] ${end}"
        sleep 1
        create;;

      4) #OK
        genssh;;

      5) #OK
        pubkey;;

      "s") #OK
        status;;

      "l") #OK
        log;;

      "c") #OK
        commit;;

      "m")
        echo "";;

      "df") #OK
        diff;;

      "cbr")
        echo "";;

      "dbr")
        echo "";;

      "sbr")
        echo "";;

      "lbr")
        echo "";;

      "push")
        echo "";;

      "pull")
        echo "";;

      "upt")
        echo "";;


      77) #OK
        purge;;

      88) #OK
        backup;;

      99) #OK
        echo "Merci d'utiliser gitvers-tool, a bientot !"
        break;;

      "exit") #OK
        echo "Merci d'utiliser gitvers-tool, a bientot !"
        break;;

      *) #OK
        echo -e "${red}[invalid input]...${nc}";;
    esac

  done
