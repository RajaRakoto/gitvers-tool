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
    read -p "[ENTRER] pour retourner au menu..." temp
  }

  function note(){
    echo -e "${cya}[note local working]"
    echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ${end}"
    echo "
    - Deplacer un ou plusieurs fichier(s) dans le dossier tmp pour etre ignorer de git
    - Editer le fichier README.md pour ajouter des informations a propos de votre projet
    - Il est fortement recommandE creer une nouvelle branche avant de travailler
    - N'oubliez pas de faire un sauvegarde a partir du script 'backup' si vous n'etes pas sur de vos manipulations
    "
    echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ${end}"
  }

  function gitConfigShow(){
    echo -e "${cya}[config-status-global]"
    echo -e "---------------------------------------------------------------- ${end}"
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
    # mkdir -p ~/Project/Server/$projectName
    # echo -e "${gre}Generate server '~/Project/Server/$projectName' ... [done] ${end}"
    # sleep 1

    #git init --bare
    # cd ~/Project/Server/$projectName && git init --bare
    # echo -e "${gre}git init --bare ... [done] ${end}"
    # sleep 1

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
    echo -e "${cya}[SSH-KEY (public)]"
    echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
    cat ~/.ssh/id_rsa.pub
    echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
    sleep 0.35
    allDone
  }

  function authorized_keys(){
    echo -e "${gry}Entrer le nom de la machine distante (ex: raja@192.168.8.100) ...${end}"
    echo -e "${Bgre}"
    read -p "[COMPUTER> " computer
    echo -e "${end}"
    #core
    ssh-copy-id $computer
    echo -e "${gre}Authorized_keys ... [done]${end}"
    sleep 0.35
    allDone
  }

  function sshConfig(){
    #create ssh bck
    sudo mkdir -p /etc/ssh/bck && cd /etc/ssh/ && cp -r ssh_config sshd_config bck/
    echo -e "${gre}ssh backuped ... [done]${end}"
    #guide
    echo ""
    echo -e "
${cya}~ VEUILLEZ NOTER et SUIVRE LES INSTRUCTIONS CI-DESSOUS ~
------------------------------------------------------------------------------------------------------------------------------${end}
1. Assurer que la machine source/cible est accessible (ping <ipv4 source/cible>)
2. Verifier que ssh (openssh-client|openssh-server) est bien installE sur chaque machine en tapant la commande 'ssh'
3. Verifier dans le champ ci-dessous que le dossier 'bck' a ete bien creer sinon creer manuellement un sauvegarde de la configuration ssh i-e '/etc/ssh'
"
ls /etc/ssh
echo -e "
4. Decommenter 'Port 22' dans 'ssh_config'
5. Decommenter 'Port 22', 'PubkeyAuthentication yes' et 'PermitRootLogin no' dans 'sshd_config'
${cya}------------------------------------------------------------------------------------------------------------------------------${end}
    "
    #core
    echo ""
    read -p "Appuyez sur [ENTRER] si vous etes pret a passer a l'etape de la configuration (ssh_config et sshd_config)..." temp
    sudo nano /etc/ssh/ssh_config
    sudo nano /etc/ssh/sshd_config
    #restart service
    echo ""
    sudo systemctl restart sshd.service && sudo systemctl restart ssh.service
    echo -e "${gre}restart all ssh service ... [done]${end}"

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
    echo -e "${cya}[COMMIT model]"
    echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n${end}"
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

  function merge(){
    cd ~/Project/$work && git checkout master 
    echo -e "${gre}Switch to branch master ... [done]${end}"
    sleep 0.35
    echo ""
    git branch
    echo "Entrer le nom de la branche a fusionner vers master"
    #core
    echo -e "${Bgre}"
    read -p "[MERGE> " merge
    echo -e "${end}"
    cd ~/Project/$work && git merge $merge
    echo -e "${gre}Merge to branch master ... [done]${end}"
    sleep 0.35
    allDone
  }

  function branch(){
    echo -e "Entrer le nom de la branche a creer"
    #core
    echo -e "${Bgre}"
    read -p "[BRANCH> " branch
    echo -e "${end}"
    cd ~/Project/$work && git branch $branch 
    echo -e "${gre}Create new branch '$branch' ... [done]${end}"
    sleep 0.35
    allDone
  }

  function delBranch(){
    cd ~/Project/$work && git branch -a
    echo -e "Entrer le nom de la branche a supprimer"
    #core
    echo -e "${Bgre}"
    read -p "[DEL> " branch
    echo -e "${end}"
    cd ~/Project/$work && git checkout master && git branch -d $branch 
    echo -e "${gre}Delete branch '$branch' ... [done]${end}"
    sleep 0.35
    allDone
  }

  function delOriginServer(){
    #list remote branch
    cd ~/Project/$work && git remote  
    echo -e "\nEntrer le nom du serveur a supprimer"
    #core
    echo -e "${Bgre}"
    read -p "[DEL> " server
    echo -e "${end}"
    cd ~/Project/$work && git remote remove $server 
    echo -e "${gre}Server '$server' deleted ... [done]${end}"
    sleep 0.35
    allDone
  }

  function switch(){
    git branch
    echo -e "Entrer le nom de la branche a changer"
    #core
    echo -e "${Bgre}"
    read -p "[SWITCH> " branch
    echo -e "${end}"
    cd ~/Project/$work && git checkout $branch
    echo -e "${gre}Switched to '$branch' ... [done]${end}"
    sleep 0.35
    allDone
  }

  function listBranch(){
    echo -e "${cya}[all branch list]"
    echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
    cd ~/Project/$work && git branch -a
    echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
    allDone
  }

  function push(){
    #push syntax
    echo -e "${cya}[PUSH syntax]"
    echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
    echo -e "<origin-id> <branch> => ${Igry}envoyer les donnees vers la machine qui se nomme '<origin-id>' de la branche '<branch>' du depot attachE a '<server>'${end}"
    echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n${end}"

    #core
    push="n/a"

      while [ ! $push = "q" ]; do
        echo -e "${gry}\n'q' pour sortir de push ...${end}"
        echo -e "${Bgre}"
        read -p "[PUSH> " push 
        echo -e "${end}"
        if [ $push = "q" ]; then
          break
        fi
        cd ~/Project/$work && git push $push
      done

    allDone
  }

  function pull(){
    #pull syntax
    echo -e "${cya}[PULL syntax]"
    echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
    echo -e "<origin-id> <branch> => ${Igry}recuperer les donnees vers la machine qui se nomme '<origin-id>' de la branche '<branch>' du depot attachE a '<server>'${end}"
    echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n${end}"

    #core
    pull="n/a"

      while [ ! $pull = "q" ]; do
        echo -e "${gry}\n'q' pour sortir de pull ...${end}"
        echo -e "${Bgre}"
        read -p "[PULL> " pull 
        echo -e "${end}"
        if [ $pull = "q" ]; then
          break
        fi
        cd ~/Project/$work && git pull $pull
      done

    allDone
  }

  function upstream(){
    read -p "Etes vous sur de vouloir mettre a jour votre depot local/fork ?, appuyez sur [ENTRER] pour continuer ..." tmp 

    #core
    echo ""
    echo "Entrer le URL(SSH) du depot original ..."
    echo -e "${Bgre}"
    read -p "[URL(SSH)> " url 
    echo -e "${end}"
	
    #verification remote branch
    cd ~/Project/$work && git remote -v
    echo -e "${gre}verify remote branch ... [done]${end}"
    sleep 0.35    

    #add upstream original url
    cd ~/Project/$work && git remote add upstream $url
    echo -e "${gre}upstream added ... [done]${end}"
    sleep 0.35

    #verify upstream branch
    cd ~/Project/$work && git remote -v
    echo -e "${gre}verify upstream branch ... [done]${end}"
    sleep 0.35
 
    #fetch upstream
    cd ~/Project/$work && git fetch upstream
    echo -e "${gre}fetch upstream ... [done]${end}"
    sleep 0.35s
    
    #merge changes from upstream/master
    cd ~/Project/$work && git merge upstream/master
    echo -e "${gre}merge upstream/master ... [done]${end}"
    sleep 0.35s
	
    #push changes to update your fork master on server 
    cd ~/Project/$work && git push $origin master
    echo -e "${gre}push changes to update your fork master on server ... [done]${end}"
    sleep 0.35s

    echo ""

    echo -e "${gre}fast-forward ... [done]${end}"
    sleep 0.35s

    allDone
  }

  function originList(){
    echo -e "${bold}\n[ORIGIN LIST (used)]-------------------------------------------------------- ${end}"
        #core
        cd ~/Project/$work && git remote -v
    echo -e "${bold}---------------------------------------------------------------------------- ${end}" 

    allDone
  } 

  function originRename(){
    echo -e "${bold}\n[ORIGIN LIST (used)]-------------------------------------------------------- ${end}"
        #core
        cd ~/Project/$work && git remote -v
    echo -e "${bold}---------------------------------------------------------------------------- ${end}"
    echo ""
    echo -e "Entrer origin ID (a renommer)"
    echo -e "${Bgre}"
    read -p "[ORIGIN ID> " oldOrigin
    echo -e "${end}"
    echo -e "Entrer un nouveau ID"
    echo -e "${Bgre}"
    read -p "[RENAME ID> " newOrigin
    echo -e "${end}"

    #core
    cd ~/Project/$work && git remote rename $oldOrigin $newOrigin
    origin=$newOrigin

    echo -e "${gre}rename '$oldOrigin' to '$newOrigin' ... [done]${end}"
    sleep 0.35

    echo -e "${bold}\n[ORIGIN LIST (used)]-------------------------------------------------------- ${end}"
        #core
        cd ~/Project/$work && git remote -v
    echo -e "${bold}---------------------------------------------------------------------------- ${end}"

    allDone
  }

  function validation(){
    echo -e "\n >>> VALIDATION <<<"
    sleep 0.5

    #create README file
    echo ""
    cd ~/Project/$work && echo '~ README ~' > README.md
    echo -e "${gre} Generate README.md ... [done]${end}"
    sleep 0.35

    #first pull
    echo ""
    cd ~/Project/$work && git pull $origin master
    echo -e "${gre}pull verification ... [done]${end}"
    sleep 0.35

    #status & add & commit & push (master)
    echo ""
    cd ~/Project/$work && git status 
    echo -e "${gre}check status 1 ... [done]${end}"
    sleep 0.35

    echo ""
    cd ~/Project/$work && git add *
    echo -e "${gre}add ... [done]${end}"
    sleep 0.35

    echo ""
    cd ~/Project/$work && git status 
    echo -e "${gre}check status 2 ... [done]${end}"
    sleep 0.35

    echo ""
    cd ~/Project/$work && git commit -m 'validation'
    echo -e "${gre}1st commit ... [done]${end}"
    sleep 0.35

    echo ""
    cd ~/Project/$work && git push $origin master
    echo -e "${gre}VALIDATION ... [done]${end}"
    sleep 0.35

    allDone
  }

###MAIN

  #blobal variable
  origin="n/a"
  work="n/a"
  server="127.0.0.1"
  branch="n/a"

  #create 'Project' folder
  mkdir -p ~/Project

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
    echo -e "${mag}<start>${end}"
    echo -e "${blu}0.${end} entrer un projet existant en mode remote"
    echo -e "${blu}1.${end} cloner un projet"
    echo -e "${blu}2.${end} configurer votre profil git"
    echo -e "${blu}3.${end} creer un projet (remote)"
    echo -e "${mag}<ssh>${end}"
    echo -e "${blu}4.${end} generer une cle ssh"
    echo -e "${blu}5.${end} afficher votre cle public"
    echo -e "${blu}6.${end} ajouter votre cle ssh dans une machine distante"
    echo -e "${blu}7.${end} config ssh de la machine courante"
    echo -e "${blu}${red}-------------[GIT]---------------${end}"
    #sleep 0.5
    echo -e "${mag}<basic>${end}"
    echo -e "${blu}s.${end} git status ${Igry}[voir le status de votre projet]${end}"
    echo -e "${blu}l.${end} git log ${Igry}[voir l'historique]${end}"
    echo -e "${blu}c.${end} git commit ${Igry}[valider vos modifications]${end}"
    echo -e "${blu}m.${end} git merge ${Igry}[fusionner une branche vers master]${end}"
    echo -e "${blu}df.${end} git diff ${Igry}[difference entre 2 etats de fichier]${end}"
    echo -e "${mag}<branch>${end}"
    echo -e "${blu}cbr.${end} create branch ${Igry}[creer une branche]${end}"
    echo -e "${blu}dbr.${end} delete branch ${Igry}[supprimer une branche]${end}"
    echo -e "${blu}sbr.${end} switch branch ${Igry}[changer d'une branche]${end}"
    echo -e "${blu}lbr.${end} list branch (local + remote) ${Igry}[lister les branches existantes]${end}"
    echo -e "${mag}<remote>${end}"
    echo -e "${blu}push.${end} send data ${Igry}[envoyer vos donnees vers le serveur]${end}"
    echo -e "${blu}pull.${end} receive data ${Igry}[recevoir des donnees depuis le serveur]${end}"
    echo -e "${blu}update.${end} fast forward ${Igry}[mettre a jour rapidement le depot]${end}"
    echo -e "${mag}<origin/server>${end}"
    echo -e "${blu}lorg.${end} list origin ${Igry}[lister l'ID origin du depot en cours]${end}"
    echo -e "${blu}norg.${end} rename origin ${Igry}[renommer l'ID origin du depot en cours]${end}"
    echo -e "${blu}dorg.${end} delete origin/server ${Igry}[supprimer un serveur]${end}"
    echo -e "${mag}<validation>${end}"
    echo -e "${blu}valid.${end} valid new project ${Igry}[valider un projet nouvellement creE]${end}"
    echo -e "${red}------------[OTHERS]-------------${end}"
    #sleep 0.5
    echo -e "${blu}77.${end} purge"
    echo -e "${blu}88.${end} backup"
    echo -e "${blu}99.${end} EXIT"
    echo "========================================================="
    if [ $work = "n/a" ]; then
      echo -e "${yel}[STATUS] =>${end} work: $work ${yel}|${end} branch: $branch ${yel}|${end} origin-id: $origin \nserver: $server"
    else
      branch=`cd ~/Project/$work && git branch | grep -i '*'`
      echo -e "${yel}[STATUS] =>${end} work: $work ${yel}|${end} branch: $branch ${yel}|${end} origin-id: $origin \nserver: $server"
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
        echo 'tmp' > .gitignore && echo 'tmp/*' >> .gitignore && echo '.gitignore' >> .gitignore
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

        #def origin
        echo -e "${bold}\n[ORIGIN LIST (used)]-------------------------------------------------------- ${end}"
        #core
        cd ~/Project/$work && git remote -v
        echo -e "${bold}---------------------------------------------------------------------------- ${end}"  
        echo ""
        echo "Entrer l'ID origin pour le serveur => '$server'"
        echo -e "$Bgre"
        read -p "[ID> " origin
        echo -e "$end"
        echo -e "${gre}Define origin ID to '$origin' ... [done]${end}"
        echo ""

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
        echo -e "${bold}\nPas d'espace sur le nom de projet... ${end}"
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

      6) #OK
        authorized_keys;;

      7) #OK
        sshConfig;;

      "s") #OK
        status;;

      "l") #OK
        log;;

      "c") #OK
        commit;;

      "m") #OK
        merge;;

      "df") #OK
        diff;;

      "cbr") #OK
        branch;;

      "dbr") #OK
        delBranch;;

      "sbr") #OK
        switch;;

      "lbr") #OK
        listBranch;;

      "push") #test *
        push;;

      "pull") #test *
        pull;;

      "update") #test *
        upstream;;

      "lorg") #OK
        originList;;

      "norg") #OK
        originRename;;

      "dorg") #OK
        delOriginServer;;
      
      "valid") #OK
        validation;;

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
