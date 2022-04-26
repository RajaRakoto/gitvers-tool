<div align="center">
<img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/gitvers-tool-logo.svg?raw=true" width="300">

<div align="center">
<img src="https://github.com/RajaRakoto/github-docs/blob/master/dago.gif?raw=true" width=40>
</div>

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/for-you.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com) [![forthebadge](https://github.com/RajaRakoto/github-docs/blob/master/badge/for-dago.svg?raw=true)](https://forthebadge.com) [![forthebadge](https://github.com/RajaRakoto/github-docs/blob/master/badge/build-by.svg?raw=true)](https://forthebadge.com)

![BASH](https://img.shields.io/badge/-Shell-777?style=flat&logo=shell&logoColor=ffffff&labelColor=green) ![Git](https://img.shields.io/badge/-Git-777?style=flat&logo=git&logoColor=F05032&labelColor=ffffff) ![Gitub](https://img.shields.io/badge/-Gitub-777?style=flat&logo=github&logoColor=777&labelColor=ffffff)

</div>

<br>

<table>
<tr><td align="center" colspan="2"><strong>~ INDEX ~</strong></td><tr>
<tr>
<td>

**[📌 Introduction](#-introduction)**

</td>
<td>
- About gitvers-tool<br>
- For MS Windows users
</td>
</tr>
<tr>
<td>

**[📌 Use](#-use)**

</td>
<td>
- Clone<br>
- Run<br>
- Presentation<br>
- Demo
</td>
</tr>
<tr>
<td>

**[📌 UNGIT](#-ungit)**

</td>
<td>
- Github<br>
- Description<br>
- Installation<br>
- Tuto
</td>
</tr>
</table>

<br><br>

# `📌 INTRODUCTION`

#### `⚫ About gitvers-tool`

**gitvers-tool** is a minimalist script made in `bash` to facilitate the use of `git`, thanks to this script, you save a significant amount of time because a single command from this script can replace several commands typed manually ... Note that this script is recommended for a `small project` but not ideal for a large project.

You should at least know the basics and concept of using git to use this script, otherwise don't try to use it to avoid problems. Obviously you need to have git installed on your machine to use it... Before we get to the nitty-gritty, I want to clarify that this script `generates a directory as a reference point` for all its uses, it can be located in your home `~/Projects` folder

> **WARNING**: if your project is outside `~/Projects` it will not be taken into account by the gitvers-tool script

<br>

#### `⚫ For MS Windows users`

**gitvers-tool** works with `MS Windows`, just install `gitbash` for it to work on windows -> https://github.com/git-for-windows/git/releases

> **NOTE**: Leftovers work the same as on `GNU/Linux`

<br>
<hr>
<br>

# `📌 USE`

#### `⚫ Clone`

```bash
 $ git clone --depth 1 https://github.com/RajaRakoto/gitvers-tool
```

<br>

#### `⚫ Run`

```bash
cd gitvers-tool
```

```bash
chmod +x gitvers-tool.sh
```

```bash
./gitvers-tool.sh
```

<br>

#### `⚫ Presentation`

<img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/project-lists.png?raw=true" width="300"> <br> <img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/illustration.png?raw=true" width="700"> <br><img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/status1.png?raw=true" width="700"> <br><img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/status2.png?raw=true" width="700"> <br><img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/inputArea.png?raw=true" width="700">

<br>

#### `⚫ Demo`

Here is a snippet of using gitvers-tool, you can also do other things like `pull`, `fast forward`, `merge branches`, `clone projects`, and many more. Don't hesitate to contact me if you have any questions.

<img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/gitvers-demo.gif?raw=true" width="1000">

<br>
<hr>
<br>

# `📌 UNGIT`

- **Github**: https://github.com/FredrikNoren/ungit
- **Description**: `UNGIT` is a version control tool (web application) `using git`, the combination of `gitvers-tool` and `ungit` will make a `great version control tool` for your project as `gitvers-tool` will save you much more time during `initialization of a project` and `ungit` will offer you `better overall visibility` on the progress of your projects, Personally I use both for more flexibility and speed ...
- **Installation**: You can install ungit easily with NPM

```bash
$ sudo -H npm install -g ungit
```

- **Tuto**: If you want a full tutorial from UNGIT (in FR) -> https://grafikart.fr/tutoriels/ungit-437

<img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/ungit-illustration.png?raw=true" width="700">

<br>

💠 Performing a commit, the advantage with ungit is that you can more easily select the file to commit <br> <img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/ungit-commit.png?raw=true" width="500"> <br>💠 To display the modification made to a file <br> <img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/ungit-diff.png?raw=true" width="500"> <br>💠 To change branches and merge one branch to another <br> <img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/ungit-merge.gif?raw=true" width="500"> <br>💠 To deploy a modification on the remote server (push) <br> <img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/ungit-push.gif?raw=true" width="500"> <br>💠 To quickly edit the .gitignore file <br> <img src="https://github.com/RajaRakoto/github-docs/blob/master/gitvers-tool/ungit-ignore.png?raw=true" width="500">

 <br>

**💡 However, I use `gitvers-tool` because sometimes `UNGIT` crashes at some point, so I use the latter in case that happens...**

🅴🅽🅹🅾🆈 ❗
