#! /usr/bin/env python2
# coding: utf-8



#dev index
   # ... //test = non-functional code in development phase (-essential)
   # ... //test * = non-functional code in development phase (+essential)
   # ... //del = code to be deleted (later) if no use
   # ... //bug = code bug to fix
   # ... //OK = code without error
   # ... //upt = sometimes a manual of the script (Update with each modification)



#GIT versioning tools v1.1
#author: Raja



#module
import os 
import sys
import time



global choice_ON



#class //color style use on print
class style:
  RED = '\033[91m' 
  DARKCYAN = '\033[36m' 
  PURPLE = '\033[95m' 
  GREEN = '\033[92m' 
  YELLOW = '\033[93m' 
  BOLD = '\033[1m'
  END = '\033[0m'



#=============================FONCTIONS-begin=========================
#title //OK
def title():
 print(style.RED)
 time.sleep(0.05)
 print("                                          /                   ")   
 time.sleep(0.05)
 print("                                       ///////                ") 
 time.sleep(0.05)
 print("                                    /////////////             ") 
 time.sleep(0.05)
 print("                                  /////////////////           ") 
 time.sleep(0.05)
 print("                               /////////     /////////        ") 
 time.sleep(0.05)
 print("                             ///////////     ///////////      ") 
 time.sleep(0.05)
 print("                          ///////////////   ///////////////   ") 
 time.sleep(0.05)
 print("                        /////////////////   /////    //////// ") 
 time.sleep(0.05)
 print("                      ///////////////////   ////      ////////") 
 time.sleep(0.05)
 print("                        /////////////////   //*     ///////// ") 
 time.sleep(0.05)
 print("                          ///////////////      ///////////.   ") 
 time.sleep(0.05)
 print("                             ///////////     .//////////      ") 
 time.sleep(0.05)
 print("                                ////////      ////////.        ") 
 time.sleep(0.05)
 print("                                  //*   ///////////           ") 
 time.sleep(0.05)
 print("                                     ///////////.             ") 
 time.sleep(0.05)
 print("                                       ///////                ") 
 time.sleep(0.05)
 print("                                          /                   ") 
 time.sleep(0.05)
 time.sleep(0.05)
 os.system("echo '──────────────────────╔╗─────────────────────────────╔╗──────╔╗────────────────────────────'")
 time.sleep(0.05)
 os.system("echo '─────────────────────╔╝╚╗───────────────────────────╔╝╚╗─────║║────────────────────────────'")
 time.sleep(0.05)
 os.system("echo '──────────────────╔══╬╗╔╝─╔╗╔╦══╦═╦══╦╦══╦═╗╔╦═╗╔══╗╚╗╔╬══╦══╣║╔══╗────────────────────────'")
 time.sleep(0.05)
 os.system("echo '──────────────────║╔╗╠╣║──║╚╝║║═╣╔╣══╬╣╔╗║╔╗╬╣╔╗╣╔╗║─║║║╔╗║╔╗║║║══╣────────────────────────'")
 time.sleep(0.05)
 os.system("echo '──────────────────║╚╝║║╚╗─╚╗╔╣║═╣║╠══║║╚╝║║║║║║║║╚╝║─║╚╣╚╝║╚╝║╚╬══║────────────────────────'")
 time.sleep(0.05)
 os.system("echo '──────────────────╚═╗╠╩═╝──╚╝╚══╩╝╚══╩╩══╩╝╚╩╩╝╚╩═╗║─╚═╩══╩══╩═╩══╝────────────────────────'")
 time.sleep(0.05)
 os.system("echo '──────────────────╔═╝║──────────────────────────╔═╝║      version 1.1'")
 time.sleep(0.05)
 os.system("echo '──────────────────╚══╝──────────────────────────╚══╝'")
 time.sleep(0.05)
 time.sleep(0.05)

 print(style.END)

#restart //OK
def restart():
  os.execl(sys.executable, sys.executable, *sys.argv)

#shell //OK
def shell():
  #shell note
    print(" \n ")
    print(style.BOLD+"[shell usage]======================================================="+style.END)
    print("* The shell mode is a way to quickly access your basic shell if you don't have TILIX as a terminal in order to better manage your project, as well as this script.")
    print(" \n ")
    print("* The shell mode does not yet work online by line, you must execute all the commands simultaneously using the boolean operator '&&', remember to check your input commands before executing it")
    print(" \n ")
    print("* The shell mode focus on your active repository, i.e. in '~/Project/{0}'".format(zen))
    print(" \n ")
    print("  PS: "+style.END+"'q' to exit shell input"+style.END)
    print(style.BOLD+"====================================================================="+style.END)
    print(" \n ")

    #shell input
    print("'q' to exit shell input")
    shell = raw_input(style.BOLD+"[🆂🅷🅴🅻🅻 > "+style.END)
    os.system("cd ~/Project/{0} && {1}".format(zen,shell))
    print(" \n ")

    #loopback
    while (shell != 'q' or shell != 'Q'):
      print("'q' to exit shell input")
      shell = raw_input(style.BOLD+"[🆂🅷🅴🅻🅻 > "+style.END)
      os.system("cd ~/Project/{0} && {1}".format(zen,shell))
      print(" \n ")
      if shell == 'q' or shell == 'Q':
        break

    done()
    choiceMenu()

#localProject //OK
def localProject():
  os.system("cd ~/Project/{0} && pwd".format(zen))

#helpssh //OK
def helpsshFR():
  print(" \n\n ")
  print(style.YELLOW+style.BOLD+"                             [SSH manual page]"+style.END)
  print("======================================================================================")
  print(" \n ")
  print(style.BOLD+style.PURPLE+"SSH:"+style.END+" un protocole permettant d'établir une communication cryptée, donc sécurisée (on parle parfois de tunnel), sur un réseau informatique (intranet ou Internet) entre une machine locale (le client) et une machine distante (le serveur).\n\n")

  os.system("cat ./docs/ssh-service-fr")

  print(" \n ")
  print("======================================================================================")

  print(" \n ")
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#helpssh //OK
def helpssh():
  print(" \n\n ")
  print(style.YELLOW+style.BOLD+"                             [SSH manual page]"+style.END)
  print("======================================================================================")
  print(" \n ")
  print(style.BOLD+style.PURPLE+"SSH:"+style.END+" a protocol making it possible to establish encrypted communication, therefore secure (we sometimes speak of a tunnel), on a computer network (intranet or Internet) between a local machine (the client) and a remote machine (the server).\n\n")

  os.system("cat ./docs/ssh-service")

  print(" \n ")
  print("======================================================================================")

  print(" \n ")
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#installssh //OK
def installssh():
  print(" \n ")
  print(style.GREEN+"openssh-server installation ... [loading]"+style.END)
  os.system("sudo apt-get update && apt-get install openssh-server")
  print(style.GREEN+"openssh-server installation ... [done]"+style.END)
  time.sleep(0.35)
  print(" \n ")
  print(style.GREEN+"openssh-client installation ... [loading]"+style.END)
  os.system("sudo apt-get install openssh-client")
  print(style.GREEN+"openssh-client installation ... [done]"+style.END)
  time.sleep(0.35)
  print(" \n ")
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#genssh //OK
def genssh():
  print(" \n ")
  print(style.BOLD+"Enter your name, ssh will use your name as the label of the generated ssh key ... "+style.END)
  tag = raw_input(style.BOLD+"[🆃🅰🅶 > "+style.END)
  os.system("ssh-keygen -t rsa -b 4096 -C '{0}' | tee log_ssh-keygen && mv log_ssh-keygen ~/.ssh".format(tag))
  print(style.GREEN+"Generate ssh-key (private|public) ... [done]"+style.END)
  time.sleep(0.35)
  print(style.GREEN+"log_ssh-keygen ... [done]"+style.END)
  time.sleep(0.35)
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#bckssh //OK
def bckssh():
  print(" \n ")
  os.system("sudo mkdir -p /etc/ssh/bck && cd /etc/ssh/ && cp -r ssh_config sshd_config bck/")
  print(style.GREEN+"All ssh config backuped in /etc/ssh/bck ... [done]"+style.END)
  time.sleep(0.35)
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#ssh_config //OK
def ssh_config():
  print(" \n ")
  os.system("sudo nano /etc/ssh/ssh_config")
  print(style.GREEN+"ssh_config edited... [done]"+style.END)
  time.sleep(0.35)
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#sshd_config //OK
def sshd_config():
  print(" \n ")
  os.system("sudo nano /etc/ssh/sshd_config")
  print(style.GREEN+"sshd_config edited ... [done]"+style.END)
  time.sleep(0.35)
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#issue_net //OK
def issue_net():
  print(" \n ")
  os.system("sudo nano /etc/issue.net")
  print(style.GREEN+"issue.net edited ... [done]"+style.END)
  time.sleep(0.35)
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#ssh_service //OK
def ssh_service():
  print(" \n ")
  os.system("sudo systemctl restart ssh")
  print(style.GREEN+"restart ssh ... [done]"+style.END)
  time.sleep(0.35)
  os.system("sudo systemctl restart sshd.service")
  print(style.GREEN+"restart sshd.service ... [done]"+style.END)
  time.sleep(0.35)
  os.system("sudo systemctl restart ssh.service")
  print(style.GREEN+"restart ssh.service ... [done]"+style.END)
  time.sleep(0.35)
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#ssh_agent_pid //OK
def ssh_agent_pid():
  print(" \n ")
  os.system("eval '$(ssh-agent -s)'")
  print(style.GREEN+"show ssh-agent pid ... [done]"+style.END)
  time.sleep(0.35)
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#ssh_agent //OK
def ssh_agent():
  print(" \n ")
  print(style.BOLD+"Enter the full path of the location of your private ssh key (with its name) ... (it should be displayed below if you haven't changed the location)"+style.END)
  print("Ex: /home/user/.ssh/id_rsa")
  os.system("cd ~/.ssh/ && ls && pwd")
  path = raw_input(style.BOLD+"[🅿🅰🆃🅷 > "+style.END)
  os.system("ssh add {0}".format(path))
  print(style.GREEN+"add ssh-key (private) to ssh-agemt ... [done]"+style.END)
  time.sleep(0.35)
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#ufw //OK
def ufw():
  print(" \n ")
  os.system("sudo ufw allow ssh")
  print(style.GREEN+"allow ssh in ufw ... [done]"+style.END)
  time.sleep(0.35)
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#pubkey //OK
def pubkey():
  print(" \n ")
  os.system("cat ~/.ssh/id_rsa.pub")
  print(" \n ")
  print(style.GREEN+"show public key ... [done]"+style.END)
  time.sleep(0.35)
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the SSH menu ..."+style.END)
  ssh()

#authorized_keys() //OK
def authorized_keys():
  print(" \n ")
  print("Enter the name of the remote machine (ex: raja@192.168.8.100) ...")
  server = raw_input(style.BOLD+"[COMPUTER > "+style.END)
  os.system("ssh-copy-id {0}".format(server))
  print(style.GREEN+"authorized_keys ... [done]"+style.END)
  time.sleep(0.35)
  ssh()

#ssh //OK
def ssh():
  print("\n")
  print(style.BOLD+"          ++++++++++++++++++++ SSH menu +++++++++++++++++++")
  print("          ================================================="+style.END)
  print("     1"+style.BOLD+" <> "+style.END+"install openssh-server $ openssh-client")
  print("     2"+style.BOLD+" <> "+style.END+"generate ssh-key (private|public)")
  print("     3"+style.BOLD+" <> "+style.END+"backup all ssh config")
  print("     4"+style.BOLD+" <> "+style.END+"edit ssh_config")
  print("     5"+style.BOLD+" <> "+style.END+"edit sshd_config")
  print("     6"+style.BOLD+" <> "+style.END+"edit issue.net")
  print("     7"+style.BOLD+" <> "+style.END+"restart all ssh service")
  print("     8"+style.BOLD+" <> "+style.END+"verify ssh-agent pid")
  print("     9"+style.BOLD+" <> "+style.END+"add ssh-key (private) to ssh-agent")
  print("    10"+style.BOLD+" <> "+style.END+"allow ssh in ufw (firewall)")
  print("    11"+style.BOLD+" <> "+style.END+"show my public key")
  print("    12"+style.BOLD+" <> "+style.END+"authorized_keys")
  print("    13"+style.BOLD+" <> "+style.END+"help ssh (fr)")
  print(style.BOLD+"          =================================================")
  print("          +++++++++++++++++++++++++++++++++++++++++++++++++"+style.END)
  
  print("\n")
  ssh = raw_input(style.BOLD+"[🆂🆂🅷 > "+style.END)

  if ssh == '1':
    installssh()

  if ssh == '2':
    genssh()

  if ssh == "3":
    bckssh()

  if ssh == "4":
    ssh_config()

  if ssh == "5":
    sshd_config()

  if ssh == "6":
    issue_net()
   
  if ssh == "7":
    ssh_service()

  if ssh == "8":
    ssh_agent_pid()

  if ssh == "9":
    ssh_agent()

  if ssh == "10":
    ufw()

  if ssh == "11":
    pubkey()

  if ssh == '12':
    authorized_keys()

  if ssh == '13' or ssh == 'help' or ssh == 'HELP':
    helpssh()

  if ssh == '13fr' or ssh == 'helpfr' or ssh == 'HELPfr':
    helpsshFR()

  done()
  choiceMain()

#installTilix //OK
def installTilix():
  print(" \n ")
  print(style.GREEN+"TILIX install ... [loading]"+style.END)
  os.system("sudo apt-get update && apt-get install tilix")
  print(style.GREEN+"TILIX install ... [done]"+style.END)
  time.sleep(0.35)
  print(" \n ")
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the menu of TILIX ..."+style.END)
  tilix()

#tilix //OK
def tilix():
  print("\n")
  print(style.BOLD+"          /\/\/\/\/\/\/\/\/\ TILIX menu /\/\/\/\/\/\/\/\/\/")
  print("          ================================================="+style.END)
  print("     1"+style.BOLD+" <> "+style.END+"install Tilix (super-terminal)")  
  print(style.BOLD+"          =================================================")
  print("          \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/"+style.END)
  
  print("\n")
  tilix = raw_input(style.BOLD+"[🆃🅸🅻🅸🆇 > "+style.END)

  if tilix == '1':
    installTilix()

  done()
  choiceMain()

#installungit //OK
def installungit():
  print(style.GREEN+"UNGIT install ... [loading]"+style.END)
  os.system("sudo -H npm install -g ungit")
  print(style.GREEN+"UNGIT install ... [done]"+style.END)
  time.sleep(0.35)
  print(" \n ")
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the menu of UNGIT ...")
  ungit()

#installNodeNpm //OK
def installNodeNpm():
  print(style.GREEN+"Node.JS and NPM install ... [loading]"+style.END)
  os.system("sudo apt-get update && apt-get install npm")
  print(style.GREEN+"Node.JS and NPM install ... [done]"+style.END)
  time.sleep(0.35)
  print(" \n ")
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the menu of UNGIT ...")
  ungit()

#helpungit //OK
def helpungit():
  print(" \n\n ")
  print(style.YELLOW+style.BOLD+"                         [UNGIT manual page]"+style.END)
  print("======================================================================================")
  print ("\n")
  print (style.BOLD + style.PURPLE + "UNGIT:" + style.END + " web-based interface that aims to control a git repository, the latter brings usability to git without sacrificing its versatility. \n \n" )

  print (style.YELLOW + "STEP 1:" + style.END + " install the pre-requisites Node.JS [> = 10.18.0] and NPM [> = 6.13.4]")
  print (style.YELLOW + "     >" + style.END + " manual command (sh): sudo apt-get update && apt-get install npm")
  print ("\n")
  print (style.YELLOW + "STEP 2:" + style.END + " install UNGIT from the NPM package manager")
  print (style.YELLOW + "     >" + style.END + " manual command (sh): sudo -H npm install -g ungit")
  print ("\n")
  print (style.YELLOW + "STEP 3:" + style.END + " use the 'ungit' command to launch UNGIT")
  print (style.YELLOW + "     >" + style.END + " once UNGIT is launched, paste this http: // localhost: 8448 / # / in your browser to display the home page of UNGIT")
  print ("\n")
  print (style.YELLOW + "STEP 4:" + style.END + " copy and paste your 'working directory' (the absolute path of your repository) at the very beginning of the page (in the search bar) UNGIT")
  print (style.YELLOW + "     >" + style.END + " manual command (sh): pwd (you must go to the repository before typing this cmd)")
  print (style.YELLOW + "     >" + style.END + " tip: you can see the absolute path of your repository by entering the local menu | remote of this script (at the top)")
  print ("\n")
  print (style.YELLOW + "STEP 5:" + style.END + " you can now use the entire UNGIT function, use with care because your action on UNGIT will affect your entire repository")

  print ("\n")
  print (style.GREEN + "REPOSITORY (ungit): https://github.com/FredrikNoren/ungit"+style.END)

  print ("\n")
  print("======================================================================================")

  print(" \n ")
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the menu of UNGIT ...")
  ungit()

