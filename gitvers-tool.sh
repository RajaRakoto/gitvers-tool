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
  echo -e "\n${cya}[config-status-global]"
  echo -e "---------------------------------------------------------------- ${end}"
  git config --list
  echo -e "${cya}---------------------------------------------------------------- ${end}"
}

function listProj() {
  echo -e "${gre}Projects list: ${end}"
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
  sleep 0.35

  #name
  echo -e "\nEnter your name"
  echo -e "${Bgre}"
  read -p "[NAME> " newName
  echo -e "${end}"
  git config --global user.name $newName
  echo -e "${gre}Name configured ... [done] ${end}"
  sleep 0.35

  #branch
  echo -e "\nEnter main branch (default = main)"
  echo -e "${Bgre}"
  read -p "[BRANCH> " defaultBranch
  echo -e "${end}"
  git config --global init.defaultBranch $defaultBranch
  echo -e "${gre}Initial branch name is '$defaultBranch' now ... [done] ${end}"
  sleep 0.35

  #color syntax
  git config --global color.ui true
  echo -e "\n${gre}Color syntax activated ... [done] ${end}"
  sleep 0.35

  #rebase
  git config --global branch.autosetuprebase always
  echo -e "\n${gre}Rebase all pull (request) ... [done] ${end}"
  sleep 0.35

  #check config
  gitConfigShow
  allDone
}

function preConf() {

  #local config
  cd ~/Projects/$projectName && git init
  echo -e "${gre}Git init ... [done] ${end}"
  echo -e "${gre}Generate .git ... [done] ${end}"
  sleep 0.2

  #gitignore
  cd ~/Projects/$projectName && touch .gitignore
  echo -e "${gre}Generate .gitignore ... [done] ${end}"
  sleep 0.2

  #config .gitignore
  echo 'tmp' >~/Projects/$projectName/.gitignore && echo 'backups' >>~/Projects/$projectName/.gitignore && echo 'node_modules' >>~/Projects/$projectName/.gitignore && echo '.gitignore' >>~/Projects/$projectName/.gitignore
  echo -e "${gre}.gitignore configured ... [done] ${end}"
  sleep 0.2

  #tmp
  cd ~/Projects/$projectName && mkdir -p tmp
  echo -e "${gre}Generate tmp folder ... [done] ${end}"
  sleep 0.2
}

function create() {

  #project generator + config
  echo -e "${Bcya} \n>>> GIT PROJECT GENERATOR <<<\n ${end}"
  sleep 0.3

  echo -e "${cya}Generate project '$projectName' directory ... [done] ${end}"

  #preconf
  preConf
  allDone
}

function genssh() {
  echo "Enter your email address, SSH will use the address as a label for the key..."
  echo -e "${Bgre}"
  read -p "[EMAIL> " tag
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
  sleep 0.35
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
----------------------------------------------------------------------------------------------------------------${end}
1. Ensure that the source/target machine is accessible (ping <ipv4 source/target>)
2. Check that ssh (openssh-client|openssh-server) is installed on each machine by typing the command 'ssh'
3. Check in the field below that the 'bck' folder has been created, otherwise manually create a backup of the ssh configuration i-e '/etc/ssh'
"
  ls /etc/ssh
  echo -e "
4. Uncomment 'Port 22' in 'ssh_config'
5. Uncomment 'Port 22', 'PubkeyAuthentication yes' and 'PermitRootLogin no' in 'sshd_config'
${cya}------------------------------------------------------------------------------------------------------------------------------${end}
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
  read -p "Removing '$purge' git project, press [ENTER] to continue..." temp
  echo -e "${end}"
  cd ~/Projects/$purge && git reset --hard && git clean -dffx && cd .. && rm -rf $purge
  echo -e "${gre}Removing $purge ... [done]${end}"
  sleep 0.35
  allDone
}

