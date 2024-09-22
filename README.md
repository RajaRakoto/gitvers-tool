# gitvers-tool 🟠

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/for-you.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com) [![forthebadge](https://rajarakoto.github.io/github-docs/badge/build-by.svg)](https://forthebadge.com)

![Git](https://img.shields.io/badge/-Git-777?style=flat&logo=git&logoColor=F05032&labelColor=ffffff) ![Gitub](https://img.shields.io/badge/-Gitub-777?style=flat&logo=github&logoColor=777&labelColor=ffffff)

**gitvers-tool** is a script designed for efficient `git` usage, saving time with single commands replacing multiple manual inputs, ideal for small projects. Prior understanding of git basics is essential to avoid issues. Git installation is necessary. A directory is generated for reference, usually in `~/Projects`, with files located outside this directory not being recognized by gitvers-tool.

---

### 📌 Usage

Run the following command to install gitvers-tool (Linux only):

```bash
curl https://raw.githubusercontent.com/RajaRakoto/gitvers-tool/master/setup > setup && chmod +x setup && ./setup
```

Uninstall gitvers-tool (Linux only):

```bash
sudo rm -r /usr/local/bin/gitvers-tool
```

---

### 📌 Guide

<img src="https://rajarakoto.github.io/github-docs/gitvers-tool/project-lists.png" width="300"> <br> <img src="https://rajarakoto.github.io/github-docs/gitvers-tool/illustration.png" width="700"> <br><img src="https://rajarakoto.github.io/github-docs/gitvers-tool/status1.png" width="700"> <br><img src="https://rajarakoto.github.io/github-docs/gitvers-tool/status2.png" width="700"> <br><img src="https://rajarakoto.github.io/github-docs/gitvers-tool/inputArea.png" width="700">

---

### 📌 Demo

Here is a snippet of using gitvers-tool, you can also do other things like `pull`, `fast forward`, `merge branches`, `clone projects`, and many more ...

<img src="https://rajarakoto.github.io/github-docs/gitvers-tool/gitvers-demo.gif" width="1000">

---

### 📌 Ungit

[Ungit](https://github.com/FredrikNoren/ungit) and `gitvers-tool` together create a powerful version control tool for managing `git` repositories with ease. `gitvers-tool` speeds up project initialization, while `ungit` provides enhanced project visibility. Combining both offers flexibility and efficiency in managing projects.

```bash
$ sudo -H npm install -g ungit
```

<img src="https://rajarakoto.github.io/github-docs/gitvers-tool/ungit-illustration.png" width="700">

<br>

**Performing a commit, the advantage with ungit is that you can more easily select the file to commit** <br> <img src="https://rajarakoto.github.io/github-docs/gitvers-tool/ungit-commit.png" width="500"> <br>**To display the modification made to a file** <br> <img src="https://rajarakoto.github.io/github-docs/gitvers-tool/ungit-diff.png" width="500"> <br>**To change branches and merge one branch to another** <br> <img src="https://rajarakoto.github.io/github-docs/gitvers-tool/ungit-merge.gif" width="500"> <br>**To deploy a modification on the remote server (push)** <br> <img src="https://rajarakoto.github.io/github-docs/gitvers-tool/ungit-push.gif" width="500"> <br>**To quickly edit the .gitignore file** <br> <img src="https://rajarakoto.github.io/github-docs/gitvers-tool/ungit-ignore.png" width="500">
