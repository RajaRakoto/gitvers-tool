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

###############################
########## FUNCTION ###########
###############################

function allDone() {
  echo -e "${gre}\nSuccessful !${end}"
  read -p "[ENTER] to return to menu..." temp
}

function gitConfigShow() {
  echo -e "${cya}[config-status-global]"
  echo -e "---------------------------------------------------------------- ${end}"
  git config --list
  echo -e "${cya}---------------------------------------------------------------- ${end}"
}

function listProj() {
  echo -e "${gre}Project list: ${end}"
  echo -e "${cya}$(ls ~/Projects)${end}"
}

function clone() {
  echo -e "\nEnter the URL (HTTPS/SSH) of the repository to clone"
  echo -e "${Bgre}"
  read -p "[URL> " clone
  echo -e "${end}"
  cd ~/Projects/ && git clone $clone
  allDone
}

function config() {
  #e-mail
  echo "Enter a valid email address"
  echo -e "${Bgre}"
  read -p "[EMAIL> " newMail
  echo -e "${end}"
  git config --global user.email $newMail
  echo -e "${gre}E-mail configured ... [done] ${end}"
  sleeping 0.35

  #name
  echo -e "\nEnter your name"
  echo -e "${Bgre}"
  read -p "[NAME> " newName
  echo -e "${end}"
  git config --global user.name $newName
  echo -e "${gre}Name configured ... [done] ${end}"
  sleeping 0.35

  #branch
  echo -e "\nEnter master branch (default = master)"
  echo -e "${Bgre}"
  read -p "[BRANCH> " branch
  echo -e "${end}"
  git config --global init.defaultBranch $branch
  echo -e "${gre}Init branch name is '$branch' now ... [done] ${end}"
  sleeping 0.35

  #color syntax
  git config --global color.ui true
  echo -e "\n${gre}Color syntax activated ... [done] ${end}"
  sleeping 0.35

  #rebase
  git config --global branch.autosetuprebase always
  echo -e "\n${gre}Rebase all pull (request) ... [done] ${end}"
  sleeping 0.35

  #check config
  gitConfigShow
  allDone
}

# TODO: test
function preConf() {
  echo -e "${Bcya} \n>>> REMOTE CONFIG <<<\n ${end}"
  sleep 2

  #local config
  cd ~/Projects/$projectName && git init
  echo -e "${gre}Git init ... [done] ${end}"
  echo -e "${gre}Generate .git ... [done] ${end}"
  sleep 1

  #gitignore
  cd ~/Projects/$projectName && touch .gitignore
  echo -e "${gre}Generate .gitignore ... [done] ${end}"
  sleep 1

  #config .gitignore
  echo 'tmp' >~/Projects/$projectName/.gitignore && echo 'node_modules' >>~/Projects/$projectName/.gitignore && echo '.originalRepo.log' >>~/Projects/$projectName/.gitignore && echo '.forkedRepo.log' >>~/Projects/$projectName/.gitignore && echo 'backups' >>~/Projects/$projectName/.gitignore && echo '.gitignore' >>~/Projects/$projectName/.gitignore
  echo -e "$.gitignore configured ... [done] ${end}"
  sleep 1

  #tmp
  cd ~/Projects/$projectName && mkdir -p tmp
  echo -e "${gre}Generate tmp folder ... [done] ${end}"
  sleep 1

  #check .gitignore
  cd ~/Projects/$projectName && cat .gitignore
  echo -e "${gre}Checking .gitignore ... [done] ${end}"
  sleep 1

  echo -e "\n"
  echo -e "${gre}All local config ... [done] ${end}"
  sleep 2
}

function create() {

  #project generator + config
  echo -e "${Bcya} \n>>> REMOTE PROJECT GENERATOR <<<\n ${end}"
  sleeping 2

  #preconf
  preConf
  echo -e "${Igry} you can now enter 'REMOTE' mode to validate what you have created ...${end}"
  allDone
}

function genssh() {
  echo "Enter your email address, SSH will use the address as a label for the key..."
  echo -e "${Bgre}"
  read -p "[EMAIL>" tag
  echo -e "${end}"
  ssh-keygen -t rsa -b 4096 -C "$tag"
  echo -e "${gre}Generate ssh-key (private|public) ... [done] ${end}"
  sleep 0.35
  allDone
}