function backup() {
  echo -e "${mag}"
  read -p "Press [ENTER] to start backup process, [CTRL+C] to cancel..." temp
  echo -e "${end}"
  #delete old backup
  echo -e "${gre}Delete old backups file (if exist) ... [Loading] ${end}"
  sleep 1
  cd ~/Projects/ && rm -rf git-projects-backups.tar.gz
  #compression
  echo -e "${gre}Compression all git projects ... [Loading] ${end}"
  sleep 1
  cd ~/Projects/ && tar cvfz git-projects-backups.tar.gz *
  echo -e "${Bgre}All git projects backuped ... [done] ${end}"
  sleep 1
  allDone
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

function commit() {
  #commit model
  echo -e "${cya}[COMMIT model]"
  echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n${end}"
  echo -e "[add]: message => ${Igry}add file(s)${end}"
  echo -e "[del]: message => ${Igry}delete file(s)${end}"
  echo -e "[fix]: message => ${Igry}bug fix${end}"
  echo -e "[feat]:message => ${Igry}adding feature${end}"
  echo -e "[docs]: message => ${Igry}documentation update${end}"
  echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n${end}"

  status0

  #commit core
  echo -e "\n"
  branchShow
  echo -e "${bold}\nAdd name of file to index (* to add all)${end}"
  echo -e "${Bgre}"
  read -p "[ADD> " index
  echo -e "${end}"
  cd ~/Projects/$work && git add $index
  sleep 0.35

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
  mainBranchInput
  cd ~/Projects/$work && git checkout $mainBranch
  echo -e "${gre}Switch to branch $mainBranch ... [done]${end}"
  sleep 0.35
  echo ""
  git branch
  echo -e "\nEnter branch name to merge into $mainBranch"
  echo -e "${Bgre}"
  read -p "[MERGE> " merge
  echo -e "${end}"
  cd ~/Projects/$work && git merge $merge
  echo -e "${gre}Merge to branch $mainBranch ... [done]${end}"
  sleep 0.35
  allDone
}

function branch() {
  echo -e "\nEnter name of the branch to create"
  echo -e "${Bgre}"
  read -p "[BRANCH> " branch
  echo -e "${end}"
  cd ~/Projects/$work && git branch $branch
  echo -e "${gre}Create new branch '$branch' ... [done]${end}"
  sleep 0.35
  allDone
}

function delBranch() {
  cd ~/Projects/$work && git branch -a
  echo -e "\nEnter name of branch to delete"
  echo -e "${Bgre}"
  read -p "[DEL> " branch
  echo -e "${end}"
  mainBranchInput
  cd ~/Projects/$work && git checkout $mainBranch && git branch -d $branch
  echo -e "${gre}Removing '$branch' branch ... [done]${end}"
  sleep 0.35
  allDone
}

function delRemoteBranch() {
  cd ~/Projects/$work && git branch -a
  echo -e "\nEnter name of remote branch to delete"
  echo -e "${Bgre}"
  read -p "[DEL> " remoteBranch
  echo -e "${end}"
  cd ~/Projects/$work && git push origin --delete $remoteBranch
  echo -e "${gre}Removing '$branch' remote branch ... [done]${end}"
  sleep 0.35
  allDone
}

function delIdServer() {
  #list remote branch
  cd ~/Projects/$work && git remote
  echo -e "\nEnter name of the server to delete"
  echo -e "${Bgre}"
  read -p "[DEL> " server
  echo -e "${end}"
  cd ~/Projects/$work && git remote remove $server
  echo -e "${gre}Server '$server' deleted ... [done]${end}"
  sleep 0.35
  serverIdList
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
  sleep 0.35
  allDone
}

function listBranch() {
  echo -e "${cya}[all branch list]"
  echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
  cd ~/Projects/$work && git branch -a
  echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
  allDone
}

function mainBranchInput() {
  echo -e "\nEnter your main branch name (default = main)"
  echo -e "${Bgre}"
  read -p "[MAIN> " mainBranch
  echo -e "${end}"
}

function push() {
  #push syntax
  echo -e "${cya}[PUSH syntax]"
  echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
  echo -e "<server-id> <branch> =>${Igry} send data to the server named <server-id> \nof branch <branch> of the repository attached to <server>${end}"
  echo -e "${cya}current server:${end} $server"
  echo -e "${cya}current server-id:${end} $origin"
  echo -e "${cya}current branch:${end} $branch"
  echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n${end}"

  echo -e "${Bgre}"
  read -p "[PUSH> " push
  echo -e "${end}"

  cd ~/Projects/$work && git push $push

  allDone
}

function pull() {
  #pull syntax
  echo -e "${cya}[PULL syntax]"
  echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${end}"
  echo -e "<server-id> <branch> =>${Igry} receive data from <branch> remote branch \nof the repository attached to <server>${end}"
  echo -e "${cya}current server:${end} $server"
  echo -e "${cya}current server-id:${end} $origin"
  echo -e "${cya}current branch:${end} $branch"
  echo -e "${cya}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n${end}"

  echo -e "${Bgre}"
  read -p "[PULL> " pull
  echo -e "${end}"

  cd ~/Projects/$work && git pull $pull

  allDone
}

function upstream() {
  echo ""
  echo -e "Enter URL (SSH) of original repository ... \nExample: git@github.com:RajaRakoto/gitvers-tool.git"
  echo ""
  echo -e "${bold}\n[SERVER LIST (used)]--------------------------------------${end}"
  tail -n 5 ~/Projects/.originalRepo.log
  echo -e "\n${bold}----------------------------------------------------------${end}"
  echo -e "${Bgre}"
  read -p "[URL> " originalRepo
  echo -e "${end}"
  echo "[original repo]-> $originalRepo" >>~/Projects/.originalRepo.log
  echo ""
  user=$(whoami)
  echo -e "Enter fork repository URL (SSH) ... \nExample: git@github.com:$user/gitvers-tool.git"
  echo ""
  echo -e "${bold}\n[SERVER LIST (used)]--------------------------------------${end}"
  tail -n 5 ~/Projects/.forkedRepo.log
  echo -e "\n${bold}----------------------------------------------------------${end}"
  echo -e "${Bgre}"
  read -p "[URL> " forkedRepo
  echo -e "${end}"
  echo "[forked repo]-> $forkedRepo" >>~/Projects/.forkedRepo.log

  function verify() {
    cd ~/Projects/$work && git remote -v
  }

  #verification remote branch
  verify
  echo -e "${gre}Verify remote branch ... [done]${end}"
  sleep 0.35

  #add upstream original url
  cd ~/Projects/$work && git remote add upstream $originalRepo
  sleep 0.35

  #verify upstream branch
  verify
  echo -e "${gre}Verify upstream branch ... [done]${end}"
  sleep 0.35

  #fetch upstream
  cd ~/Projects/$work && git fetch upstream
  echo -e "${gre}Fetch upstream ... [done]${end}"
  sleep 0.35s

  #set main branch
  mainBranchInput

  #merge changes from upstream/<mainBranch>
  cd ~/Projects/$work && git merge upstream/$mainBranch
  echo -e "${gre}Merge upstream/$mainBranch ... [done]${end}"
  sleep 0.35s

  #push changes to update your fork main branch on server
  cd ~/Projects/$work && git push $forkedRepo $mainBranch
  echo -e "${gre}Push changes to update your fork $mainBranch on server ... [done]${end}"
  sleep 0.35s

  allDone
}

function serverIdList() {
  echo -e "${bold}\n[ORIGIN LIST (used)]-------------------------------------- ${end}"
  cd ~/Projects/$work && git remote -v
  echo -e "${bold}---------------------------------------------------------- ${end}"

  allDone
}

function serverIdList0() {
  echo -e "${bold}\n[ORIGIN LIST (used)]-------------------------------------- ${end}"
  cd ~/Projects/$work && git remote -v
  echo -e "${bold}---------------------------------------------------------- ${end}"
}

function serverIdRename() {
  serverIdList0
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

  serverIdList0

  allDone
}

function validation() {
  echo -e "${Bcya}\n >>> VALIDATION <<<${end}"
  sleep 0.5

  mainBranchInput

  #first pull
  echo ""
  cd ~/Projects/$work && git pull $origin $mainBranch

  #create README.md
  cd ~/Projects/$work && touch README.md

  #status & add & commit & push
  echo ""
  cd ~/Projects/$work && git add *

  echo ""
  cd ~/Projects/$work && git status

  echo ""
  cd ~/Projects/$work && git commit -m '1st commit'

  echo ""
  cd ~/Projects/$work && git push $origin $mainBranch
  echo -e "${gre}VALIDATION (1st commit) ... [done]${end}"
  sleep 1

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

#create working files
mkdir -p ~/Projects
cd ~/Projects && touch .server.log .originalRepo.log .forkedRepo.log

while [ true ]; do
  echo -e "\n"
  echo -e "${Bred}                     GITVERS-TOOL${end}"
  sleep 1
  echo "========================================================="
  echo -e "${yel}Version: 2.0.0"
  #sleep 0.5
  echo -e "Author: Raja"
  #sleep 0.5
  git --version
  #sleep 0.5
  echo -e "${red}------------[PROJECTS]-----------${end}"
  #sleep 0.5
  listProj
  echo -e "${red}-------------[INIT]--------------${end}"
  #sleep 0.5
  echo -e "${mag}<START>${end}"
  echo -e "${blu}work.${end} Working on a git project"
  echo -e "${blu}clone.${end} Clone git project"
  echo -e "${blu}config.${end} Configure your git profile"
  echo -e "${blu}create.${end} Create git project"
  echo -e "${mag}<SSH>${end}"
  echo -e "${blu}sshgen.${end} Generate SSH key"
  echo -e "${blu}myssh.${end} Show your public key"
  echo -e "${blu}sshauth.${end} Add your SSH key to another computer"
  echo -e "${blu}sshconf.${end} SSH config"
  echo -e "${blu}${red}-------------[GIT]---------------${end}"
  #sleep 0.5
  echo -e "${mag}<BASICS>${end}"
  echo -e "${blu}c.${end} Git commit ${gry}[commit your changes]${end}"
  echo -e "${blu}l.${end} Git log ${gry}[view your project history]${end}"
  echo -e "${blu}s.${end} Git status ${gry}[see your project status]${end}"
  echo -e "${blu}merge.${end} Git merge ${gry}[merge to main branch]${end}"
  echo -e "${blu}diff.${end} Git diff ${gry}[difference between 2 file states]${end}"
  echo -e "${mag}<BRANCH>${end}"
  echo -e "${blu}cbr.${end} Create branch ${gry}[create new branch]${end}"
  echo -e "${blu}dbr.${end} Delete local branch ${gry}[delete local branch]${end}"
  echo -e "${blu}drbr.${end} Delete remote branch ${gry}[delete remote branch]${end}"
  echo -e "${blu}sbr.${end} Switch branch ${gry}[move to another branch]${end}"
  echo -e "${blu}lbr.${end} List branch ${gry}[list all existing branches]${end}"
  echo -e "${mag}<REMOTE>${end}"
  echo -e "${blu}push.${end} Send data ${gry}[send your data to remote repository]${end}"
  echo -e "${blu}pull.${end} Receive data ${gry}[receive data from remote repository]${end}"
  echo -e "${blu}update.${end} Fast forward ${gry}[update local and remote repository]${end}"
  echo -e "${mag}<SERVER>${end}"
  echo -e "${blu}lserv.${end} List server-id ${gry}[list server id of current repository]${end}"
  echo -e "${blu}nserv.${end} Rename server-id ${gry}[rename server id of current repository]${end}"
  echo -e "${blu}dserv.${end} Delete server-id ${gry}[delete server id of current repository]${end}"
  echo -e "${mag}<VALIDATION>${end}"
  echo -e "${blu}valid.${end} Valid new git project ${gry}[validate newly created git project]${end}"
  echo -e "${red}------------[OTHERS]-------------${end}"
  #sleep 0.5
  echo -e "${blu}purge.${end} Purge ${gry}[delete git project cleanly]${end}"
  echo -e "${blu}bck.${end} Backup ${gry}[create a backup of your git projects]${end}"
  echo -e "${blu}exit.${end} EXIT"
  echo "========================================================="
  if [ $work = "n/a" ]; then
    echo -e "${yel}[STATUS] =>${end} work: $work ${yel}|${end} branch: $branch ${yel}|${end} server-id: $origin \n${yel}[SERVER] =>${end} $server"
  else
    branch=$(cd ~/Projects/$work && git branch | grep -i '*')
    echo -e "${yel}[STATUS] =>${end} work: $work ${yel}|${end} branch: $branch ${yel}|${end} server-id: $origin \n${yel}[SERVER] =>${end} $server"
  fi

  echo -e "${Bgre}"
  read -p "[INPUT> " input
  echo -e "${end}"

  case $input in

  "work")
    echo "Enter your project name..."
    echo -e "${Bgre}"
    read -p "[PROJECT> " work
    echo -e "${end}"

    function serverList() {
      echo -e "${bold}\n[SERVER LIST (used)]--------------------------------------${end}"
      tail -n 5 ~/Projects/.server.log
      echo -e "${Igry}\nNOTE: Enter 'clear' to clear the saved server list ${end}"
      echo -e "${bold}----------------------------------------------------------${end}"
    }

    serverList

    function serverInput() {
      echo -e "\nEnter git repository URL (SSH)..."
      echo "Example: git@github.com:RajaRakoto/gitvers-tool.git"
      echo -e "${Bgre}"
      read -p "[REPO> " server
      echo -e "${end}"
    }

    serverInput

    #server log
    echo "[repository]-> $server" >>~/Projects/.server.log

    #cleaning server log
    if [ $server = "clear" ] || [ $server = "CLEAR" ]; then
      echo -e "\n"
      echo "" >~/Projects/.server.log
      echo -e "${gre}All repository list cleared ... [done] ${end}"
      sleep 0.5
      serverList

      serverInput
    fi

    #def origin
    echo ""
    echo "Enter the ID for server => '$server' (default = origin)"
    echo -e "$Bgre"
    read -p "[ID> " origin
    echo -e "$end"
    echo ""

    #origin
    cd ~/Projects/$work && git remote add $origin $server

    #checking
    cd ~/Projects/$work && git remote -v
    echo -e "${gre}Config & checking origin ... [done] ${end}"
    sleep 1
    allDone
    ;;

  "clone")
    clone
    ;;

  "config")
    config
    ;;

  "create")
    #create projects directory
    mkdir -p ~/Projects

    #project name
    echo -e "${bold}\nNo space on project name ... ${end}"
    echo -e "${Bgre}"
    read -p "[PROJET> " projectName
    echo -e "${end}"
    cd ~/Projects/ && mkdir -p $projectName
    sleep 1
    create
    ;;

  "sshgen")
    genssh
    ;;

  "myssh")
    pubkey
    ;;

  "sshauth")
    authorized_keys
    ;;

  "sshconf")
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

  "merge")
    merge
    ;;

  "diff")
    diff
    ;;

  "cbr")
    branch
    ;;

  "dbr")
    delBranch
    ;;

  "drbr")
    delRemoteBranch
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

  "lserv")
    serverIdList
    ;;

  "nserv")
    serverIdRename
    ;;

  "dserv")
    delIdServer
    ;;

  "valid")
    validation
    ;;

  "purge")
    purge
    ;;

  "bck")
    backup
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