#ungit //OK
def ungit():
  print("\n")
  print(style.YELLOW+"          /\/\/\/\/\/\/\/\/\ UNGIT menu /\/\/\/\/\/\/\/\/\/")
  print("          ================================================="+style.END)
  print("     1"+style.YELLOW+" <> "+style.END+"install Node.JS [>= 10.18.0] et NPM [>= 6.13.4]")  
  print("     2"+style.YELLOW+" <> "+style.END+"install UNGIT")  
  print("     3"+style.YELLOW+" <> "+style.END+"help UNGIT")
  print(style.YELLOW+"          =================================================")
  print("          \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/"+style.END)
  
  print("\n")
  ungit = raw_input(style.YELLOW+"[🆄🅽🅶🅸🆃 > "+style.END)

  if ungit == '1':
    installNodeNpm()
  
  if ungit == '2':
    installungit()
  
  if ungit == '3' or ungit == 'help' or ungit == 'HELP' or ungit == 'h' or ungit == 'H':
    helpungit()
  
  done()
  choiceMain()

#installflow //test*
def installflow():
  print(" \n ")
  print(style.GREEN+"git flow install ... [loading]"+style.END)
  os.system("sudo apt-get update && apt-get install git-flow")
  print(style.GREEN+"git flow install ... [done]"+style.END)
  time.sleep(0.35)
  print(" \n ")
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the menu of GITflow ...")
  flow()

#helpflow //test*
def helpflow():
  print(" \n ")
  print(style.GREEN+"git flow help ... [loading]"+style.END)
  time.sleep(0.5)
  #decompress gitflow.info.tar.gz
  os.system("cd docs && tar xvf gitflow.info.tar.gz")
  print(style.GREEN+"gitflow.info decompressing ... [done]"+style.END)
  time.sleep(0.35)
  #read index.html in default browser
  print(style.GREEN+"reading index.html of gitflow.info ... [loading]"+style.END)
  time.sleep(1)
  os.system("cd docs/ && gnome-www-browser gitflow.info/index.html")
  print(" \n ")
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the menu of GITflow ...")
  #free up memory
  os.system("cd docs && rm -rf gitflow.info")
  print(style.GREEN+"clean cache gitflow.info ... [done]"+style.END)
  time.sleep(0.35)
  flow()

#flow //test*
def flow():
  print("\n")
  print(style.YELLOW+"          * * * * * * *  GITflow menu * * * * * *"+style.END)
  print("     1"+style.YELLOW+" +> "+style.END+"install GITflow     ")  
  print("     2"+style.YELLOW+" +> "+style.END+"help GITflow          ")
  print(style.YELLOW+"          * * * * * * * * * * * * * * * * * * * * ")
  
  print("\n")
  flow = raw_input(style.YELLOW+"[🅵🅻🅾🆆 > "+style.END)

  if flow == '1':
    installflow()
  
  if flow == '2':
    helpflow()
  
  done()
  choiceMain()

#manual //OK
def manual():
  print(style.GREEN+style.BOLD+"                                [git manual page (official)]"+style.END)
  print("===============================================================================================")
  print(" \n ")
  os.system("git --help")
  print(" \n ")
  print("===============================================================================================")

#serviceDE //OK
def serviceFR():
  print(" \n\n ")
  print(style.YELLOW+style.BOLD+"                           [Services tiers de Github & Bitbucket]"+style.END)
  print("==========================================================================================================================================")
  print(" \n ")
  os.system("cat ./docs/git-service-fr")
  print(" \n ")
  print("==========================================================================================================================================")

  print(" \n ")
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the main menu ..."+style.END)
  
  done()
  choiceMain()

#service //OK
def service():
  print(" \n\n ")
  print(style.YELLOW+style.BOLD+"                           [Github & Bitbucket third-party services]"+style.END)
  print("==========================================================================================================================================")
  print(" \n ")
  os.system("cat ./docs/git-service")
  print(" \n ")
  print("==========================================================================================================================================")

  print(" \n ")
  temp = raw_input(style.DARKCYAN+"Press [ENTER] to return to the main menu ..."+style.END)
  
  done()
  choiceMain()