function pubkey() {
  echo -e "${cya}[SSH-KEY (public)]"
  echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
  cat ~/.ssh/id_rsa.pub
  echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
  sleep 0.35
  allDone
}

function authorized_keys() {
  echo -e "${gry}Enter remote machine name (ex: raja@192.168.8.100) ...${end}"
  echo -e "${Bgre}"
  read -p "[COMPUTER> " computer
  echo -e "${end}"
  ssh-copy-id $computer
  echo -e "${gre}Authorized_keys ... [done]${end}"
  sleeping 0.35
  allDone
}

function sshConfig() {
  #create ssh bck
  sudo mkdir -p /etc/ssh/bck && cd /etc/ssh/ && cp -r ssh_config sshd_config bck/
  echo -e "${gre}SSH backuped ... [done]${end}"
  #guide
  echo ""
  echo -e "
${cya}~ PLEASE NOTE and FOLLOW INSTRUCTIONS BELOW~
-------------------------------------------------- -------------------------------------------------- ------------${end}
1. Ensure that the source/target machine is accessible (ping <ipv4 source/target>)
2. Check that ssh (openssh-client|openssh-server) is installed on each machine by typing the command 'ssh'
3. Check in the field below that the 'bck' folder has been created, otherwise manually create a backup of the ssh configuration i-e '/etc/ssh'
"
  ls /etc/ssh
  echo -e "
4. Uncomment 'Port 22' in 'ssh_config'
5. Uncomment 'Port 22', 'PubkeyAuthentication yes' and 'PermitRootLogin no' in 'sshd_config'
${cya}---------------------------------------------- -------------------------------------------------- ------------------------------${end}
"
  echo ""
  read -p "Press [ENTER] if you are ready to proceed to the configuration step (ssh_config and sshd_config)..." temp
  sudo nano /etc/ssh/ssh_config
  sudo nano /etc/ssh/sshd_config
  #restart service
  echo ""
  sudo systemctl restart sshd.service && sudo systemctl restart ssh.service
  echo -e "${gre}Restart all ssh service ... [done]${end}"

  allDone
}

function purge() {
  echo -e "\nEnter name of the project to delete..."
  echo -e "${Bgre}"
  read -p "[PROJECT> " purge
  echo -e "${end}"
  echo -e "${red}"
  read -p "You are deleting project '$purge', press [ENTER] to continue..." temp
  echo -e "${end}"
  cd ~/Projects/$purge && git reset --hard && git clean -dffx && cd .. && rm -rf $purge
  echo "Deleting $purge"
  sleeping 0.35
  allDone
}

function backup() {
  echo -e "${mag}"
  read -p "Press [ENTER] to start backup process, [CTRL+C] to cancel..." temp
  echo -e "${end}"
  echo -e "${gre}All project/server backup ... [loading] ${end}"
  sleeping 1
  #delete old backup
  echo -e "${gre}Delete old backup (if exist) ... [Loading] ${end}"
  sleeping 1
  cd ~/Projects/ && rm -rf bac.tar.gz
  #compression
  echo -e "${gre}Compression all project ... [Loading] ${end}"
  sleeping 1
  cd ~/Projects/ && tar cvfz bac.tar.gz *
  echo -e "${Bgre}All project/server backup ... [done] ${end}"
  sleeping 1
  allDone
}

# TODO: test
function serverList() {
  echo -e "${bold}\n[SERVER LIST (used)]--------------------------------------------------------${end}"
  touch ~/Projects/$work/.server.log && tail -n 5 ~/Projects/$work/.server.log
  echo -e "${Igry}\nNOTE: Enter 'clear' to clear the saved server list ${end}"
  echo -e "${bold}------------------------------------------------------------------------------------------- ${end}"
}

function status() {
  echo -e "${bold}====================================== ${end}"
  cd ~/Projects/$work && git status
  echo -e "${bold}====================================== ${end}"
  allDone
}

function status0() {
  echo -e "${bold}====================================== ${end}"
  cd ~/Projects/$work && git status
  echo -e "${bold}====================================== ${end}"
}

function log() {
  echo -e "${bold}====================================== ${end}"
  cd ~/Projects/$work && git log --graph --pretty='%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'
  echo -e "${bold}====================================== ${end}"
  allDone
}

function branchShow() {
  echo -e "${mag}Your current branch is =>${end} $branch"
}

# TODO: test
function commit() {
  #commit model
  echo -e "${cya}[COMMIT model]"
  echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~\n${end}"
  echo -e "[add]: message => ${Igry}add file(s)${end}"
  echo -e "[del]: message => ${Igry}delete file(s)${end}"
  echo -e "[fix]: message => ${Igry}bug fix${end}"
  echo -e "[feat]:message => ${Igry}adding feature${end}"
  echo -e "[docs]: message => ${Igry}documentation update${end}"
  echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~\n${end}"

  status0

  #commit core
  echo -e "\n"
  branchShow
  echo -e "${bold}\nAdd name of file to index (* to add all)${end}"
  echo -e "${Bgre}"
  read -p "[ADD> " index
  echo -e "${end}"
  cd ~/Projects/$work && git add $index
  sleeping 0.35

  status0

  #commit message
  echo -e "${Bgre}"
  read -p "[MESSAGE> " msg
  echo -e "${end}"
  cd ~/Projects/$work && git commit -m "$msg"
  sleep 0.35

  echo -e "\n"
  status0
  allDone
}

function diff() {
  echo -e "${bold}====================================== ${end}"
  cd ~/Projects/$work && git diff
  echo -e "${bold}====================================== ${end}"
  allDone
}

function merge() {
  cd ~/Projects/$work && git checkout master
  echo -e "${gre}Switch to branch master ... [done]${end}"
  sleeping 0.35
  echo ""
  git branch
  echo "Enter branch name to merge into master"
  echo -e "${Bgre}"
  read -p "[MERGE> " merge
  echo -e "${end}"
  cd ~/Projects/$work && git merge $merge
  echo -e "${gre}Merge to branch master ... [done]${end}"
  sleeping 0.35
  allDone
}

function branch() {
  echo -e "Enter name of the branch to create"
  echo -e "${Bgre}"
  read -p "[BRANCH> " branch
  echo -e "${end}"
  cd ~/Projects/$work && git branch $branch
  echo -e "${gre}Create new branch '$branch' ... [done]${end}"
  sleeping 0.35
  allDone
}

function delBranch() {
  cd ~/Projects/$work && git branch -a
  echo -e "Enter name of branch to delete"
  echo -e "${Bgre}"
  read -p "[DEL> " branch
  echo -e "${end}"
  cd ~/Projects/$work && git checkout master && git branch -d $branch
  echo -e "${gre}Delete branch '$branch' ... [done]${end}"
  sleeping 0.35
  allDone
}

function delOriginServer() {
  #list remote branch
  cd ~/Projects/$work && git remote
  echo -e "\nEnter name of the server to delete"
  echo -e "${Bgre}"
  read -p "[DEL> " server
  echo -e "${end}"
  cd ~/Projects/$work && git remote remove $server
  echo -e "${gre}Server '$server' deleted ... [done]${end}"
  sleeping 0.35
  allDone
}

function switch() {
  git branch
  echo -e "Enter branch name to change"
  echo -e "${Bgre}"
  read -p "[SWITCH> " branch
  echo -e "${end}"
  cd ~/Projects/$work && git checkout $branch
  echo -e "${gre}Switched to '$branch' ... [done]${end}"
  sleeping 0.35
  allDone
}

function listBranch() {
  echo -e "${cya}[all branch list]"
  echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
  cd ~/Projects/$work && git branch -a
  echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
  allDone
}

# TODO: test | fix
function push() {
  #push syntax
  echo -e "${cya}[PUSH syntax]"
  echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
  echo -e "<origin-id> <branch> => ${Igry} send data to the machine named '<origin-id>' of branch '<branch>' of the repository attached to '<server> '${end}"
  echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n${end}"
  push="n/a"

  while [ ! $push = "q" ]; do
    echo -e "${gry}\n'q' to exit push ...${end}"
    echo -e "${Bgre}"
    read -p "[PUSH> " push
    echo -e "${end}"
    if [ $push = "q" ]; then
      break
    fi
    cd ~/Projects/$work && git push $push
  done

  allDone
}