#keywordsFR //OK
def keywordsFR():
  print(style.BOLD+style.GREEN+" Keywords :"+style.END)
  print(style.BOLD+"all|*"+style.END+" = tous les fichiers & repertoires")
  print(style.BOLD+"*.extension"+style.END+" = tous les fichiers of type .extension (ex: *.py)")
  print(style.BOLD+style.DARKCYAN+"\nIl existe 2 façon pour acceder aux fonctiions of ce script, soit un acces basique (du menu) par un numero, soit un acces rapide via un mot-cle"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT CONFIG ~"+style.END)
  print("0 | config : "+style.GREEN+"git config (menu)"+style.END)
  print("configlob : "+style.GREEN+"afficher la configuration global of git"+style.END)
  print("configmail : "+style.GREEN+"définit l'email que vous voulez associer à toutes vos opérations of commit"+style.END)
  print("configname : "+style.GREEN+"définit le nom que vous voulez associer à toutes vos opérations of commit"+style.END)
  print("configrebase : "+style.GREEN+"permet d'avoir un historique propre lors d'un pull request"+style.END)
  print("configquick : "+style.GREEN+"configurer rapidement votre profil git"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT ADD & REMOVE ~"+style.END)
  print("1 | + | add : "+style.GREEN+"ajoute un instantané du fichier, en préparation pour le suivi of version"+style.END)
 #================
  print(" \n ")
  print("2 | - | del : "+style.GREEN+"supprime le fichier du système of suivi of version mais le préserve localement"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT IGNORE ~"+style.END)
  print("3 : "+style.GREEN+"git ignore (menu)"+style.END)
  print("ignore | temp : "+style.GREEN+"ignorer (of git) rapidement un/plusieurs element(s)"+style.END)
  print("reignore | retemp : "+style.GREEN+"reignorer (of temp) rapidement un/plusieurs element(s)"+style.END)
  print("eignore | etemp : "+style.GREEN+"editer rapidement le fichier .gitignore"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT LOG ~"+style.END)
  print("4 : "+style.GREEN+"git log (menu)"+style.END)
  print("l | log : "+style.GREEN+"montre l'historique des versions pour la branche courante avec ID simplifiE des commits"+style.END)
  print("h | history : "+style.GREEN+"montre l'historique des versions pour la branche courante avec ID complet des commits"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT DIFF ~"+style.END)
  print("5 | df | diff : "+style.GREEN+"montre les différences of contenu entre deux element(s) (l'un commitE et l'autre en cours of modification)"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT CHECKOUT ~"+style.END)
  print("6 | check | checkout : "+style.GREEN+"remettre un element a l'etat specifiE grace a son ID commit (revenir en arriere)"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT REVERT ~"+style.END)
  print("7 | rev | revert : "+style.GREEN+"defaire un commit a partir of son id en creant un nouveau commit (ne permet pas of revenir en arriere comme git checkout)"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT RESET ~"+style.END)
  print("8 | res | reset : "+style.GREEN+"enleve le fichier of l'index, mais conserve son contenu, autrement dit, réinitialiser la HEAD courante à l'état spécifié"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT STASH ~"+style.END)
  print("9 | stash : "+style.GREEN+"git stash (menu)"+style.END)
  print("stash exec : "+style.GREEN+"enregistre of manière temporaire tous les fichiers sous suivi of version qui ont été modifiés 'remiser son travail'"+style.END)
  print("stash list : "+style.GREEN+"lister toutes les remises gardE (en memoire)"+style.END)
  print("stash apply : "+style.GREEN+"reappliquer un remise (avec l'ID stash)"+style.END)
  print("stash drop : "+style.GREEN+"supprimer un remise (avec l'ID stash)"+style.END)
  print("stash diff : "+style.GREEN+"difference of contenu d'un remise (avec l'ID stash)"+style.END)
  print("stash branch : "+style.GREEN+"switcher d'une branch en copiant les remises gardE (en memoire)"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT BRANCH & SWITCH ~"+style.END)
  print("10 | branch : "+style.GREEN+"git branch (menu)"+style.END)
  print("br | new : "+style.GREEN+"creer une nouvelle branche locale"+style.END)
  print("lbr : "+style.GREEN+"lister toutes les branches locales dans le dépôt courant"+style.END)
  print("rm br : "+style.GREEN+"supprimer une branche local"+style.END)
  print("11 | mbr | merge : "+style.GREEN+"combine dans la branche courante l'historique of la branche spécifiée"+style.END)
  print("12 | sbr | switch : "+style.GREEN+"bascule sur la branche spécifiée et met à jour le répertoire of travail"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ WORKFLOWS ~"+style.END)
  print("13 : "+style.GREEN+"git branch (remote - menu)"+style.END)
  print("rbr | rnew : "+style.GREEN+"creer une nouvelle branche distant"+style.END)
  print("rlbr : "+style.GREEN+"lister toutes les branches distantes dans le dépôt courant"+style.END)
  print("rm br : "+style.GREEN+"supprimer une branche distante"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ ORIGIN ~"+style.END)
  print("14 | org : "+style.GREEN+"origin (menu)"+style.END)
  print("org rename : "+style.GREEN+"renommer l'ID origin"+style.END)
  print("org list : "+style.GREEN+"lister l'ID origin"+style.END)
 #================
  print(" \n ")
  print(style.RED+style.BOLD+"~ PUSH & PULL (request) ~"+style.END)
  print("15 | push : "+style.GREEN+"push (send request) - envoie tous les commits of la branche locale vers un serveur (SSHserver, plateforme git)"+style.END)
  print("16 | pull : "+style.GREEN+"pull (receive request) - récupère tout l'historique du dépôt nommé et incorpore les modifications"+style.END)
 #================
  print(" \n ")
  print(style.RED+style.BOLD+"~ OTHER ~"+style.END)
  print("a : "+style.GREEN+"check project (menu)"+style.END)
  print("b | sh | shell : "+style.GREEN+"acceder au shell"+style.END)
 #================
  print(" \n ")
  print(style.YELLOW+style.BOLD+"~ COMMIT ~"+style.END)
  print("c | com | commit : "+style.GREEN+"enregistre des instantanés of fichiers of façon permanente dans l'historique des versions"+style.END)

#keywords //upt
def keywords():
  print (style.BOLD + style.GREEN + "Keywords:" + style.END)
  print (style.BOLD + "all|*" + style.END + " = all files & directories")
  print (style.BOLD + "*.extension" + style.END + " = all files of type .extension (ex: *.py)")
  print (style.BOLD + style.DARKCYAN + "\nThere are 2 ways to access the functions of this script, either a basic access (from the menu) by a number, or a quick access via a keyword" + style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT CONFIG ~"+style.END)
  print("0 | config : "+style.GREEN+"git config (menu)"+style.END)
  print ("configlob : " + style.GREEN + "display global of git configuration" + style.END)
  print ("configmail : " + style.GREEN + "defines the email you want to associate with all your commit operations" + style.END)
  print ("configname : " + style.GREEN + "defines the name you want to associate with all your commit operations" + style.END)
  print ("configrebase : " + style.GREEN + "allows to have a clean history during a pull request" + style.END)
  print ("configquick : " + style.GREEN + "quickly configure your git profile" + style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT ADD & REMOVE ~"+style.END)
  print("1 | + | add : "+style.GREEN+"add a snapshot of the file, in preparation for version tracking"+style.END)
 #================
  print(" \n ")
  print("2 | - | del : "+style.GREEN+"remove the file from the version tracking system but keep it locally"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT IGNORE ~"+style.END)
  print("3 : "+style.GREEN+"git ignore (menu)"+style.END)
  print ("ignore | temp :" + style.GREEN + "quickly ignore (of git) one/more element(s)" + style.END)
  print ("reignore | retemp :" + style.GREEN + "reignore (of temp) quickly one/more element(s)" + style.END)
  print ("eignore | etemp :" + style.GREEN + "quickly edit the .gitignore file" + style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT LOG ~"+style.END)
  print("4 : "+style.GREEN+"git log (menu)"+style.END)
  print ("l | log :" + style.GREEN + "shows the version history for the current branch with simplified ID of commits" + style.END)
  print ("h | history :" + style.GREEN + "shows the version history for the current branch with full ID of commits" + style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT DIFF ~"+style.END)
  print("5 | df | diff : "+style.GREEN+"show the differences of content between two element(s) (one commited and the other being modified)"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT CHECKOUT ~"+style.END)
  print("6 | check | checkout : "+style.GREEN+"reset an element to the specified state thanks to its commit ID (go back)"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT REVERT ~"+style.END)
  print("7 | rev | revert : "+style.GREEN+"make a commit from its id by creating a new commit (does not allow to go back like git checkout)"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT RESET ~"+style.END)
  print("8 | res | reset : "+style.GREEN+"remove the file from the index, but keep its contents, in other words, reset the current HEAD to the specified state"+style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT STASH ~"+style.END)
  print("9 | stash : "+style.GREEN+"git stash (menu)"+style.END)
  print ("stash exec : " + style.GREEN + "temporarily saves all files under version tracking that have been modified 'put your work back'" + style.END)
  print ("stash list : " + style.GREEN + "list all stash list (in memory)" + style.END)
  print ("stash apply : " + style.GREEN + "reapply a discount (with stash id)" + style.END)
  print ("stash drop : " + style.GREEN + "remove a drop (with stash id)" + style.END)
  print ("stash diff : " + style.GREEN + "difference of content of a discount (with stash id)" + style.END)
  print ("stash branch : " + style.GREEN + "switch from a branch by copying the guard discounts (in memory)" + style.END)
 #================
  print(" \n ")
  print(style.RED+"~ GIT BRANCH & SWITCH ~"+style.END)
  print("10 | branch : "+style.GREEN+"git branch (menu)"+style.END)
  print ("br | new : " + style.GREEN + "create a new local branch" + style.END)
  print ("lbr : " + style.GREEN + "list all local branches in the current repository" + style.END)
  print ("rm br : " + style.GREEN + "delete a local branch" + style.END)
  print ("11 | mbr | merge : " + style.GREEN + "combines in the current branch the history of the specified branch" + style.END)
  print ("12 | sbr | switch : " + style.GREEN + "switch to the specified branch and update the working directory" + style.END)
 #================
  print(" \n ")
  print(style.RED+"~ WORKFLOWS ~"+style.END)
  print("13 : "+style.GREEN+"git branch (remote - menu)"+style.END)
  print ("rbr | rnew : " + style.GREEN + "create a new remote branch" + style.END)
  print ("rlbr : " + style.GREEN + "list all remote branches in the current repository" + style.END)
  print ("rm br : " + style.GREEN + "remove remote branch" + style.END)
 #================
  print(" \n ")
  print(style.RED+"~ ORIGIN ~"+style.END)
  print("14 | org : "+style.GREEN+"origin (menu)"+style.END)
  print ("org rename : " + style.GREEN + "rename origin ID" + style.END)
  print ("org list : " + style.GREEN + "list the origin ID" + style.END)
 #================
  print(" \n ")
  print(style.RED+style.BOLD+"~ PUSH & PULL (request) ~"+style.END)
  print ("15 | push : " + style.GREEN + "push (send request) - send all commits from the local branch to a server (SSHserver, git platform)" + style.END)
  print ("16 | pull : " + style.GREEN + "pull (receive request) - get all the history of the named repository and incorporate the changes" + style.END)
 #================
  print(" \n ")
  print(style.RED+style.BOLD+"~ OTHER ~"+style.END)
  print("a : "+style.GREEN+"check project (menu)"+style.END)
  print("b | sh | shell : "+style.GREEN+"access the shell"+style.END)
 #================
  print(" \n ")
  print(style.YELLOW+style.BOLD+"~ COMMIT ~"+style.END)
  print("c | com | commit : "+style.GREEN+"save snapshots of files permanently in version history"+style.END)

#minikeywords //upt
def minikey():
  print(style.BOLD+style.GREEN+"Keywords :"+style.END)
  print(style.BOLD+"all|*"+style.END+" = all files & directories")
  print(style.BOLD+"*.extension"+style.END+" = all type files .extension (ex: *.py)")

#position //OK
def position():
  print("in "+style.GREEN+zen+style.END)

#tree //OK
def tree():
  print(style.GREEN+style.BOLD + "\n        [tree {0}]".format(zen) + style.END)
  print("========================================")
  os.system("tree ~/Project/{0}".format(zen))
  print(style.BOLD + "\n[file hided]" + style.END)
  os.system("ls -a ~/Project/{0}".format(zen))
  print("========================================")

  choiceMenu()

#touch //OK
def touch():
  print(" \n ")
  position()
  i = input(style.PURPLE+"How many files to create ? >> "+style.END)
  choice_ON = raw_input(style.PURPLE+"\nAuto add extensions ? (Y/N) >> "+style.END)
 
  while choice_ON != 'Y' and choice_ON != 'N' and choice_ON != 'y' and choice_ON != 'n':
    choice_ON = raw_input(style.PURPLE+"Your choice is invalid, try again ! (Y/N) >> "+style.END)
  
  if choice_ON == 'Y' or choice_ON == 'y': 
    print("___________________list.extension___________________")
    print(style.YELLOW+"Bourne Again Shell (bash)"+style.END+"| .sh")
    print(style.YELLOW+"C"+style.END+"| .c")
    print(style.YELLOW+"C#"+style.END+"| .csharp")
    print(style.YELLOW+"C++"+style.END+"| .cpp")
    print(style.YELLOW+"HTML"+style.END+"| .html")  
    print(style.YELLOW+"CSS"+style.END+"| .css")
    print(style.YELLOW+"Json"+style.END+"| .json")
    print(style.YELLOW+"INI"+style.END+"| .ini")
    print(style.YELLOW+"Dart"+style.END+"| .dart")
    print(style.YELLOW+"Python"+style.END+"| .py")
    print(style.YELLOW+"PHP"+style.END+"| .php")
    print(style.YELLOW+"Perl"+style.END+"| .perl")
    print(style.YELLOW+"Java"+style.END+"| .java")
    print(style.YELLOW+"JavaScript"+style.END+"| .js")  
    print(style.YELLOW+"Vue"+style.END+"| .vue")
    print(style.YELLOW+"Lua"+style.END+"| .lua")
    print(style.YELLOW+"Ruby"+style.END+"| .ruby")
    print(style.YELLOW+"SQL"+style.END+"| .sql")
    print(style.YELLOW+"XML"+style.END+"| .xml")
    print(style.YELLOW+"VisualBasic"+style.END+"| .vb")
    print(style.YELLOW+"Swift"+style.END+"| .swift")
    print(style.YELLOW+"GO"+style.END+"| .go")
    print("___________________________________________________\n")
    branchShow()
    extension = raw_input(style.GREEN+"[🅴🆇🆃🅴🅽🆂🅸🅾🅽 > "+style.END)
    done()

  if choice_ON == 'N' or choice_ON == 'n':
    print(style.GREEN+"Auto extension canceled ... [done]"+ style.END)
    time.sleep(0.35)

  for i in range(i): 

   if choice_ON == 'Y' or choice_ON == 'y':
     branchShow()
     inTouch = raw_input(style.GREEN + "\n[🅽🅰🅼🅴 > ".format(extension) + style.END)
     os.system("touch ~/Project/{0}/'{1}{2}'".format(zen,inTouch,extension))
     print(style.GREEN+"Touch {0}{1} ... [done]".format(inTouch,extension)+style.END)
     time.sleep(0.35)
  
   if choice_ON == 'N' or choice_ON == 'n':
     branchShow()
     inTouch = raw_input(style.GREEN + "\n[🅽🅰🅼🅴 > " + style.END)
     os.system("touch ~/Project/{0}/'{1}'".format(zen,inTouch))
     print(style.GREEN+"Touch {0} ... [done]".format(inTouch)+style.END)
     time.sleep(0.35)

  done()
  choiceMenu()

#remove //OK
def remove():
 position()
 os.system("tree ~/Project/{0}".format(zen))
  
 minikey()
 
 branchShow()
 rm = raw_input(style.RED+style.BOLD+"\n[🅳🅴🅻 > "+style.END)
 
 choice_ON = raw_input(style.RED+"Are you sure to delete ? (Y/N) >> "+style.END)
 while choice_ON != 'Y' and choice_ON != 'N' and choice_ON != 'y' and choice_ON != 'n':
   choice_ON = raw_input(style.PURPLE+"Your choice is invalid, try again! (Y/N) >> "+style.END)
 
 if choice_ON == 'Y' or choice_ON == 'y': 
   if rm == "*" or rm == "all":
     temp = raw_input(style.RED+"You are in the process of deleting everything (CTRL+C) to cancel, (ENTER) to continue the operation"+style.END)
     os.system("cd ~/Project/{0} && rm -r *".format(zen))  
     print(style.RED+"all files|directory deleted ... [done]"+style.END)
     time.sleep(0.35)
   else:
     os.system("cd ~/Project/{0} && rm -r {1}".format(zen,rm))
     print(style.RED+"{0} deleted ... [done]".format(rm))
     time.sleep(0.35) 

 if choice_ON == 'N' or choice_ON == 'n':
   print("Operation canceled !")

 done()
 choiceMenu()

#choiceMenu //OK
def choiceMenu():
  print("\n")
  temp = raw_input(style.DARKCYAN+style.BOLD+"press [ENTER] to return menu, [q] to exit ... "+style.END)
  print("\n")

  if temp == 'q' or temp == 'quit' or temp == 'Q' or temp == 'QUIT' or temp == 'exit' or temp == 'EXIT':
    exit0()
  else:
    menu()

#choice0 //OK
def choiceMain():
  print("\n")
  temp = raw_input(style.DARKCYAN+style.BOLD+"press [ENTER] to return main, [q] to exit ... "+style.END)
  print("\n")

  if temp == 'q' or temp == 'quit' or temp == 'Q' or temp == 'QUIT' or temp == 'exit' or temp == 'EXIT':
    exit0()
  else:
    restart()

#exit0 //OK
def exit0():
  print("")

#exit1 //OK
def exit1():
  print(style.RED+"\n\nThanks for using this script! See you soon ;)"+style.END)

#listeprojet //OK
def listProj(): 
  print("|"+style.GREEN+" ___________________________________"+style.BOLD+"Ⓟ Ⓡ Ⓞ Ⓙ Ⓔ Ⓒ Ⓣ"+style.END+style.GREEN+" _____________________________________"+style.END)
  print("|"+style.GREEN+"*                                                                                      *"+style.END)            
  os.system("ls ~/Project")
  print("|"+style.GREEN+"*______________________________________________________________________________________*"+style.END)

#done //OK
def done():
   print(style.BOLD+style.DARKCYAN + "\n>>> DONE <<<" + style.END)

#installGit //OK
def installGit():
  os.system("sudo apt-get update && sudo apt-get install git")
  done()
  choiceMain()

#gitclone //OK
def gitclone():

  print(" \n ")
  print(style.DARKCYAN+style.BOLD+"[clone usage]======================================================="+style.END)
  print(style.DARKCYAN+"LINK_ORIGIN (original repository to clone) ="+style.END+" repo-git (github, gitlabs, bitbucket), ssh-server, directory (absolute path)"+style.END)
  print(style.DARKCYAN+"LINK_TARGET (name of the clone repository) ="+style.END+" this is optional if you want to keep the default name of the original repository to be cloned"+style.END)
  print(" \n ")
  print(style.DARKCYAN+"* cas1:"+style.END+" clone a repository (online)")
  print("   [clone> LINK_ORIGIN")
  print("   (ex): https://github.com/FredrikNoren/ungit (clone the ungit of github repository)\n")

  print("   [clone> LINK_ORIGIN LINK_TARGET")
  print("   (ex): https://github.com/FredrikNoren/ungit ungit_modified (clone the ungit of github repository then change its name)")
            
  print(" \n ")
  print(style.DARKCYAN+"* cas2:"+style.END+" clone a repository (locally/online) then change its name")
  print("   [clone> LINK_ORIGIN LINK_TARGET")
  print("   (ex): /home/raja/my_study_project mon_study_projet_copy (clone a local repository to ~/Project)")
  
  print(" \n ")
  print(style.DARKCYAN+"PS: "+style.END+"All cloned repositories (online/locally) are in ~/Project/ as long as you use this script")
  print(style.DARKCYAN+style.BOLD+"===================================================================="+style.END)
  print(" \n ")
  
  print(style.BOLD+"Enter LINK_ORIGIN | LINK_TARGET"+style.END)
  link = raw_input(style.GREEN+style.BOLD+"[🅲🅻🅾🅽🅴 > "+style.END) 
  os.system("cd ~/Project/ && git clone {0}".format(link))

  done()
  choiceMain()

#gitconfig //OK
def configlob():
    print(style.DARKCYAN +"\n[config-status-global]--------------------" + style.END)
    os.system("git config --list")
    print(style.DARKCYAN +"------------------------------------------" + style.END)
    choiceMenu()

#configmail //OK
def configmail():
  print(" \n ")
  print(style.BOLD+"Please enter a valid email address :)"+style.END)
  branchShow()
  newMail = raw_input(style.GREEN + style.BOLD +"[🅽🅴🆆-🅼🅰🅸🅻 > " + style.END)
  choiceMenu()

#configname //OK
def configname():
  print(" \n ")
  print(style.BOLD+"Please enter a name :)"+style.END)
  branchShow()
  newName = raw_input(style.GREEN + style.BOLD +"[🅽🅴🆆-🅽🅰🅼🅴 > " + style.END)
  choiceMenu()

#initBranch //OK
def initBranch():
  print(" \n ")
  print(style.BOLD+"Please enter the name of the initial branch to use [default = master] :)"+style.END)
  branchShow()
  init = raw_input(style.GREEN + style.BOLD +"[🅸🅽🅸🆃-🅱🆁🅰🅽🅲🅷 > " + style.END)
  os.system("git config --global init.defaultBranch {0}".format(init))
  print(style.GREEN+"init branch name is {0} now ... [done]".format(init)+style.END)
  time.sleep(0.35)
  choiceMenu()

#rebase //OK
def rebase():
  print(" \n ")
  os.system("git config --global branch.autosetuprebase always".format(zen))
  print(style.GREEN+"rebase all pull (request) ... [done]"+style.END)
  time.sleep(0.35)
  choiceMenu()

#configquick //OK
def configquick():
  print(" \n ")
  print(style.BOLD+"Please enter a valid email address :)"+style.END)
  branchShow()
  newMail = raw_input(style.GREEN + style.BOLD +"[🅽🅴🆆-🅼🅰🅸🅻 > " + style.END)
  os.system("git config --global user.email '{0}'".format(newMail)) 
  print(style.GREEN+"Creation new e-mail ... [done]"+ style.END)
  time.sleep(0.35)

  print(" \n ")
  print(style.BOLD+"Please enter a name :)"+style.END)
  branchShow()
  newName = raw_input(style.GREEN + style.BOLD +"[🅽🅴🆆-🅽🅰🅼🅴 > " + style.END)
  os.system("git config --global user.name '{0}'".format(newName))
  print(style.GREEN+"Creation new name ... [done]"+ style.END) 
  time.sleep(0.35)

  print(" \n ")
  print(style.BOLD+"Please enter the name of the initial branch to use [default = master] :)"+style.END)
  branchShow()
  init = raw_input(style.GREEN + style.BOLD +"[🅸🅽🅸🆃-🅱🆁🅰🅽🅲🅷 > " + style.END)
  os.system("git config --global init.defaultBranch {0}".format(init))
  print(style.GREEN+"init branch name is {0} now ... [done]".format(init)+style.END)
  time.sleep(0.35)

  print(" \n ")
  os.system("git config --global color.ui true")
  print(style.GREEN+"Color syntax activated ... [done]"+ style.END)
  time.sleep(0.35)
  
  print(" \n ")
  os.system("git config --global branch.autosetuprebase always")
  print(style.GREEN+"rebase all pull (request) ... [done]"+style.END)
  time.sleep(0.35)

  print(" \n ")
  print(style.DARKCYAN +"\n[config-status-global]--------------------" + style.END)
  os.system("git config --list")
  print(style.DARKCYAN +"------------------------------------------" + style.END)
  done()
  choiceMenu()

#configquick0 //OK
def configquick0():
  print(" \n ")
  print(style.BOLD+"Please enter a valid email address :)"+style.END)
  newMail = raw_input(style.GREEN + style.BOLD +"[🅽🅴🆆-🅼🅰🅸🅻 > " + style.END)
  os.system("git config --global user.email '{0}'".format(newMail)) 
  print(style.GREEN+"Creation new e-mail ... [done]"+ style.END)
  time.sleep(0.35)

  print(" \n ")
  print(style.BOLD+"Please enter a name :)"+style.END)
  newName = raw_input(style.GREEN + style.BOLD +"[🅽🅴🆆-🅽🅰🅼🅴 > " + style.END)
  os.system("git config --global user.name '{0}'".format(newName))
  print(style.GREEN+"Creation new name ... [done]"+ style.END) 
  time.sleep(0.35)

  print(" \n ")
  print(style.BOLD+"Please enter the name of the initial branch to use [default = master] :)"+style.END)
  init = raw_input(style.GREEN + style.BOLD +"[🅸🅽🅸🆃-🅱🆁🅰🅽🅲🅷 > " + style.END)
  os.system("git config --global init.defaultBranch {0}".format(init))
  print(style.GREEN+"init branch name is {0} now ... [done]".format(init)+style.END)
  time.sleep(0.35)

  print(" \n ")
  os.system("git config --global color.ui true")
  print(style.GREEN+"Color syntax activated ... [done]"+ style.END)
  time.sleep(0.35)

  print(" \n ")
  os.system("git config --global branch.autosetuprebase always")
  print(style.GREEN+"rebase all pull (request) ... [done]"+style.END)
  time.sleep(0.35)

  print(" \n ")
  print(style.DARKCYAN +"\n[config-status-global]--------------------" + style.END)
  os.system("git config --list")
  print(style.DARKCYAN +"------------------------------------------" + style.END)
  done()
  choiceMain()

#gitconfig (menu) //OK
def gitConfig():
  print("\n*************************")
  print(style.DARKCYAN + "0" + style.END + " - config status")
  print(style.DARKCYAN + "1" + style.END + " - config e-mail")
  print(style.DARKCYAN + "2" + style.END + " - config name")
  print(style.DARKCYAN + "3" + style.END + " - config colorsyntax")
  print(style.DARKCYAN + "4" + style.END + " - config init branch (name)")
  print(style.DARKCYAN + "5" + style.END + " - rebase all pull (request)")
  print(style.DARKCYAN + "6" + style.END + " - quick config")
  print("*************************")

  branchShow()
  inPut = raw_input(style.GREEN + style.BOLD+"[🅲🅾🅽🅵🅸🅶 > " + style.END)

  if inPut == '0':
    configlob()
   
  if inPut == '1':
    configmail()

  if inPut == '2':
    configname()

  if inPut == '3':
    print("\n***********")
    print(style.DARKCYAN + "0" + style.END + " - enable syntax highlighting (coloration)")
    print(style.DARKCYAN + "1" + style.END + " - turn off syntax highlighting (coloration)")
    print("***********")


    branchShow()
    syntaxColoration = raw_input(style.GREEN + style.BOLD+"\n[🅲🅾🅻🅾🆁 > " + style.END)
    
    if syntaxColoration == '0':
      os.system("git config --global color.ui true")
      #other option 
      # git config --global color.diff auto
      # git config --global color.status auto
      # git config --global color.branch auto
      print(style.GREEN+"Color syntax activated ... [done]"+style.END)
      time.sleep(0.35)

    if syntaxColoration == '1':
      os.system("git config --global color.ui false")
      print(style.GREEN+"Color syntax disabled ... [done]"+style.END)
      time.sleep(0.35)

  if inPut == '4':
    initBranch()

  if inPut == '5':
    rebase()

  if inPut == '6':
    configquick()

  done()
  choiceMenu()

#backup //OK
def backup():
  print("\n")
  temp = raw_input(style.PURPLE+"Press [ENTER] to start saving, [CTRL + C] to cancel ... "+style.END)
  print(" \n ")
  time.sleep(0.02)
  print("╔╗───────╔╗")
  time.sleep(0.02)
  print("║║───────║║")
  time.sleep(0.02)
  print("║╚═╦══╦══╣║╔╦╗╔╦══╗")
  time.sleep(0.02)
  print("║╔╗║╔╗║╔═╣╚╝╣║║║╔╗║")
  time.sleep(0.02)
  print("║╚╝║╔╗║╚═╣╔╗╣╚╝║╚╝║")
  time.sleep(0.02)
  print("╚══╩╝╚╩══╩╝╚╩══╣╔═╝")
  time.sleep(0.02)
  print("───────────────║║")
  time.sleep(0.02)
  print("───────────────╚╝")
  time.sleep(0.02)
  print("\n")
  print(style.GREEN+"All project/server backup ... [Loading]"+style.END)
  time.sleep(2)
  print("\n")
  #delete if old backup exist
  print(style.GREEN+"Deletion old backup (if exist) ... [Loading]"+style.END)
  time.sleep(1)
  os.system("cd ~/Project/ && rm -rf ALL-PROJECT-SERVER-BACKUP.tar.gz")
  #compress all project
  print(style.GREEN+"Compression all project ... [Loading]"+style.END)
  time.sleep(1)
  os.system("cd ~/Project/ && tar cvfz ALL-PROJECT-SERVER-BACKUP.tar.gz *")
  print("\n")
  time.sleep(2)
  print(style.GREEN+"All project/server backup ... [done]"+style.END)
  time.sleep(1)
  print("\n")
  print(style.BOLD+"Now put 'ALL-PROJECT-SERVER-BACKUP.tar.gz' in a safe and secure location ..."+style.END)
  print("[Tips]: Create your own order (alias) to be able to backup faster - https://alvinalexander.com/blog/post/linux-unix/create-aliases/")

  done()
  choiceMain()

#gitstatus //OK
def gitstatus():

  print(style.BOLD + style.GREEN +"\n          [status {0}]".format(zen) + style.END)
  print("======================================")
  os.system("cd $HOME/Project/{0} && git status".format(zen))
  print("======================================")

  choiceMenu()

#gitstatus0 //OK
def gitstatus0():

  print(style.BOLD + style.GREEN +"\n          [status {0}]".format(zen) + style.END)
  print("======================================")
  os.system("cd $HOME/Project/{0} && git status".format(zen))
  print("======================================")

#checkprojet (menu) //OK
def checkProj():

  print("\n**********")
  print(style.DARKCYAN + "0" + style.END + " - git status")
  print(style.DARKCYAN + "1" + style.END + " - tree")
  print("**********")

  branchShow()
  inPut = raw_input(style.GREEN + style.BOLD + "[🅶🅸🆃 > " +  style.END)


  if inPut == '0':
    gitstatus()
  
  if inPut == '1':
    tree()

  done()
  choiceMenu()

#readme (menu) //OK
def readme():
  print(style.BOLD+"Vous voulez editer avec :"+style.END)
  print("\n**********")
  print(style.DARKCYAN + "0" + style.END + " - nano")
  print(style.DARKCYAN + "1" + style.END + " - sublimetext")
  print("**********")

  branchShow()
  inPut = raw_input(style.GREEN + style.BOLD + "[🅶🅸🆃 > " +  style.END)

  if inPut == '0':
    os.system("cd ~/Project/{0}/ && nano README.md".format(zen))
  if inPut == '1':
    os.system("cd ~/Project/{0}/ && subl README.md".format(zen))
  
  choiceMenu()

#noteFR //OK
def noteFR():
  print(style.BOLD + "\n              [GIT-NOTE]" + style.END)
  print("========================================")
  print("~ "+style.DARKCYAN+"Pas d'espace"+style.END+" sur le nom of projet")
  print("~ Deplacez vos fichiers dans "+style.DARKCYAN+"'tmp'"+style.END+" pour etre ignorer of git")
  print("~ Editer le fichier "+style.DARKCYAN+"'README.md'"+style.END+" pour ajouter des infos a propos of votre projet\n")
  keywordsFR()
  print("========================================")
  
  if mainPut == "notefr" or mainPut == 'NOTEFR' or mainPut == "nfr" or mainPut == 'NFR':
    choiceMain()

#note //OK
def note():
  print(style.BOLD + "\n              [GIT-NOTE]" + style.END)
  print("========================================")
  print("~ "+style.DARKCYAN+"No space"+style.END+" on the name of the project")
  print("~ Move your files to "+style.DARKCYAN+"'tmp'"+style.END+" to be ignored of git")
  print("~ Edit file "+style.DARKCYAN+"'README.md'"+style.END+" to add info about your project\n")
  keywords()
  print("========================================")
  
  if mainPut == "note" or mainPut == 'NOTE' or mainPut == "n" or mainPut == 'N':
    choiceMain()

#note1 //OK
def note1FR():
  noteFR()
  choiceMenu()

#note1 //OK
def note1():
  note()
  choiceMenu()

#tree0 //OK
def tree0() :
  print(style.GREEN+style.BOLD + "\n         [tree {0}]".format(zen) + style.END)
  print("========================================")
  os.system("tree ~/Project/{0}".format(zen))
  print(style.BOLD + "\n[file hided]" + style.END)
  os.system("ls -a ~/Project/{0}".format(zen))
  print("========================================")

#gitadd (menu) //OK
def gitadd(): 
 
 print("\n_____________gitadd-note______________")
 print("1. Basic use: enter the name of a file + extension "+ style.RED +" (in red) "+ style.END +" to put it in the zone of transit")
 print("2. Multiple addition: "+style.YELLOW+"*.extension (ex: *.html | *.js | *.py)"+style.END)
 print("3. Addition of all files in the zone of transit: "+style.YELLOW+"ALL"+style.END)
 print("______________________________________")
 gitstatus0()

 branchShow()
 gitadd = raw_input(style.GREEN+style.BOLD+"[🅰🅳🅳 > " + style.END)
 
 if gitadd != "ALL" and gitadd != "all":
   os.system("cd ~/Project/{0} && git add {1}".format(zen,gitadd))
   gitstatus0()
   print(style.GREEN+"Addition of {0} in the zone of transit ... [done]".format(gitadd)+style.END)
   time.sleep(0.35)

 if gitadd == "ALL" or gitadd == "all":
   os.system("cd ~/Project/{0} && git add --all".format(zen))
   gitstatus0()
   print(style.GREEN+"Addition of all files in the zone of transit ... [done]".format(gitadd)+style.END)
   time.sleep(0.35)

 print(" \n ")
 choice_ON = raw_input(style.GREEN+"[🅲 🅾 🅼 🅼 🅸 🆃 ](Y/N) >> "+style.END)
 
 
 while choice_ON != 'Y' and choice_ON != 'N' and choice_ON != 'y' and choice_ON != 'n':
   print(style.PURPLE+"Your choice is invalid, try again! (Y / N)"+style.END)
   choice_ON = raw_input(style.GREEN + "\n[🅲 🅾 🅼 🅼 🅸 🆃 ](Y/N) >> " + style.END)
   

 if choice_ON == 'Y' or choice_ON == 'y': 
   gitCommit()
   print(style.GREEN+"Commit file ... [done]"+ style.END)
   time.sleep(0.35)
   
 if choice_ON == 'N' or choice_ON == 'n':
   print(style.GREEN+"Commit canceled ... [done]"+ style.END) 
   time.sleep(0.35)
 gitstatus0()
 done() 
 choiceMenu() 
 
#gitremove //OK
def gitremove(): 

 print("\n___________gitremove-note____________")
 print("1. Basic use: enter the name of a file "+ style.GREEN +" (in green) "+ style.END +" to deindex it from the zone of transit")
 print("_____________________________________")
 gitstatus0()

 branchShow()
 gitrm = raw_input(style.RED +style.BOLD+ "\n[🆁🅴🅼🅾🆅🅴 > " + style.END) 
 
 os.system("cd ~/Project/{0} && git rm --cached {1}".format(zen,gitrm))
 print(style.GREEN+"Desindexation '{0}' in the zone of transit ... [done]".format(gitrm)+style.END)
 time.sleep(0.35)
 
 gitstatus0()
 done()
 choiceMenu()

#gitcommit //OK
def gitCommit():
 
 print("\n____________gitcommit-note____________")
 print("1. Basic use: comment out the file (s) "+ style.GREEN +" (in green) "+style.END)
 print("2. it is always recommended to commit a meaningful committal to your changes "+style.END)
 print(style.BOLD+"--all|*"+style.END+" = all files & directories")
 print("______________________________________") 
 
 print(" \n ")
 
 #commit model
 os.system("cat ./docs/commit-model") 

 print(" \n ")
 
 #git status
 gitstatus0()
 
 #commit core
 print(style.BOLD+"Enter the name of the file(s) to track"+style.END)
 branchShow()
 temp = raw_input(style.GREEN + style.BOLD +"\n[🅰🅳🅳 > " + style.END) 
 os.system("cd ~/Project/{0} && git add {1}".format(zen,temp))
 print(style.GREEN+"exec git add {0} ... [done]".format(zen)+style.END)
 time.sleep(0.35)
 
 gitstatus0()

 branchShow()
 gitcom = raw_input(style.GREEN + style.BOLD +"\n[🅼🅴🆂🆂🅰🅶🅴 > " + style.END) 
 
 os.system("cd ~/Project/{0} && git commit -m '{1}'".format(zen,gitcom))
 print(style.GREEN+"Update: {0} ... [done]".format(gitcom)+style.END)
 time.sleep(0.35)
 
 gitstatus0()
 done()
 choiceMenu()

#gitignore_list //OK
def gitignoreList():

  print("\n___________gitignore-note___________")
  print("1. Basic usage: enter the filename | directory to ignore of git\n")
  minikey()
  print("____________________________________")  
  tree0()

  print(" \n ")
  print(style.BOLD+"Enter file/directory to ignore (from git)"+style.END)
  branchShow()
  gitign = raw_input(style.GREEN + style.BOLD + "[🅸🅶🅽🅾🆁🅴 > " + style.END) 

  if gitign == "ALL" or gitign == "all" or gitign == "*":
    gitign = "*"
    os.system("cd ~/Project/{0} && mv {1} tmp".format(zen,gitign))
    print(style.GREEN+"Moving {0} to tmp ... [done]".format(gitign)+style.END)
    time.sleep(0.35)
    os.system("cd ~/Project/{0}/tmp/ && mv README.md ..".format(zen))
    print(style.GREEN+"Removing README.md to {0} ... [done]".format(zen)+style.END)
    time.sleep(0.35)
   
  if gitign != "ALL" and gitign != "all" and gitign != "*":  
    os.system("cd ~/Project/{0} && mv {1} tmp".format(zen,gitign))
    print(style.GREEN+"Moving {0} to tmp ... [done]".format(gitign)+style.END)
    time.sleep(0.35)
 
  tree()
  done()
  choiceMenu()

#gitignoreEdit //OK
def gitignoreEdit():
  os.system("cd ~/Project/{0} && nano .gitignore".format(zen))
  print(style.GREEN+"Editing .gitignore ... [done]"+style.END)
  time.sleep(0.35)
  choiceMenu()

#gitignore (menu) //OK
def gitignore():
  print("\n***************")
  print(style.DARKCYAN+"0. "+style.END+"exec gitignore")
  print(style.DARKCYAN+"1. "+style.END+"exec reignore")
  print(style.DARKCYAN+"2. "+style.END+"edit .gitignore") 
  print("***************")
  
  print(" \n ")
  branchShow()
  gitign0 = raw_input(style.GREEN + style.BOLD+"[🅸🅶🅽🅾🆁🅴 > " + style.END) 
  
  if gitign0 == '0':
    gitignoreList()
  
  if gitign0 == '1':
    reIgnore()

  if gitign0 == '2':
    gitignoreEdit()    

#gitreIgnore //OK
def reIgnore():
  print(" \n ")
  minikey()
  tree0()

  print(style.BOLD+"Enter the name of the file/directory to reignore (from tmp)"+style.END)
  branchShow()
  reignore = raw_input(style.GREEN + style.BOLD + "[🆁🅴🅸🅶🅽🅾🆁🅴 > " + style.END) 

  if reignore == '*' or reignore == 'all' or reignore == 'ALL':
    os.system("cd ~/Project/{0}/tmp && mv {1} ..".format(zen,reignore))
    print(style.GREEN+"reignore all ... [done]")
    time.sleep(0.35)

  else:
    os.system("cd ~/Project/{0}/tmp && mv {1} ..".format(zen,reignore))
    print(style.GREEN+"reignore {0} ... [done]".format(reignore))
    time.sleep(0.35)

  tree0()
  done()
  choiceMenu()

#log //OK
def log():
  print(style.BOLD+style.GREEN+"                          [log]"+style.END)
  print("==============================================================================")
  os.system("cd ~/Project/{0} && git log --graph --pretty='%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'".format(zen))
  print("==============================================================================")
  choiceMenu()

#history //OK
def history():
  print(style.BOLD+style.GREEN+"                        [history]"+style.END)
  print("==============================================================================")
  os.system("cd ~/Project/{0} && git log".format(zen))
  print("==============================================================================")
  choiceMenu()

#gitlog //OK
def gitlog():
 print("\n**************")
 print(style.DARKCYAN+"0. "+style.END+"log")
 print(style.DARKCYAN+"1. "+style.END+"history")
 print("**************\n")

 branchShow()
 gitlg = raw_input(style.GREEN + style.BOLD+"[🅻🅾🅶 > " + style.END) 
 
 if gitlg == '0':
   log()
  
 if gitlg == '1':
   history()

#gitdiff //OK
def gitdiff():
  print(style.GREEN+"[difference]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+style.END)
  os.system("cd ~/Project/{0} && git diff".format(zen))
  print(style.GREEN+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+style.END)

  done()
  choiceMenu()

#branchlist //OK
def branchlist():
  print(" \n ")
  print(style.GREEN+"[all-branch-list]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+style.END)
  os.system("cd ~/Project/{0} && git branch -a".format(zen))
  print(style.GREEN+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+style.END)

  done()
  choiceMenu()  

#branchlist0 //OK
def branchlist0():
  print(" \n ")
  print(style.GREEN+"[all-branch-list]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+style.END)
  os.system("cd ~/Project/{0} && git branch -a".format(zen))
  print(style.GREEN+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+style.END)
  done()

#gitbranch (menu) //OK
def gitbranch():
 print("\n**************")
 print(style.DARKCYAN+"0. "+style.END+"git branch")
 print(style.DARKCYAN+"1. "+style.END+"list branch")
 print(style.DARKCYAN+"2. "+style.END+"remove branch")
 print("**************\n")

 branchShow()
 gitlg = raw_input(style.GREEN + style.BOLD+ "[🅸🅽🅿🆄🆃 > " + style.END) 
 
 if gitlg == '0':
   exGitbranch()
  
 if gitlg == '1':
   branchlist()
  
 if gitlg == '2':
   branchremove()

 done()
 choiceMenu()

#exGitbranch //OK
def exGitbranch():
  print(style.BOLD+"\nPlease enter the name of the new branch"+style.END)
  
  branchShow()
  gitbrch = raw_input(style.GREEN + style.BOLD + "[🅱🆁🅰🅽🅲🅷 > " + style.END) 
  
  os.system("cd ~/Project/{0} && git branch {1}".format(zen,gitbrch))
  print(style.GREEN+"Create new branch '{0}' ... [done]".format(gitbrch))
  time.sleep(0.35)

  branchlist()
  done()
  choiceMenu()

#branchremove //OK
def branchremove():
  temp = raw_input(style.PURPLE+"Press [ENTER] to see the lists of available branches ... "+style.END)
  os.system("cd ~/Project/{0} && git branch".format(zen))

  print(style.RED+"Please enter the name of the branch to be deleted ... "+style.END)

  branchShow()
  rmbrch = raw_input(style.RED + style.BOLD + "[🅳🅴🅻 > " + style.END) 
  
  os.system("cd ~/Project/{0} && git checkout master && git branch -d {1}".format(zen,rmbrch))
  print(style.GREEN+"Delete branch '{0}' ... [done]".format(rmbrch))
  time.sleep(0.35)
  
  done()
  choiceMenu()

#branchremotelist //OK
def gitbranchRemoteList():
  print(" \n ")
  print(style.GREEN+"[remote-list]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+style.END)
  os.system("cd ~/Project/{0} && git branch -r".format(zen))
  print(style.GREEN+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+style.END)

  done()
  choiceMenu()  

#gitbranchremote (menu) //OK
def gitbranchRemoteMenu():
 print("\n**************")
 print(style.DARKCYAN+"0. "+style.END+"git branch (remote)")
 print(style.DARKCYAN+"1. "+style.END+"list branch (remote)")
 print(style.DARKCYAN+"2. "+style.END+"remove branch (remote)")
 print("**************\n")

 branchShow()
 gitlg = raw_input(style.GREEN + style.BOLD+ "[🅸🅽🅿🆄🆃 > " + style.END) 
 
 if gitlg == '0':
   exgitbranchRemoteMenu()
  
 if gitlg == '1':
   gitbranchRemoteList() 
  
 if gitlg == '2':
   gitbranchRemoteRemove()

 done()
 choiceMenu()

#exGitbranchremote (creer une nouvelle branche remote) //OK
def exgitbranchRemoteMenu():
  print(style.BOLD+"\nPlease enter the name of the new branch"+style.END)
  
  branchShow()
  rbr = raw_input(style.GREEN + style.BOLD + "[🅱🆁🅰🅽🅲🅷 > " + style.END) 
  
  #STEP1:
  print(" \n ")
  os.system("cd ~/Project/{0} && git branch {1}".format(zen,rbr))
  print(style.GREEN+"Create new branch '{0}' ... [done]".format(rbr)+style.END)
  time.sleep(0.35)

  #STEP2: 
  #git push <origin> <branch> 
  os.system("cd ~/Project/{0} && git push {1} {2}".format(zen,origin,rbr))
  print(style.GREEN+style.BOLD+"\nPushing {0} => {1} ... [done]".format(rbr,origin)+style.END)
  time.sleep(0.35)
  print(" \n ")

  gitbranchRemoteList()
  done()
  choiceMenu()

#branchremoveremote //OK
def gitbranchRemoteRemove():
  
  print(" \n ")
  temp = raw_input(style.PURPLE+"Press [ENTER] to display the lists of available branches ... "+style.END)
  os.system("cd ~/Project/{0} && git branch -a".format(zen))

  print(" \n ")

  print(style.BOLD+"Please enter the name of the remote branch to be deleted")
  rmrbr = raw_input(style.RED+style.BOLD+"[🅳🅴🅻🅴🆃🅴 > " + style.END) 
  
  print(" \n ")

  #delete remote branch
  print(style.GREEN+"Deletion of the current remote branch ... "+style.END)
  os.system("cd ~/Project/{0} && git push {1} --delete {2}".format(zen,origin,rmrbr))
  print(style.GREEN+"Delete remote branch '{0}' ... [done]".format(rmrbr))
  time.sleep(0.35)
  
  print(" \n ")
  temp = raw_input(style.PURPLE+"Press [ENTER] to verify the change ... "+style.END)
  os.system("cd ~/Project/{0} && git branch -a".format(zen))
  print(style.GREEN+"Verification ... [done]".format(rmrbr))
  time.sleep(0.35)

  done()
  choiceMenu()

#switch //OK
def switch():
  print(style.BOLD+"\nPlease enter the name of the branch"+style.END)

  branchShow()
  swi = raw_input(style.GREEN + style.BOLD + "[🆂🆆🅸🆃🅲🅷 > " + style.END)
  os.system("cd ~/Project/{0} && git checkout {1}".format(zen,swi))

  print(style.GREEN+"Switched to '{0}' branch ... [done]".format(swi))
  time.sleep(0.35)

  done()
  choiceMenu()

#switchMain //OK
def switchMain():
  # choice_ON = raw_input(style.PURPLE+"\nLISTER LES BRANCHES? (Y/N) >> "+style.END)
  # while choice_ON != 'Y' and choice_ON != 'N' and choice_ON != 'y' and choice_ON != 'n':
  #   choice_ON = raw_input(style.PURPLE+"Your choice is invalid, try again! (Y/N) >> "+style.END)
  
  # if choice_ON == 'Y' or choice_ON == 'y':
  os.system("cd ~/Project/{0} && git branch".format(zen))
  switch()

  # if choice_ON == 'N' or choice_ON == 'n':
  #   switch()

  branchlist()
  done()
  choiceMenu()

#gitcheckout //OK
def gitcheckout():
  print(style.BOLD+style.GREEN+"                          [log]"+style.END)
  print("==============================================================================")
  os.system("cd ~/Project/{0} && git log --oneline".format(zen))
  print("==============================================================================")
  print(style.BOLD+"Enter the commit ID [ex 9ca266e]"+style.END)

  branchShow()
  idLog = raw_input(style.GREEN+style.BOLD+"[🅸🅳 > "+style.END)

  os.system("cd ~/Project/{0} && tree".format(zen))   
  fileName = raw_input(style.GREEN+"\n[🅵🅸🅻🅴-🅽🅰🅼🅴 > "+style.END)
  os.system("cd ~/Project/{0} && git checkout {1} {2}".format(zen,idLog,fileName))

  done()
  choiceMenu()

#gitrevert //OK
def gitrevert():
  print(style.BOLD+style.GREEN+"                          [log]"+style.END)
  print("==============================================================================")
  os.system("cd ~/Project/{0} && git log --oneline".format(zen))
  print("==============================================================================")
  print(style.BOLD+"Enter the commit ID [ex 9ca266e]"+style.END)

  branchShow()
  idLog = raw_input(style.GREEN+style.BOLD+"[🅸🅳 > "+style.END)

  os.system("cd ~/Project/{0} && git revert {1}".format(zen,idLog))

  done()
  choiceMenu()

#gitreset //OK
def gitreset():
  print(" \n ")
  minikey()
  gitstatus0()
  print("\nEnter the name of the item to reset")

  branchShow()
  reset = raw_input(style.RED+style.BOLD+"[🆁🅴🆂🅴🆃 > "+style.END)

  os.system("cd ~/Project/{0} && git reset -- {1}".format(zen,reset))
  gitstatus0()

  done()
  choiceMenu()

#branchShow //OK
def branchShow():
  print(style.GREEN)
  show_branch = os.system("cd ~/Project/{0} && git branch | grep -i '*'".format(zen))
  return show_branch

#originDirShow //OK
def serverShow():
    print("🇸​​​​​🇪​​​​​🇷​​​​​🇻​​​​​🇪​​​​​🇷​​​​​ => "+remote)


#originIDShow //OK
def originIDShow():
  print("origin-🅘🅓 => "+origin)

#gitmerge //OK
def gitmerge():

  print(" \n ")
  os.system("cd ~/Project/{0} && git checkout master".format(zen))
  print(style.GREEN+"Switch to branch master ... [done]"+style.END)
  time.sleep(0.35)
  print(" \n ")
  print(style.GREEN+style.BOLD+"\nEnter the name of the branch you want to merge of the branch master")
  temp = raw_input(style.PURPLE+"Press [ENTER] to see the list of the existing branch"+style.END)
 

  os.system("cd ~/Project/{0} && git branch".format(zen))
  print(" \n ")
  merge = raw_input(style.GREEN+style.BOLD+"[🅼🅴🆁🅶🅴 > "+style.END)

  os.system("cd ~/Project/{0} && git merge {1}".format(zen,merge))
  print(style.GREEN+"Merge of the {0} branch to the master branch ... [done]".format(merge)+style.END)
  time.sleep(0.35)

  done()
  choiceMenu()

#originlist0 //OK
def originList0():
  print(" \n ")
  temp = raw_input(style.PURPLE+"Press [ENTER] to see the available 'origin ID' & 'server' list..."+style.END)
  print(" \n ")
  os.system("cd ~/Project/{0} && git remote -v".format(zen))
  print(" \n ")

#originlist //OK
def originList():
  print(" \n ")
  temp = raw_input(style.PURPLE+"Press [ENTER] to see the available 'origin ID' & 'server' list ..."+style.END)
  print(" \n ")
  os.system("cd ~/Project/{0} && git remote -v".format(zen))
  print(" \n ")

  done()
  choiceMenu()

#originrename //OK
def originRename():

  originList0()
  
  print(style.BOLD+"Enter origin ID (to rename)"+style.END)
  org0 = raw_input(style.GREEN+style.BOLD+ "[🅾🆁🅸🅶🅸🅽 🅸🅳 > " + style.END) 
  print(" \n ")
  print(style.BOLD+"Rename origin ID"+style.END)
  org1 = raw_input(style.GREEN+style.BOLD+ "[🆁🅴🅽🅰🅼🅴 > " + style.END) 
  os.system("cd ~/Project/{0} && git remote rename {1} {2}".format(zen,org0,org1))
  print(" \n ")

  #origin change
  origin = org1

  os.system("cd ~/Project/{0} &&  git remote -v".format(zen))
  print(style.GREEN+"rename '{0}' to '{1}' ... [done]".format(org0,org1)+style.END)
  time.sleep(0.35)

  done()
  choiceMenu()

#originmenu //OK
def originMenu():
  print("\n**************")
  print(style.DARKCYAN+"0. "+style.END+"list origin id")
  print(style.DARKCYAN+"1. "+style.END+"rename origin id")
  print("**************\n")
 
  branchShow()
  org = raw_input(style.GREEN + style.BOLD+ "[🅸🅽🅿🆄🆃 > " + style.END) 
  
  if org == '0':
    originList()
   
  if org == '1':
    originRename()
   
  done()
  choiceMenu()

#push (manual) //OK
def push():

  #push note
    print(" \n ")
    print(style.DARKCYAN+style.BOLD+"[push (send) usage]======================================================="+style.END)
    print(style.DARKCYAN+" <origin-id> "+style.END+" : by convention, the value given to the origin id is always = 'origin' but this script uses another id for a more efficient organization")
    print(style.DARKCYAN+" [push> "+style.END+"-h : allows you to see the possible option of push ")
    print(style.DARKCYAN+" [push> "+style.END+"<origin-id> <branch> : send the information(s) in the <branch> branch to <origin-id> ")
    print(style.DARKCYAN+" (ex) "+style.END+" : [push]> github-ssh dev")
    print(" \n ")
    print(style.DARKCYAN+"  PS: "+style.END+"'q' to exit push input") 
    print(style.DARKCYAN+style.BOLD+"========================================================================="+style.END)
    print(" \n ")

  #push input (bouclage tant que push different of 'q')
    print("'q' to exit push input")
    push = raw_input(style.GREEN + style.BOLD+ "[🅿🆄🆂🅷 > " + style.END) 
    os.system("cd ~/Project/{0} && git push {1}".format(zen,push))
    print(" \n ")
    while (push != 'q' or push != 'Q'):
      print("'q' to exit push input")
      push = raw_input(style.GREEN + style.BOLD+ "[🅿🆄🆂🅷 > " + style.END) 
      os.system("cd ~/Project/{0} && git push {1}".format(zen,push))
      print(" \n ")
      if push == 'q' or push == 'Q':
        break

    done()
    choiceMenu()

#pushquickly //test
def pushQ():

    #verification
    temp = raw_input(style.BOLD+ "\nBefore executing the quick push, make sure that the branch exists locally, [ENTER] to continue ... " + style.END) 
    branchlist0()

    #pushQ menu
    print("\n    ------------- quick 🅿🆄🆂🅷 ------------")
    print("  /                                       \\")              
    print(style.BOLD+"             0 | to master"+style.END);
    print(style.BOLD+"             1 | to dev"+style.END);
    print(style.BOLD+"             2 | to release"+style.END);
    print(style.BOLD+"             3 | specify branch"+style.END);
    print("  \                                       /")  
    print("    -------------------------------------")
    print("[Origin ID] = {0}".format(origin))

    pushQ = raw_input(style.GREEN + style.BOLD+ "\n[🅿🆄🆂🅷(quick) > " + style.END) 
    
    if pushQ == '0': #to master
      os.system("cd ~/Project/{0} && git push {1} master".format(zen,origin))
      print(style.GREEN+"Origin ID = {0}".format(origin)+style.END)
      print(style.GREEN+"push to master ... [done]"+style.END)
      time.sleep(0.5)

    if pushQ == '1': #to dev
      os.system("cd ~/Project/{0} && git push {1} dev".format(zen,origin))
      print(style.GREEN+"Origin ID = {0}".format(origin)+style.END)
      print(style.GREEN+"push to dev ... [done]"+style.END)
      time.sleep(0.5)

    if pushQ == '2': #to release
      os.system("cd ~/Project/{0} && git push {1} release".format(zen,origin))
      print(style.GREEN+"Origin ID = {0}".format(origin)+style.END)
      print(style.GREEN+"push to release ... [done]"+style.END)
      time.sleep(0.5)

    if pushQ == '3': #specify branch
      print(style.BOLD+"\nManually enter the branch name ... "+style.END)
      branch = raw_input(style.GREEN + style.BOLD+ "[🅱🆁🅰🅽🅲🅷 > " + style.END) 
      os.system("cd ~/Project/{0} && git push {1} {2}".format(zen,origin,branch))
      print(style.GREEN+"Origin ID = {0}".format(origin)+style.END)
      print(style.GREEN+"push to {0} ... [done]".format(branch)+style.END)
      time.sleep(0.5)

    done()
    choiceMenu()
    
#pull //OK
def pull():

  #pull note
    print(" \n ")
    print(style.DARKCYAN+style.BOLD+"[pull (receive) usage]======================================================="+style.END)
    print(style.DARKCYAN+" <origin-id> "+style.END+" : by convention, the value given to the origin id is always = 'origin' but this script uses another id for a more efficient organization")
    print(style.DARKCYAN+" [push> "+style.END+"-h : allows you to see the possible option of pull ")
    print(style.DARKCYAN+" [push> "+style.END+"<origin-id> <branch> : receive the information(s) in the <branch> branch from <origin-id> ")
    print(style.DARKCYAN+" (ex) "+style.END+" : [pull]> bitbucket-https master")
    # print(style.DARKCYAN+" [pull> "+style.END+" : ")
    # print(style.DARKCYAN+"    (ex) "+style.END+" : ")
    # print(style.DARKCYAN+" [pull> "+style.END+" : ")
    # print(style.DARKCYAN+"    (ex) "+style.END+" : ")
    # print(style.DARKCYAN+" [pull> "+style.END+" : ")
    # print(style.DARKCYAN+"    (ex) "+style.END+" : ")
    print(" \n ")
    print(style.DARKCYAN+"  PS: "+style.END+"'q' to exit pull input")
    print(style.DARKCYAN+style.BOLD+"============================================================================"+style.END)
    print(" \n ")

  #pull input (bouclage tant que pull different of 'q')
    print("'q' to exit pull input")
    pull = raw_input(style.GREEN + style.BOLD+ "[🅿🆄🅻🅻 > " + style.END) 
    os.system("cd ~/Project/{0} && git pull {1}".format(zen,pull))
    while (pull != 'q' or pull != 'Q'):
      print("'q' to exit pull input")
      pull = raw_input(style.GREEN + style.BOLD+ "[🅿🆄🅻🅻 > " + style.END) 
      os.system("cd ~/Project/{0} && git pull {1}".format(zen,pull))
      print(" \n ")
      if pull == 'q' or pull == 'Q':
        break

    done()
    choiceMenu()

#exstash //OK
def exstash():
  print(" \n ")

  print(style.PURPLE+"Please put a TAG to better identify your stashes ..."+style.END)
  tag = raw_input(style.GREEN + style.BOLD+ "[🆃🅰🅶 > " + style.END)

  print(" \n ")

  os.system("cd ~/Project/{0} && git stash save '{1}'".format(zen,tag))
  print(style.GREEN+"stash tag = {0}".format(tag)+style.END)
  print(style.GREEN+"stash en memoire ... [done]"+style.END)
  time.sleep(0.35)

  liststash0()

  done()
  choiceMenu()

#liststash //OK
def liststash():
  print(" \n ")

  print(style.GREEN+"         [stash-list]"+style.END) 
  print("================================")
  os.system("cd ~/Project/{0} && git stash list".format(zen))
  print("================================")
  print(style.GREEN+"stash list ... [done]"+style.END)
  time.sleep(0.35)

  done()
  choiceMenu()

#liststash0 //OK
def liststash0():
  print(" \n ")
  
  print(style.GREEN+"         [stash-list]"+style.END) 
  print("================================")
  os.system("cd ~/Project/{0} && git stash list".format(zen))
  print("================================")
  print(style.GREEN+"stash list ... [done]"+style.END)
  time.sleep(0.35)

  print(" \n ")

#applystash //OK
def applystash():

  liststash0()

  print(style.PURPLE+"Enter stash ID to apply (ex: stash@{1})..."+style.END)
  apply = raw_input(style.GREEN + style.BOLD+ "[🅰🅿🅿🅻🆈 > " + style.END)

  print(" \n ")

  os.system("cd ~/Project/{0} && git stash apply {1}".format(zen,apply))
  print(style.GREEN+"stash {0} apply ... [done]".format(apply)+style.END)
  time.sleep(0.35)

  done()
  choiceMenu()

#dropstash //OK
def dropstash():

  liststash0()

  print(style.PURPLE+"Enter stash ID to drop (ex: stash@{1})..."+style.END)
  drop = raw_input(style.GREEN + style.BOLD+ "[🅳🆁🅾🅿 > " + style.END)

  print(" \n ")

  os.system("cd ~/Project/{0} && git stash drop {1}".format(zen,drop))
  print(style.GREEN+"stash {0} drop ... [done]".format(drop)+style.END)
  time.sleep(0.35)

  liststash0()

  done()
  choiceMenu()

#diffstash //OK
def diffstash():

  liststash0()

  print(style.PURPLE+"Enter stash ID to be compared (ex: stash@{1})..."+style.END)
  diff = raw_input(style.GREEN + style.BOLD+ "[🅳🅸🅵🅵 > " + style.END)

  print(" \n ")

  os.system("cd ~/Project/{0} && git stash show {1} -p".format(zen,diff))
  print(style.GREEN+"stash diff ... [done] "+style.END)
  time.sleep(0.35)

  done()
  choiceMenu()

#branchstash //OK
def branchstash():

  print(" \n ")
  os.system("cd ~/Project/{0} && git branch".format(zen))

  print(style.PURPLE+"Copy the stashes stored in memory to the branch ... "+style.END)
  branch = raw_input(style.GREEN + style.BOLD+ "[🅱🆁🅰🅽🅲🅷 > " + style.END)
  #if branch !exist
  os.system("cd ~/Project/{0} && git branch {1}".format(zen,branch))

  print(" \n ")

  os.system("cd ~/Project/{0} && git stash branch {1} -p".format(zen,branch))
  print(style.GREEN+"stash branch ... [done] "+style.END)
  time.sleep(0.35)

  print(" \n ")

  os.system("cd ~/Project/{0} && git checkout {1}".format(zen,branch))
  print(style.GREEN+"Switch to {0} branch ... [done] "+style.END)
  time.sleep(0.35)

  liststash0()

  done()
  choiceMenu()

#gitstash //OK
def gitstash():
  print("\n**************")
  print(style.DARKCYAN+"0. "+style.END+"exec stash")
  print(style.DARKCYAN+"1. "+style.END+"list stash")
  print(style.DARKCYAN+"2. "+style.END+"apply stash")
  print(style.DARKCYAN+"3. "+style.END+"drop stash")
  print(style.DARKCYAN+"4. "+style.END+"diff stash")
  print(style.DARKCYAN+"5. "+style.END+"branch stash")
  print("**************\n")
 
  branchShow()
  stash = raw_input(style.GREEN + style.BOLD+ "[🅸🅽🅿🆄🆃 > " + style.END) 
  
  if stash == '0':
    #stash save (ettiquete)
    exstash()
   
  if stash == '1':
    liststash()
   
  if stash == '2':
    #apply per ID
    applystash()
   
  if stash == '3':
    dropstash()

  if stash == '4':
    diffstash()

  if stash == '5':
    branchstash()
   
  done()
  choiceMenu()

#forward //test*
def forward():

  print(" \n ")
  temp = raw_input(style.BOLD+"You are sure you want to update the FORK, [ENTER] to continue, [CTRL + C] to cancel ..."+style.END)
  print(" \n ")

  #add upstream
  print(style.PURPLE+"Enter 'HTTPS url' from the original repository ..."+style.END)
  url = raw_input(style.GREEN + style.BOLD+ "[🆄🆁🅻 > " + style.END) 

  print(" \n ")

  os.system("cd ~/Project/{0} && git remote add upstream {1}".format(zen,url))
  print(style.GREEN+"upstream added ... [done]"+style.END)
  time.sleep(0.35)

  os.system("cd ~/Project/{0} && git remote -v".format(zen))
  print(style.GREEN+"verify upstream ... [done]"+style.END)
  time.sleep(0.35)

  os.system("cd ~/Project/{0} && git fetch upstream".format(zen))
  print(style.GREEN+"fetch upstream ... [done]"+style.END)
  time.sleep(0.35)

  os.system("cd ~/Project/{0} && git branch -a".format(zen))
  print(style.GREEN+"verify remote branch upstream ... [done]"+style.END)
  time.sleep(0.35)

  os.system("cd ~/Project/{0} && git merge upstream/master".format(zen))
  print(style.GREEN+"auto update all informations on branch master ... [done]"+style.END)
  time.sleep(0.35)

  print(" \n ")

  print(style.GREEN+style.BOLD+"fast-forward ... [done]"+style.END)
  time.sleep(1)

  done()
  choiceMenu()

#report //OK
def report():
   print(style.BOLD+"[report]"+style.END)
   print("   |")
   print("   |>> email: raja.rakoto7@gmail.com")
   print("   |>> facebook: https://www.facebook.com/raja.rakotonirina")
   print("   |>> linkedin: https://www.linkedin.com/in/raja-rakotonirina-20a0b116b")
#============================FONCTIONS-end============================



#debugZone //OK
def debugZone():
  done()
  choiceMenu()

#note local //OK
def noteLR():
  print(" \n ")
  print(style.GREEN+style.BOLD+"[note local working]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+style.END)
  print ("- Move your files to 'tmp' to be ignored of git")
  time.sleep (0.1)
  print ("- Edit the file 'README.md' to add info about your project")
  time.sleep (0.1)
  print (style.GREEN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "+ style.END)
  print ("\n")
  print (style.GREEN + style.BOLD + "[note remote working]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "+ style.END)
  print ("- If it's a remote git repository, no one (except those who have permission to access the server) can manipulate it")
  time.sleep (0.1)
  print ("- When creating a new project, only one person (the project manager) must perform the first validation of the project (of remote mode) so that the other members can clone his repository (project) ")
  time.sleep (0.1)
  print ("- For a more efficient organization, it is strongly recommended to create a branch for each category of employee before starting work")
  time.sleep (0.1)
  print ("- Be careful not to delete (by accident) the 'Server' folder because it contains all the configurations/logs of your git server")
  time.sleep (0.1)
  print ("- Remember to make a complete backup of your project (of time to time) to avoid bad expectations")
  time.sleep(0.1)
  print(style.GREEN+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+style.END)
  print(" \n ")



#============================LOCAL-begin==============================
#create local project //OK
def GenProjLocal():

   print(" \n ") 
   print(style.BOLD+style.DARKCYAN+"      >>> LOCAL PROJECT GENERATOR <<<"+style.END)
   time.sleep(2)
   print(" \n ")

  #This can return a false positive if the Project directory already exists (this is normal) - contains all the projects the script uses
   os.system("cd $HOME && mkdir Project")
   print(style.GREEN+"Generate Project directory in $HOME ... [done]"+style.END)
   time.sleep(1)

  #Creation of the project directory
   print(style.GREEN+"Generate project '{0}' ... [done]".format(newProjectName)+style.END)
   time.sleep(1)
   os.system("mkdir -p ~/Project/{0}".format(newProjectName))

  #LOCAL (git init)
   os.system("cd ~/Project/{0} && git init".format(newProjectName))
   print(style.GREEN+"git init ... [done]"+style.END)
   time.sleep(1)
   print(style.GREEN+"Init versioning ... [done]"+style.END)
   time.sleep(1)
   print(style.GREEN+".git config ... [done]"+style.END)
   time.sleep(1)

 #local config

   print("\n")
   print(style.BOLD+style.GREEN+"Init LOCAL config ... [done]"+style.END)
   time.sleep(1)
   print(" \n ")
   
  #gitignore & tmp
   os.system("cd ~/Project/{0} && touch .gitignore".format(newProjectName))
   print(style.GREEN+"Generate .gitignore ... [done]"+style.END)
   time.sleep(1)

   os.system("cd ~/Project/{0} && mkdir tmp && echo 'tmp' > .gitignore && echo 'tmp/*' >> .gitignore && echo 'log_ssh-keygen' >> .gitignore".format(newProjectName))
   print(style.GREEN+"Generate tmp folder ... [done]"+style.END)
   time.sleep(1)

   print(style.GREEN+".gitignore config... [done]"+style.END)
   time.sleep(1)
   os.system("cd ~/Project/{0} && cat .gitignore".format(newProjectName))
   print(style.GREEN+"Checking .gitignore ... [done]"+style.END)
   time.sleep(1)

   os.system("cd ~/Project/{0} && touch README.md && echo '~ About the project {0} ~' > README.md".format(newProjectName))
   print(style.GREEN+"Generate README.md ... [done]"+style.END)
   time.sleep(1)

   print(" \n ")
   print(style.GREEN+style.BOLD+"all LOCAL config ... [done]"+style.END)
   time.sleep(2)

  #note 
   noteLR()

   print(style.BOLD+"You can now work in 'LOCAL' mod (main screen) ... "+style.END)
  
   done()
   choiceMain()
#============================LOCAL-end================================



#============================REMOTE-begin=============================
#remoteconfig //OK
def remotePREconfig():
      print(" \n ") 
      print(style.BOLD+style.DARKCYAN+"      >>> REMOTE CONFIG <<<    "+style.END)
      time.sleep(2)
      print(" \n ")

   #local config
      os.system("cd ~/Project/{0} && git init".format(newProjectName))
      print(style.GREEN+"git init ... [done]"+style.END)
      time.sleep(1)
      print(style.GREEN+"Init versioning ... [done]"+style.END)
      time.sleep(1)
      print(style.GREEN+".git config ... [done]"+style.END)
      time.sleep(1)

      print("\n")
      print(style.BOLD+style.GREEN+"Init LOCAL config ... [done]"+style.END)
      print(" \n ")
   
      #gitignore & tmp 
      os.system("cd ~/Project/{0} && touch .gitignore".format(newProjectName))
      print(style.GREEN+"Generate .gitignore ... [done]"+style.END)
      time.sleep(1)
  
      os.system("cd ~/Project/{0} && mkdir tmp && echo 'tmp' > .gitignore && echo 'tmp/*' >> .gitignore".format(newProjectName))
      print(style.GREEN+"Generate tmp folder ... [done]"+style.END)
      time.sleep(1)
  
      print(style.GREEN+".gitignore config ... [done]"+style.END)
      time.sleep(1)
      os.system("cd ~/Project/{0} && cat .gitignore".format(newProjectName))
      print(style.GREEN+"Checking .gitignore ... [done]"+style.END)
      time.sleep(1)

      print(" \n ")
      print(style.GREEN+style.BOLD+"all LOCAL config ... [done]"+style.END)
      time.sleep(2)
      print(" \n ")
      
      print(" \n ")
      print(style.BOLD+style.GREEN+"Init REMOTE config ... [done]"+style.END)
      time.sleep(2)
      print(" \n ")

#creer un projet remote //OK
def GenProjRemote():

   print(" \n ") 
   print(style.BOLD+style.DARKCYAN+"      >>> REMOTE PROJECT GENERATOR <<<"+style.END)
   time.sleep(2)
   print(" \n ")
  
  #Project folder
   os.system("cd ~/Project/ && mkdir {0}".format(newProjectName))
   print(style.GREEN+"Generate project '{0}' folder ... [done]".format(newProjectName)+style.END)
   time.sleep(1)

  #This can return a false positive if the Project & Server directory already exists (this is normal) - contains all the projects the script uses
   os.system("cd $HOME && mkdir Project && cd Project && mkdir Server")
   print(style.GREEN+"Generate Project & Server directory in $HOME ... [done]"+style.END)
   time.sleep(1)

  #Creation du repertoire of projet
   os.system("mkdir -p ~/Project/Server/{0}".format(newProjectName))
   print(style.GREEN+"Generate server '{0}' ... [done]".format(newProjectName)+style.END)
   time.sleep(2)

  #REMOTE (git init --bare)
   os.system("cd ~/Project/Server/{0} && git init --bare".format(newProjectName))
   print(style.GREEN+"git init --bare ... [done]"+style.END)
   time.sleep(1)
   print(style.GREEN+"Init versioning ({0}-server) ... [done]".format(newProjectName)+style.END)
   time.sleep(1)

  #remote pre-conf
   remotePREconfig()

  #note 
   noteLR()
   
   print(style.BOLD+"The project manager should now connect in 'REMOTE' mod (main screen) for the first validation of the project ... "+style.END)

   done()
   choiceMain()


#validation //OK
def validation():
   
   print(" \n ")
   print(style.BOLD+style.DARKCYAN+"      >>> VALIDATION <<<"+style.END)
   time.sleep(2)
   print(" \n ")

   #create README.md
   os.system("cd ~/Project/{0} && touch README.md && echo '~ About the {0} project ~' > README.md".format(zen))
   print(style.GREEN+"Generate README.md ... [done]"+style.END)
   time.sleep(1)

   #first pull (if LICENCE exist)
   print(" \n ")
   os.system("cd ~/Project/{0} && git pull {1} master".format(zen,origin))
   print(style.GREEN+"pull verification ... [done]"+style.END)
   time.sleep(1)

   #status & add & commit & push (master)
   print(" \n ")
   os.system("cd ~/Project/{0} && git status".format(zen))
   print(style.GREEN+"status 1 ... [done]"+style.END)
   time.sleep(1)

   print(" \n ")
   os.system("cd ~/Project/{0} && git add *".format(zen))
   print(style.GREEN+"add ... [done]"+style.END)
   time.sleep(1)

   print(" \n ")
   os.system("cd ~/Project/{0} && git status".format(zen))
   print(style.GREEN+"status 2 ... [done]"+style.END)
   time.sleep(1)

   #1st commit 
   print(" \n ")
   os.system("cd ~/Project/{0} && git commit -m '1st validation'".format(zen))
   print(style.GREEN+"1st validation ... [done]"+style.END)
   time.sleep(1)
    
   print(" \n ")
   os.system("cd ~/Project/{0} && git push {1} master".format(zen,origin))
   print(style.GREEN+"push {0} master... [done]".format(origin)+style.END)
   time.sleep(1)

   print(" \n ")
   print(" \n ")
   print(style.GREEN+style.BOLD+"The project '{0}' is now valid ! you can now use the available git tools".format(zen)+style.END)
   time.sleep(2)

   done()
   menu()
#============================REMOTE-end===============================



#============================LOCAL MODEL-begin========================
#localmodel //OK
def localmodel():

   localmodel = "local-model"
   print(" \n ")
   print(style.BOLD+style.DARKCYAN+"      >>> LOCAL MODEL GENERATOR <<<"+style.END)
   time.sleep(0.1)
   print(" \n ")
 
 #creation du repertoire local-model
   os.system ("mkdir -p ~/Project/{0}".format(localmodel))
   print(style.GREEN+"Generate {0} ... [done]".format(localmodel)+style.END)
   time.sleep(0.01)

 #initialisation of git dans local-model 
   os.system("cd ~/Project/{0} && git init".format(localmodel))
   print(style.GREEN+"git init ... [done]"+style.END)
   time.sleep(0.01)
   print(style.GREEN+"Init du versioning ... [done]"+style.END)
   time.sleep(0.01)
   print(style.GREEN+".git config ... [done]"+style.END)
   time.sleep(0.01)

 #conf local-model

   print("\n")
   print(style.BOLD+style.GREEN+"Init LOCAL-MODEL config ... [done]"+style.END)
   time.sleep(0.1)
   print(" \n ")

  #gitignore - temp - readme
   os.system("cd ~/Project/{0} && touch .gitignore".format(localmodel))
   print(style.GREEN+"Generate .gitignore ... [done]"+style.END)
   time.sleep(0.01)

   os.system("cd ~/Project/{0} && mkdir tmp && echo 'tmp' > .gitignore && echo 'tmp/*' >> .gitignore".format(localmodel))
   print(style.GREEN+"Generate tmp folder ... [done]"+style.END)
   time.sleep(0.01)

   print(style.GREEN+".gitignore config ... [done]"+style.END)
   time.sleep(0.01)
   os.system("cd ~/Project/{0} && cat .gitignore".format(localmodel))
   print(style.GREEN+"Checking .gitignore ... [done]"+style.END)
   time.sleep(0.01)

   os.system("cd ~/Project/{0} && touch README.md && echo '~ A propos du projet {0} ~' > README.md".format(localmodel))
   print(style.GREEN+"Generate README.md ... [done]"+style.END)
   time.sleep(0.01)

   print(" \n ")
   print(style.GREEN+style.BOLD+"all LOCAL-MODEL config ... [done]"+style.END)
   time.sleep(0.5)


#localclean //OK
def localclean():
  os.system ("sudo rm -r ~/Project/local-model")
  print(style.GREEN+"Cleaning local-model ... [done]"+style.END)
  localmodel()
#============================LOCAL MODEL-end==========================



#============================MENU-begin===============================
#menu //OK
def menu():
 #menu0  

     os.system("cd ~/Project/{0}".format(zen))
     print(style.GREEN+"Switching to {0} ... [done]".format(zen)+style.END)  
     print(style.RED+"________________________________________________________________________"+style.END)        
     print ( style.RED + style.BOLD + "\n             ~ 𝔾 𝕀 𝕋  𝕧 𝕖 𝕣 𝕤 𝕚 𝕠 𝕟 𝕚 𝕟 𝕘  𝕥 𝕠 𝕠 𝕝 𝕤 ~" + style.END)
     print("                          Author: Raja")        
 
     print(style.BOLD+" ______________________________________________________________________"+style.END)
     print(style.BOLD+"/                                                                      \ "+style.END)
 
 #menu1 //OK
  
     print(style.BOLD+style.YELLOW+"  🅄 🄽 🄶 🄸 🅃  working directory"+style.GREEN+"               [𝙋𝙍𝙊𝙅𝙀𝘾𝙏 = {0}]".format(zen)+style.END)
     localProject()

 #menu2
     print(style.BOLD+"---------------------------------------------------------------------- "+style.END)
    
    #config
     print(style.PURPLE+"   🅒🅞🅝🅕🅘🅖"+style.END+"   | "+style.DARKCYAN+"⓪"+ style.END + " - git config (menu)          |"+style.YELLOW+"        config        "+style. END+"  |")
     print("---------------------------------------------------------------------<          ") 
    
    #manip
     print("            | "+style.DARKCYAN+"①"+ style.END + " - git add (dans l'index)     |"+style.YELLOW+"         add           "+style.END+" |")
     print(style.PURPLE+"   🅜🅐🅝🅘🅟    "+style.END+"| "+style.DARKCYAN+"②"+ style.END + " - git remove (of l'index)    |"+style.YELLOW+"         del           "+style. END+" |")
     print("            | "+style.DARKCYAN+"③"+ style.END + " - git ignore|reignore (menu) |"+style.YELLOW+"     (e/re)+[temp]     "+style.END+" |")
     print("---------------------------------------------------------------------<          ") 

    #log/history 
     print(style.PURPLE+"    🅛🅞🅖"+style.END+"     | "+style.DARKCYAN+"④"+ style.END + " - git log (menu)             |"+style.YELLOW+"      log/history      "+style.END +" |")
     print(style.PURPLE+"  🅗🅘🅢🅣🅞🅡🅨"+style.END+"   | "+style.DARKCYAN+"⑤"+ style.END + " - git diff                   |"+style.YELLOW+"         diff          "  +style.END+" |")
     print("---------------------------------------------------------------------<          ")   
     
    #backup 
     print("            | "+style.DARKCYAN+"⑥"+ style.END + " - git checkout               |"+style.YELLOW+"        check          "+style.END+" |")
     print(style.PURPLE+"   🅑🅐🅒🅚🅤🅟"+style.END+"   | "+style.DARKCYAN+"⑦"+ style.END + " - git revert                 |"+style.YELLOW+"         rev           " +style. END+" |")
     print("            | "+style.DARKCYAN+"⑧"+ style.END + " - git reset                  |"+style.YELLOW+"         res           "+style.END+" |")
     print("            | "+style.DARKCYAN+"⑨"+ style.END + " - git stash (menu)           |"+style.YELLOW+"[stash]+_exec/list/apply"+style.END+"|")
     print("            | "+style.DARKCYAN+" "+ style.END + "                              |"+style.YELLOW+"    /drop/diff/branch"+style.END+"   |")
     print("---------------------------------------------------------------------<          ")   
     
    #branch
     print("            |"+style.DARKCYAN+"①⓪"+ style.END + " - git branch (local - menu)  |"+style.YELLOW+"      l+[br]/rm_br     "+style.END+" |")
     print(style.PURPLE+"   🅑🅡🅐🅝🅒🅗"+style.END+"   |"+style.DARKCYAN+"①①"+ style.END + " - git merge (fusion)         |"+style.YELLOW+"         merge       " +style. END+"   |")
     print("            |"+style.DARKCYAN+"①②"+ style.END + " - switch branch              |"+style.YELLOW+"         sbr           "+style.END+" |")
     print("---------------------------------------------------------------------<          ")   
    
    #workflows
     print("            |"+style.DARKCYAN+"①③"+ style.END + " - git branch (remote - menu) |"+style.YELLOW+"   r+l+[br]/rm_rbr"+style.END+"      |")
     print("            |"+style.DARKCYAN+"①④"+ style.END + " - origin (menu)              |"+style.YELLOW+"  [org]+_(rename/list)" +style. END+"  |")
     print(style.PURPLE+" 🅦🅞🅡🅚🅕🅛🅞🅦🅢"+style.END+"  |"+style.DARKCYAN+"①⑤"+ style.END + " - git push (send request)    |"+style.YELLOW+"      push/pushq       "  +style.END+" |")
     print("            |"+style.DARKCYAN+"①⑥"+ style.END + " - git pull (receive request) |"+style.YELLOW+"         pull          "+style.END+" |")
     print("            |"+style.DARKCYAN+"①⑦"+ style.END + " - fast forward (update repo) |"+style.YELLOW+"        update          "+style.END+"|")
     print("---------------------------------------------------------------------<          ") 
     
    #other
     print(style.PURPLE+"   🅞🅣🅗🅔🅡 "+style.END+"   |"+style.DARKCYAN+" a"+ style.END + " - check project (menu)       |"+style.YELLOW+"      s/ls/tree      " +style. END+"   |")
     print("            |"+style.DARKCYAN+" b"+ style.END + " - shell                      |"+style.YELLOW+"          sh           " +style. END+" |")
     print(style.BOLD+"---------------------------------------------------------------------- "+style.END)
    #  print("---------------------------------------------------------------------<          ") 
     print(style.GREEN+style.BOLD+"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\   🇨 ​​​​​🇴​​​​​ 🇲 ​​​​​🇲​ ​​​​🇮​ ​​​​🇹   ///////////////////////////"+style. END)
     print(style.GREEN+style.BOLD+"/////////////////////////       [c]       \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"+style.END)
  
  #menu3
     if mainPut == 'remote' or mainPut == 'REMOTE':
        print("   >--------------------------------------------------------------< "+style.END)
        print(style.YELLOW + "        v|valid" + style.END + " > valid the project '{0}' (exec 1x)                 ".format(zen))
     
     if mainPut == 'local' or mainPut == 'LOCAL' or mainPut == 'remote' or mainPut == 'REMOTE':
        print("   >--------------------------------------------------------------< "+style.END)
        print(style.YELLOW + "        t|touch" + style.END + " > create one/more file(s)                           ")
        print(style.YELLOW + "        r|remove" + style.END + " > delete one/more file(s) & directory(s)     ")
        print(style.YELLOW + "       ls|list" + style.END + " > list the element(s) of your project                ")
     
     if mainPut == 'localmod' or mainPut == 'LOCALMOD':
        print("   >--------------------------------------------------------------< "+style.END)
        print(style.YELLOW + "        d|debug" + style.END + " > exec debug-zone                                         ")
        print(style.YELLOW + "        t|touch" + style.END + " > create one/more file(s)                           ")
        print(style.YELLOW + "        r|remove" + style.END + " > delete one/more file(s) & directory(s)      ")
        print(style.YELLOW + "       ls|list" + style.END + " > list the element(s) of your project                  ")
     print("   >--------------------------------------------------------------< "+style.END)
  
  
  #menu4
     if mainPut == 'localmod' or mainPut == 'LOCALMOD':
       print(style.DARKCYAN + "        [𝔠𝔩𝔢𝔞𝔫] " + style.END + "renew the local-model project")
     
     print(style.DARKCYAN + "          [𝔯𝔢𝔞𝔡𝔪𝔢] " + style.END + "edit the README.md file of the project")
     print(style.DARKCYAN + "          [𝔪𝔞𝔦𝔫] " + style.END + "return to the main screen")
     print(style.DARKCYAN + "          [𝔫𝔬𝔱𝔢(fr)] " + style.END + "see the git-note & list of executable command")
     print(style.DARKCYAN + "          [𝔥𝔢𝔩𝔭|𝔪𝔞𝔫] " + style.END + "man page (official) of git")
     print(style.DARKCYAN + "          [q|𝔢𝔵𝔦𝔱] " + style.END + "exit menu")

     print(style.BOLD+"\______________________________________________________________________/"+style.END)
     os.system("git --version")

  #mod logo
     if mainPut == 'local' or mainPut == 'LOCAL':
       print("L𝖮⊂ᎯL")
     if mainPut == 'remote' or mainPut == 'REMOTE':
       print("ᖇ∈ⲙ𝖮𝜏∈")
     if mainPut == 'localmod' or mainPut == 'LOCALMOD':
       print("L𝖮⊂ᎯL ⲙᗝᖙ∈𝘭")
     print(style.RED+"________________________________________________________________________"+style.END)     

  #### inPut ####

   #branchshow
     serverShow() 
     originIDShow()

     branchShow()
     inPut = raw_input(style.GREEN + style.BOLD +"[🅶🅸🆃 > "+style.END)

#===============touch & remove
  # ... //del
  # if inPut == "d" or inPut == "D" or inPut == "debug" or inPut == "DEBUG": 
  #   branchShow()

     if inPut == "v" or inPut == "V" or inPut == "valid" or inPut == "VALID":
       validation()

     if inPut == "t" or inPut == "T" or inPut == "touch" or inPut == "TOUCH":
       touch()
   
     if inPut == "r" or inPut == "R" or inPut == "remove" or inPut == "REMOVE":
       remove()
#===============gitconfig
     if inPut == '0' or inPut == 'config'  or inPut == 'CONFIG':
       gitConfig()
   
     if inPut == 'configlob' or inPut == 'CONFIGLOB':
       configlob()
   
     if inPut == 'configmail' or inPut == 'CONFIGMAIL':
       configmail()
   
     if inPut == 'configname' or inPut == 'CONFIGNAME':
       configname()
     
     if inPut == 'configrebase' or inPut == 'CONFIGREABASE':
       rebase()

     if inPut == 'configquick' or inPut == 'CONFIGQUICK':
       configquick()
#===============gitadd & gitremove
     if inPut == '1'  or inPut == 'add' or inPut == 'ADD' or inPut == '+':
       gitadd()

     if inPut == '2'  or inPut == 'del' or inPut == 'DEL' or inPut == '-':
       gitremove()
#===============gitignore & reignore
     if inPut == '3':
       gitignore()

     if inPut == 'ignore' or inPut == 'IGNORE' or inPut == 'temp' or inPut == 'TEMP':
       gitignoreList()

     if inPut == 'reignore' or inPut == 'REIGNORE' or inPut == 'retemp' or inPut == 'RETEMP':
       reIgnore()
  
     if inPut == 'eignore' or inPut == 'EIGNORE' or inPut == 'etemp' or inPut == 'ETEMP':
       gitignoreEdit()
#===============gitlog & history
     if inPut == '4':
       gitlog()

     if inPut == 'log' or inPut == 'LOG' or inPut == 'l' or inPut == 'L':
       log()

     if inPut == 'history' or inPut == 'HISTORY' or inPut == 'h' or inPut == 'H':
       history()
#===============gitdiff 
     if inPut == '5'  or inPut == 'diff' or inPut == 'DIFF' or inPut == 'df' or inPut == 'DF':
       gitdiff()
#===============gitcheckout & gitrevert & gitreset
     if inPut == '6' or inPut == 'checkout' or inPut == 'CHECKOUT' or inPut == 'check' or inPut == 'CHECK':
       gitcheckout()    
   
     if inPut == '7' or inPut == 'rev' or inPut == 'REV' or inPut == 'revert' or inPut == 'REVERT':
       gitrevert()
   
     if inPut == '8' or inPut == 'res' or inPut == 'RES' or inPut == 'reset' or inPut == 'reset':
       gitreset()
#===============gitstash
     if inPut == '9' or inPut == 'stash' or inPut == 'STASH':
       gitstash()

     if inPut == 'stash exec' or inPut == 'STASH EXEC':
       exstash()

     if inPut == 'stash list' or inPut == 'STASH LIST':
       liststash()

     if inPut == 'stash apply' or inPut == 'STASH APPLY':
       applystash()

     if inPut == 'stash drop' or inPut == 'STASH DROP':
       dropstash()

     if inPut == 'stash diff' or inPut == 'STASH DIFF':
       diffstash()

     if inPut == 'stash branch' or inPut == 'STASH BRANCH':
       branchstash()
#===============gitbranch & gitmerge
     if inPut == '10' or inPut == 'branch' or inPut == 'BRANCH':
       gitbranch()
   
     if inPut == 'br' or inPut == 'BR' or inPut == 'new' or inPut == 'NEW':
       exGitbranch()
   
     if inPut == 'lbr' or inPut == 'LBR':
       branchlist()

     if inPut == 'rm br' or inPut == 'RM BR':
       branchremove()

     if inPut == '11' or inPut == 'merge' or inPut == 'MERGE' or inPut == 'mbr' or inPut == 'MBR':
       gitmerge()

     if inPut == '12' or inPut == 'sbr' or inPut == 'SBR' or inPut == 'switch' or inPut == 'SWITCH':
       switchMain()
   
#===============remote
     if inPut == '13': 
       gitbranchRemoteMenu()
     
     if inPut == 'rbr' or inPut == 'RBR' or inPut == 'rnew' or inPut == 'RNEW' : 
       exgitbranchRemoteMenu()
   
     if inPut == 'rlbr' or inPut == 'RLBR': 
       gitbranchRemoteList()
   
     if inPut == 'rm rbr' or inPut == 'RM RBR': 
       gitbranchRemoteRemove()

#===============origin
     if inPut == '14' or inPut == 'org' or inPut == 'ORG':
       originMenu()

     if inPut == 'org rename' or inPut == 'ORG RENAME':
       originRename()

     if inPut == 'org list' or inPut == 'ORG LIST':
       originList()

#===============pull & push
     if inPut == '15' or inPut == 'push' or inPut == 'PUSH':
       push()

     if inPut == 'pushq' or inPut == 'PUSHQ':
       pushQ()

     if inPut == '16' or inPut == 'pull' or inPut == 'PULL':
       pull()

#===============fast-forward
     if inPut == '17' or inPut == 'update' or inPut == 'UPDATE':
       forward()

#===============checkproj
     if inPut == 'A' or inPut == 'a':
       checkProj()

#===============shell
     if inPut == 'B' or inPut == 'b' or inPut == 'sh' or inPut == 'SH' or inPut == 'shell' or inPut == 'SHELL':
       shell()

#===============gitcommit
     if inPut == 'c' or inPut == 'C' or inPut == 'commit' or inPut == 'COMMIT' or inPut == 'com' or inPut == 'COM' or inPut == "/":
       gitCommit()
#===============gitstatus & tree
     if inPut == 'status' or inPut == 'STATUS' or inPut == 's' or inPut == 'S':
       gitstatus()

     if inPut == "tree" or inPut == 'TREE' or inPut == 'ls' or inPut == 'LS' or inPut == "list" or inPut == 'LIST':
       tree()
#===============readme
     if inPut == 'readme' or inPut == 'README':
       readme()

#mini-menu
     if inPut == "clean" or inPut == 'CLEAN':
       if mainPut == 'localmod' or mainPut == 'LOCALMOD' or mainPut == 'lm' or mainPut == 'LM':
         localclean()

     if inPut == "main" or inPut == 'MAIN':
       restart()
     
     if inPut == "note" or inPut == 'NOTE':
       note1()
     
     if inPut == "notefr" or inPut == 'NOTEFR':
       note1FR()
     
     if inPut == "help" or inPut == 'HELP' or inPut == "man" or inPut == 'MAN':
       manual()
       choiceMenu()
      
    #  if inPut == 'q' or inPut == 'Q' or inPut == 'quit' or inPut == 'QUIT' or inPut == 'exit' or inPut == 'EXIT':
    #    exit0()

#loopback
     while (True):
       if inPut == 'q' or inPut == 'Q' or inPut == 'quit' or inPut == 'QUIT' or inPut == 'exit' or inPut == 'EXIT':
         break
   
       if inPut != 'q' or inPut != 'Q' or inPut != 'quit' or inPut != 'QUIT' or inPut != 'exit' or inPut != 'EXIT':
         menu()
         break
#=================================MENU-end============================



#=================================MAIN-begin==========================
#main //OK
while (True):

#===============main0 
   print("\n")
 
   title()
#===============main1
   print(style.BOLD+"___________________________________________________________________________________________"+style.END)
   print (style.BOLD+"Welcome to" + style.RED + style.BOLD + "\nGIT versioning tools" + style.END)
   print("Author: Raja")
   os.system("git --version")
   print("||")
   listProj()
   print("||")
   print("||"+"    ------------------------------------- 🅼🅰🅸🅽 -----------------------------------")
   print("||"+"  /                                                                                \\")              
   print("||"+style.RED+"______⓿⓿   |git "+style.END+"- install git [internet required]")
   print("||"+style.RED+"______⓿    |config "+style.END+"- quickly configure your git profile [to be executed for new users]")
   print("||"+style.RED+"______➊    |clone "+style.END+"- clone a repository [internet required]")
   print("||"+style.RED+"______➋    |new local "+style.END+"- create a project [local repository]")
   print("||"+style.RED+"______➌    |new remote "+style.END+"- create a project [remote repository]")
   print("||"+style.RED+"______➍    |del & delall "+style.END+"- delete one/more project(s) [local]")
   print("||"+style.RED+"______➎    |purge "+style.END+"- purge a project and clear all traces from git [log/history]")
   print("||"+style.RED+"______➏    |backup "+style.END+"- create a backup of the whole project/server [local]")
   print("||"+"  \                                                                                /")  
   print("||"+"    ------------------------------------------------------------------------------")
#===============main2
 #local & remote menu
   print("||")
   print("||"+style.GREEN+style.BOLD+ "_______________________________🄻 🄾 🄲 🄰 🄻 => " + style.END + "local mod")
   print("||"+style.GREEN+style.BOLD+ "______________________________🅁 🄴 🄼 🄾 🅃 🄴 => " + style.END + "remote mod")
   print("||")
#===============main3
 #plugins menu
   print("||"+style.BOLD + "________________{🅢🅢🅗 } "+style.END+"install/use SSH [internet required]")
   print("||"+style.BOLD + "________________{🅣🅘🅛🅘🅧 } "+style.END+"install/use TILIX [internet required]")
   print("||"+style.YELLOW + style.BOLD + "________________{🅤🅝🅖🅘🅣 } "+style.END+"install/use UNGIT [internet required]")
   print("||"+style.YELLOW + style.BOLD + "________________{🅕🅛🅞🅦 } "+style.END+"install/use GITflow [internet required]")
#===============main4
 #other menu (localmod - note - help|man - q|exit)
   print("||")
   print("||"+style.DARKCYAN + "____________[debug] " + style.END + "exec local-model")
   print("||"+style.DARKCYAN + "____________[𝔫𝔬𝔱𝔢(fr)] " + style.END + "to see the git-note & list of executable command")
   print("||"+style.DARKCYAN + "____________[𝔰𝔢𝔯𝔳𝔦𝔠𝔢(fr)] " + style.END + "to see third-party services of Github and Bitbucket")
   print("||"+style.DARKCYAN + "____________[𝔥𝔢𝔩𝔭|𝔪𝔞𝔫] " + style.END + "man page (official) of git")
   print("||"+style.DARKCYAN + "____________[q|𝔢𝔵𝔦𝔱] " + style.END + "exit script")
   print("||")
   print("||"+style.BOLD+"____________________________________________________________________________________________"+style.END)
   report()
#===============main5
 #prompt mainput
   mainPut = raw_input(style.GREEN + style.BOLD + "\n[🅸🅽🅿🆄🆃 > " +  style.END)
#===============main6
 #00
   if mainPut == '00' or mainPut == 'git' or mainPut == 'GIT':
     installGit()
#===============main6.0
 #0
   if mainPut == '0' or mainPut == 'config' or mainPut == 'CONFIG':

     print(style.DARKCYAN +"\n[config-status-global]--------------------" + style.END)
     os.system("git config --list")
     print(style.DARKCYAN +"------------------------------------------" + style.END)

     configquick0()
#===============main7
 #1
   if mainPut == '1' or mainPut == 'clone' or mainPut == 'CLONE':
     gitclone()
#===============main8
 #2
   if mainPut == '2' or mainPut == 'new local' or mainPut == 'NEW LOCAL':
     print(" \n ")
     print(style.BOLD+"[Note] : No space on the project name"+style.END)
     newProjectName = raw_input(style.GREEN + style.BOLD +"[🅽🅰🅼🅴 > " + style.END)
     GenProjLocal()
#===============main9
 #3
   if mainPut == '3' or mainPut == 'new remote' or mainPut == 'NEW REMOTE':
     print(" \n ")
     print(style.BOLD+"[Note] : No space on the project name"+style.END)
     newProjectName = raw_input(style.GREEN + style.BOLD +"[🅽🅰🅼🅴 > " + style.END)
     origin = "origin"
     os.system("cd ~/Project/ && mkdir {0}".format(newProjectName))
     GenProjRemote()
#===============main10
 #4
   if mainPut == '4' or mainPut == 'del' or mainPut == 'DEL':
     print(style.BOLD+"Enter the name of the project to delete\n"+style.END)
   
     delProjectName = raw_input(style.RED + "[🅳🅴🅻🅴🆃🅴> " + style.END)
     
     #undel VIP files 
     if delProjectName == 'Server' or delProjectName == 'gitvers-tool' or delProjectName == 'ALL-PROJECT-SERVER-BACKUP.tar.gz':
       print(style.RED+"[Warning!]: it is impossible to delete '{0}', operation canceled ... ".format(delProjectName)+style.END)
       choiceMain()
     else:
       os.system("sudo rm -r ~/Project/{0}".format(delProjectName))
       print(style.RED+"delete {0} ... [done]".format(delProjectName))
     
     #del server
     print("\n")
     choice_ON = raw_input(style.RED + "\nDelete server '{0}' (if it exists)? (Y/N) >> ".format(delProjectName)+style.END)
     
     while choice_ON != 'Y' and choice_ON != 'N' and choice_ON != 'y' and choice_ON != 'n':
       choice_ON = raw_input(style.PURPLE + "Your choice is invalid, try again! (Y/N) >> " + style.END)
       
     if choice_ON == 'Y' or choice_ON == 'y':
       temp = raw_input(style.RED+"You are deleting the server '{0}' (CTRL+C) to cancel, (ENTER) to continue the operation ... ".format(delProjectName)+style.END)
       print(style.RED+"seletion server '{0}' in progress ... ".format(delProjectName)+style.END)
       os.system("cd ~/Project/Server && sudo rm -r {0}".format(delProjectName))
       
     if choice_ON == 'N' or choice_ON == 'n':
       print(style.GREEN+"deletion canceled ... [done]"+ style.END)
       time.sleep(0.35)

     done()
     choiceMain()
 
   if mainPut == 'delall' or mainPut == 'DELALL': 
     choice_ON = raw_input(style.RED + "\nYou are sure you want to delete the whole project ? (Y/N) >> " + style.END)
     
     while choice_ON != 'Y' and choice_ON != 'N' and choice_ON != 'y' and choice_ON != 'n':
       choice_ON = raw_input(style.PURPLE + "Your choice is invalid, try again! (Y/N) >> " + style.END)
       
     if choice_ON == 'Y' or choice_ON == 'y':
       temp = raw_input(style.RED+"You are in the process of deleting everything (CTRL+C) to cancel, (ENTER) to continue the operation"+style.END)
       print(style.RED+"Deletion in progress ... "+ style.END)
       os.system("cd ~/Project/ && sudo rm -r *")
 
     if choice_ON == 'N' or choice_ON == 'n':
       print(style.GREEN+"deletion canceled ... [done]"+ style.END)
       time.sleep(0.35)
 
     done()
     choiceMain()
#===============main10.0
 #5
   if mainPut == '5' or mainPut == 'purge' or mainPut == 'PURGE':
      
     listProj()
     
     print(style.RED+style.BOLD+"Enter the name of the project to purge ... "+style.END)
     purge = raw_input(style.RED + style.BOLD + "\n[🅿🆄🆁🅶🅴 > " + style.END)
    
     choice_ON = raw_input(style.RED + "\nYou are sure you want to purge everything in the project {0} ? (Y/N) >> ".format(purge)+style.END)
       
     while choice_ON != 'Y' and choice_ON != 'N' and choice_ON != 'y' and choice_ON != 'n':
       choice_ON = raw_input(style.PURPLE + "Your choice is invalid, try again! (Y/N) >>     " + style.END)
         
       if choice_ON == 'Y' or choice_ON == 'y':
        print("")
    
       if choice_ON == 'N' or choice_ON == 'n':
        print(style.GREEN+"Purge canceled ... [done]"+ style.END)
        time.sleep(0.35)
    
     if choice_ON == 'y' or choice_ON == 'Y':
     
        temp = raw_input(style.RED+"You are purging the project (CTRL+C) to cancel, (ENTER) to continue the operation ... "+style.END)
        print(style.RED+"Purge '{0}' ... [loading]".format(purge))
        os.system("cd ~/Project/{0} && sudo git reset --hard && git clean -dffx && cd .. && sudo rm -rf {0}".format(purge))
        print(style.RED+"Purge '{0}' ... [done]".format(purge))
        time.sleep(0.35)

     done()
     choiceMain()
#===============main10.1
 #6
   if mainPut == '6' or mainPut == 'backup' or mainPut == 'BACKUP':
      backup()
#===============main11
 #ssh
   if mainPut == 'ssh' or mainPut == 'SSH':
    ssh()
 #tilix
   if mainPut == 'tilix' or mainPut == 'TILIX':
    tilix()
 #ungit
   if mainPut == 'ungit' or mainPut == 'UNGIT':
    ungit()
 #flow
   if mainPut == 'flow' or mainPut == 'FLOW':
    flow()

#### MAINPUT (local & remote) ####

 #mainput local (input main)
   if mainPut == 'local' or mainPut == 'LOCAL':
      print(" \n ")
     #input local (global)
      print(style.BOLD+"\nPlease enter the name of your (existing) project !"+style.END)
      zen = raw_input(style.GREEN + style.BOLD + "[🅿🆁🅾🅹🅴🅲🆃 > " + style.END)
      origin = "localhost"
      remote = "127.0.0.1"

      noteLR()
      menu()
  
   if mainPut == 'remote' or mainPut == 'REMOTE':
      print(" \n ")
      listProj()
     #valid confirm
      print(" \n ")
      temp = raw_input(style.DARKCYAN+"Have you already configured your git profile? ... do it (in the main screen) otherwise the validation of your project will not work, if you have already done it, press [ENTER] to continue, [CTRL+C] to cancel ..."+style.END)
     #input remote (global)
      print(" \n ")
      print(style.BOLD+"Please enter the name of your (existing) project !"+style.END)
      zen = raw_input(style.GREEN + style.BOLD + "[🅿🆁🅾🅹🅴🅲🆃 > " + style.END)
     #input origin/remote (global)
      print("\n    ------------- 🅾🆁🅸🅶🅸🅽 -------------")
      print("  /                                    \\")              
      print(style.BOLD+"           0 | github(https)"+style.END);
      print(style.BOLD+"           1 | github(ssh)"+style.END);
      print(style.BOLD+"           2 | bitbucket(https)"+style.END);
      print(style.BOLD+"           3 | bitbucket(ssh)"+style.END);
      print("  \                                    /")  
      print("    ----------------------------------\n")
      temp = raw_input(style.GREEN + style.BOLD + "[🅾🆁🅸🅶🅸🅽 > " + style.END)
      if temp == '0':
        origin = 'github-https'
        print(style.GREEN+"origin => {0}".format(origin)+style.END)
      if temp == '1':
        origin = 'github-ssh'
        print(style.GREEN+"origin => {0}".format(origin)+style.END)
      if temp == '2':
        origin = 'bitbucket-https'
        print(style.GREEN+"origin => {0}".format(origin)+style.END)
      if temp == '3':
        origin = 'bitbucket-ssh'
        print(style.GREEN+"origin => {0}".format(origin)+style.END)
        print(" \n ")

      #remote conf  
      print(style.PURPLE+"\nPlease enter the address (local-server | ssh-server | https-server) of the remotely accessible repository ..."+style.END)
      print(style.BOLD+"* local-server:"+style.END+" ~/Project/Server/{0}".format(zen))
      print(style.BOLD+"* ssh-server:"+style.END+" git@github.com:RajaRakoto/gitvers-tool.git OR raja@192.168.8.100:/home/raja/Project/Server/gitvers-tool")
      print(style.BOLD+"* https-server:"+style.END+" https://github.com/RajaRakoto/gitvers-tool.git")
      print(" \n ")

      #sever list
      print(style.BOLD+"[SERVER LIST (used)]--------------------------------------------------------"+style.END)
      os.system("touch ~/Project/.remote.log && cat ~/Project/.remote.log")
      print("\nNOTE: Enter 'clear' in the [SERVER> prompt to clean up the entire server list")
      print(style.BOLD+"----------------------------------------------------------------------------"+style.END)
      remote = raw_input(style.GREEN+"[🆂🅴🆁🆅🅴🆁 > "+style.END)

      #clear server list
      if remote == 'clear' or remote == 'CLEAR':
        print(" \n ")
        os.system("cd /tmp && rm -rf .remote.log")
        os.system("cd ~/Project && rm -rf .remote.log")
        print(style.GREEN+"all server list cleared ... [done]"+style.END)
        #show server list again (verification)
        print(style.BOLD+"[SERVER LIST (used)]--------------------------------------------------------"+style.END)
        os.system("touch ~/Project/.remote.log && cat ~/Project/.remote.log")
        print("\nNOTE: Enter 'clear' in the [SERVER> prompt to clean up the entire server list")
        print(style.BOLD+"----------------------------------------------------------------------------"+style.END)
        remote = raw_input(style.GREEN+"[🆂🅴🆁🆅🅴🆁 > "+style.END)

      print(" \n ")
      print(style.GREEN+"origin ID = {0}".format(origin)+style.END)
      time.sleep(1)

      #server log //test*
      #create file '.remote.log' in /tmp
      if temp == '0': #github-https
        serverLog = open(r"/tmp/.remote.log","a +")
        serverLog.write("[https]-> "+remote+"\n")
        serverLog.close()
        os.system("cat /tmp/.remote.log > ~/Project/.remote.log")
      if temp == '1': #github-ssh
        serverLog = open(r"/tmp/.remote.log","a +")
        serverLog.write("[ssh]-> "+remote+"\n")
        serverLog.close()
        os.system("cat /tmp/.remote.log > ~/Project/.remote.log")
      #import '.remote.log' to ~/Project
      if temp == '2': #bitbucket-https
        serverLog = open(r"/tmp/.remote.log","a +")
        serverLog.write("[https]-> "+remote+"\n")
        serverLog.close()
        os.system("cat /tmp/.remote.log > ~/Project/.remote.log")
      if temp == '3': #bitbucket-ssh
        serverLog = open(r"/tmp/.remote.log","a +")
        serverLog.write("[ssh]-> "+remote+"\n")
        serverLog.close()
        os.system("cat /tmp/.remote.log > ~/Project/.remote.log")
        
      print(style.GREEN+"Server update to .remote.log ... [done]"+style.END)
      time.sleep(1)
      #checking ID
      print(style.GREEN+"Checking origin ID ... [done]"+style.END)
      time.sleep(1)
      os.system("cd ~/Project/{0} && git remote add {1} {2}".format(zen,origin,remote)) #lien avec le projet
      os.system("cd ~/Project/{0} && git remote -v".format(zen)) #verification du remote
      print(style.GREEN+"Checking origin tree ... [done]".format(origin)+style.END)
      time.sleep(1)
  
      print(" \n ")
      print(style.GREEN+style.BOLD+"all REMOTE config ... [done]"+style.END)
      time.sleep(2)
      print(" \n ")

      noteLR()
      menu()

#### MAINPUT MODEL (local-model) ####

 #mainput localmod (input main)
   if mainPut == 'debug' or mainPut == 'DEBUG':
     #input localmod (global)
     zen = "local-model"
     origin = "localhost"
     remote = "127.0.0.1"

     localmodel()
     menu()

#===============main12
 #note
   if mainPut == "note" or mainPut == 'NOTE' or mainPut == "n" or mainPut == 'N':
      note()
 #notefr
   if mainPut == "notefr" or mainPut == 'NOTEFR' or mainPut == "nfr" or mainPut == 'NFR':
      noteFR()
 #note
   if mainPut == "service" or mainPut == 'SERVICE':
      service()

   if mainPut == "servicefr" or mainPut == 'SERVICEFR':
      serviceFR()
 #man
   if mainPut == 'h' or mainPut == 'H' or mainPut == "help" or mainPut == 'HELP' or mainPut == "man" or mainPut == 'MAN':
      manual()
      choiceMain()
 
 #to ignore error input main
   if mainPut == 'q' or mainPut == 'Q' or mainPut == 'quit' or mainPut == 'QUIT' or mainPut == 'exit' or mainPut == 'EXIT':
      break
#=================================MAIN-end==========================
 


exit1()