# TODO: test | fix
function pull() {
  #pull syntax
  echo -e "${cya}[PULL syntax]"
  echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~${end}"
  echo -e "<origin-id> <branch> => ${Igry} retrieve data to the machine named '<origin-id>' from branch '<branch>' of the repository attached to '<server> '${end}"
  echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~\n${end}"
  pull="n/a"

  while [ ! $pull = "q" ]; do
    echo -e "${gry}\n'q' to exit pull ...${end}"
    echo -e "${Bgre}"
    read -p "[PULL> " pull
    echo -e "${end}"
    if [ $pull = "q" ]; then
      break
    fi
    cd ~/Projects/$work && git pull $pull
  done

  allDone
}

# TODO: test
function upstream() {
  #create log files
  touch ~/Projects/$work/tmp/.originalRepo.log
  touch ~/Projects/$work/tmp/.forkedRepo.log
  echo -e "${gre}Generate originalRepo.log & forkedRepo.log ... [done]${end}"

  echo ""
  echo "Enter URL(SSH) of original repository ... (Ex: git@github.com:RajaRakoto/gitvers-tool.git)"
  echo ""
  echo -e "[original-repository]---------------[log]"
  tail -n 5 ~/Projects/$work/tmp/.originalRepo.log
  echo -e "-----------------------------------------"
  echo -e "${Bgre}"
  read -p "[URL(SSH)> " origin
  echo -e "${end}"
  echo "=> $origin" >>~/Projects/$work/tmp/.originalRepo.log
  echo ""
  user=$(whoami)
  echo "Enter fork repository URL(SSH) ... (Ex: git@github.com:$user/gitvers-tool.git)"
  echo ""
  echo -e "[fork-repository]-------------------[log]"
  tail -n 5 ~/Projects/$work/tmp/.forkedRepo.log
  echo -e "-----------------------------------------"
  echo -e "${Bgre}"
  read -p "[URL(SSH)> " fork
  echo -e "${end}"
  echo "=> $fork" >>~/Projects/$work/tmp/.forkedRepo.log

  #verification remote branch
  cd ~/Projects/$work && git remote -v
  echo -e "${gre}Verify remote branch ... [done]${end}"
  sleep 0.35

  #add upstream original url
  cd ~/Projects/$work && git remote add upstream $origin
  echo -e "${gre}Upstream added ... [done]${end}"
  sleep 0.35

  #verify upstream branch
  cd ~/Projects/$work && git remote -v
  echo -e "${gre}Verify upstream branch ... [done]${end}"
  sleep 0.35

  #fetch upstream
  cd ~/Projects/$work && git fetch upstream
  echo -e "${gre}Fetch upstream ... [done]${end}"
  sleep 0.35s

  #merge changes from upstream/master
  cd ~/Projects/$work && git merge upstream/master
  echo -e "${gre}Merge upstream/master ... [done]${end}"
  sleep 0.35s

  #push changes to update your fork master on server
  cd ~/Projects/$work && git push $fork master
  echo -e "${gre}Push changes to update your fork master on server ... [done]${end}"
  sleep 0.35s

  allDone
}

function originList() {
  echo -e "${bold}\n[ORIGIN LIST (used)]-------------------------------------------------------- ${end}"
  cd ~/Projects/$work && git remote -v
  echo -e "${bold}---------------------------------------------------------------------------- ${end}"

  allDone
}

function originRename() {
  echo -e "${bold}\n[ORIGIN LIST (used)]-------------------------------------------------------- ${end}"
  cd ~/Projects/$work && git remote -v
  echo -e "${bold}---------------------------------------------------------------------------- ${end}"
  echo ""
  echo -e "Enter origin ID (to rename)"
  echo -e "${Bgre}"
  read -p "[ORIGIN ID> " oldOrigin
  echo -e "${end}"
  echo -e "Enter new ID"
  echo -e "${Bgre}"
  read -p "[RENAME ID> " newOrigin
  echo -e "${end}"

  cd ~/Projects/$work && git remote rename $oldOrigin $newOrigin
  origin=$newOrigin

  echo -e "${gre}rename '$oldOrigin' to '$newOrigin' ... [done]${end}"
  sleep 0.35

  echo -e "${bold}\n[ORIGIN LIST (used)]-------------------------------------------------------- ${end}"
  cd ~/Projects/$work && git remote -v
  echo -e "${bold}---------------------------------------------------------------------------- ${end}"

  allDone
}

# TODO: test
function validation() {
  echo -e "\n >>> VALIDATION <<<"
  sleep 0.5

  #first pull
  echo ""
  cd ~/Projects/$work && git pull $origin master
  echo -e "${gre}pull verification ... [done]${end}"
  sleep 0.35

  #status & add & commit & push (master)
  echo ""
  cd ~/Projects/$work && git status
  echo -e "${gre}Check status ... [done]${end}"
  sleep 0.35

  echo ""
  cd ~/Projects/$work && git add *
  echo -e "${gre}Add all ... [done]${end}"
  sleep 0.35

  echo ""
  cd ~/Projects/$work && git status
  echo -e "${gre}Check status ... [done]${end}"
  sleep 0.35

  echo ""
  cd ~/Projects/$work && git commit -m '1st commit'
  echo -e "${gre}1st commit ... [done]${end}"
  sleep 0.35

  echo ""
  cd ~/Projects/$work && git push $origin master
  echo -e "${gre}VALIDATION ... [done]${end}"
  sleep 0.35

  allDone
}

###########################
########## MAIN ###########
###########################

#blobal variable
origin="n/a"
work="n/a"
server="127.0.0.1"
branch="n/a"

#create 'Projects' folder
mkdir -p ~/Projects

while [ true ]; do
  echo -e "\n"
  echo -e "${Bred}            GITVERS-TOOL${end}"
  sleep 1
  echo "========================================================="
  echo -e "${yel}Version: 2.0.0"
  #sleep 0.5
  echo -e "Author: Raja"
  #sleep 0.5
  git --version
  #sleep 0.5
  echo -e "${red}------------[PROJECTS]------------${end}"
  #sleep 0.5
  listProj
  echo -e "${red}-------------[INIT]--------------${end}"
  #sleep 0.5
  echo -e "${mag}<START>${end}"
  echo -e "${blu}0.${end} Working on a git project"
  echo -e "${blu}1.${end} Clone git project"
  echo -e "${blu}2.${end} Configure your git profile"
  echo -e "${blu}3.${end} Create git project"
  echo -e "${mag}<SSH>${end}"
  echo -e "${blu}4.${end} Generate SSH key"
  echo -e "${blu}5.${end} Show your public key"
  echo -e "${blu}6.${end} Add your SSH key to a remote machine"
  echo -e "${blu}7.${end} SSH config of current machine"
  echo -e "${blu}${red}-------------[GIT]---------------${end}"
  #sleep 0.5
  echo -e "${mag}<BASICS>${end}"
  echo -e "${blu}s.${end} git status ${Igry}[see your project status]${end}"
  echo -e "${blu}l.${end} git log ${Igry}[view your project history]${end}"
  echo -e "${blu}c.${end} git commit ${Igry}[commit your changes]${end}"
  echo -e "${blu}m.${end} git merge ${Igry}[merge branch to master]${end}"
  echo -e "${blu}df.${end} git diff ${Igry}[difference between 2 file states]${end}"
  echo -e "${mag}<BRANCH>${end}"
  echo -e "${blu}cbr.${end} Create branch ${Igry}[create new branch]${end}"
  echo -e "${blu}dbr.${end} Delete branch ${Igry}[delete branch]${end}"
  echo -e "${blu}sbr.${end} Switch branch ${Igry}[move to another branch]${end}"
  echo -e "${blu}lbr.${end} List branch (local + remote) ${Igry}[list all existing branches]${end}"
  echo -e "${mag}<REMOTE>${end}"
  echo -e "${blu}push.${end} Send data ${Igry}[send your data to server]${end}"
  echo -e "${blu}pull.${end} Receive data ${Igry}[receive data from server]${end}"
  echo -e "${blu}update.${end} Fast forward ${Igry}[update local and remote repository]${end}"
  echo -e "${mag}<ORIGIN|SERVER>${end}"
  echo -e "${blu}lorg.${end} List origin ${Igry}[list origin id of current repository]${end}"
  echo -e "${blu}norg.${end} Rename origin ${Igry}[rename origin id of current repository]${end}"
  echo -e "${blu}dorg.${end} Delete origin|server ${Igry}[delete server]${end}"
  echo -e "${mag}<COMMIT>${end}"
  echo -e "${blu}valid.${end} Valid new git project ${Igry}[validate newly created git project]${end}"
  echo -e "${red}------------[OTHERS]-------------${end}"
  #sleep 0.5
  echo -e "${blu}77.${end} Purge ${Igry}[delete git project cleanly]${end}"
  echo -e "${blu}88.${end} Backup ${Igry}[create a backup of your git projects]${end}"
  echo -e "${blu}99.${end} EXIT"
  echo "========================================================="
  if [ $work = "n/a" ]; then
    echo -e "${yel}[STATUS] =>${end} work: $work ${yel}|${end} branch: $branch ${yel}|${end} origin-id: $origin \nserver: $server"
  else
    branch=$(cd ~/Projects/$work && git branch | grep -i '*')
    echo -e "${yel}[STATUS] =>${end} work: $work ${yel}|${end} branch: $branch ${yel}|${end} origin-id: $origin \nserver: $server"
  fi

  echo -e "${Bgre}"
  read -p "[INPUT> " input
  echo -e "${end}"

  case $input in

  0)
    echo "Enter your project name..."
    echo -e "${Bgre}"
    read -p "[PROJECT> " work
    echo -e "${end}"

    serverList

    function serverInput() {
      echo -e "\nEnter git repository link (SSH/HTTPS)..."
      echo "Example: git@github.com:RajaRakoto/gitvers-tool.git"
      echo -e "${Bgre}"
      read -p "[REPO> " server
      echo -e "${end}"
    }

    serverInput

    #server log
    echo "[repository]-> $server" >>~/Projects/$work/tmp/server.log
    echo -e "${gre}Repository list updated from .server.log ... [done] ${end}"
    sleep 1

    #cleaning server log
    if [ $server = "clear" ] || [ $server = "CLEAR" ]; then
      echo -e "\n"
      echo "" >~/Projects/$work/tmp/.server.log
      echo -e "${gre}All repository list cleared ... [done] ${end}"
      sleep 0.5
      serverList

      serverInput
    fi

    #def origin
    echo -e "${bold}\n[ORIGIN LIST (used)]-------------------------------------------------------- ${end}"
    cd ~/Projects/$work && git remote -v
    echo -e "${bold}---------------------------------------------------------------------------- ${end}"
    echo ""
    echo "Enter the ID for server => '$server' (default = origin)"
    echo -e "$Bgre"
    read -p "[ID> " origin
    echo -e "$end"
    echo -e "${gre}Define server ID to '$origin' ... [done]${end}"
    echo ""

    #origin
    echo -e "${gre}Config origin ... [done] ${end}"
    sleep 0.5
    cd ~/Projects/$work && git remote add $origin $server

    #checking
    cd ~/Projects/$work && git remote -v
    echo -e "${gre}Checking origin ... [done] ${end}"
    sleep 1
    echo -e "${Bgre}\nAll remote config ... [done] ${end}"
    sleep 1.5
    allDone
    ;;

  1)
    clone
    ;;

  2)
    config
    ;;

  3)
    #create projects directory
    mkdir -p ~/Projects
    echo -e "\n${gre}Generate '~/Projects' directory ... [done] ${end}"
    echo -e "\n"

    #project name
    echo -e "${bold}\nNo space on project name ... ${end}"
    echo -e "${Bgre}"
    read -p "[PROJET> " projectName
    echo -e "${end}"
    cd ~/Projects/ && mkdir -p $projectName
    echo -e "Generate project '$projectName' directory ... [done] ${end}"
    sleep 1
    create
    ;;

  4)
    genssh
    ;;

  5)
    pubkey
    ;;

  6)
    authorized_keys
    ;;

  7)
    sshConfig
    ;;

  "s")
    status
    ;;

  "l")
    log
    ;;

  "c")
    commit
    ;;

  "m")
    merge
    ;;

  "df")
    diff
    ;;

  "cbr")
    branch
    ;;

  "dbr")
    delBranch
    ;;

  "sbr")
    switch
    ;;

  "lbr")
    listBranch
    ;;

  "push")
    push
    ;;

  "pull")
    pull
    ;;

  "update")
    upstream
    ;;

  "lorg")
    originList
    ;;

  "norg")
    originRename
    ;;

  "dorg")
    delOriginServer
    ;;

  "valid")
    validation
    ;;

  77)
    purge
    ;;

  88)
    backup
    ;;

  99)
    echo "Thank you for using gitvers-tool, see you soon!"
    break
    ;;

  "exit")
    echo "Thank you for using gitvers-tool, see you soon!"
    break
    ;;

  *)
    echo -e "${red}[invalid input]...${nc}"
    ;;
  esac

done
