add, checkout, clone, commit, config, gitignore, log, init, merge, gitk, status,push, pull, remote, stash

# git commands
## 1. add
- The git add command adds a change in the working directory to the staging area.
- It tells Git that you want to include updates to a particular file in the next commit. However, git add doesn't really affect the repository in any significant way—changes are not actually recorded until you run git commit .

        git add <File name>  

## 2. checkout
- The git checkout command is used to switch between branches in a repository.

        git branch  
        git checkout <branchnam

## 3. clone
- n Git, cloning is the act of making a copy of any target repository.
- The target repository can be remote or local. You can clone your repository from the remote repository to create a local copy on your system

        $ git clone <repository URL>  

## 4. commit
- It is used to record the changes in the repository. It is the next command after the git add. Every commit contains the index data and the commit message.

        git commit  

## 5. config
- The git config command is a convenience function that is used to set Git configuration values on a global or local project level. 

        git config

## 6. gitignore
- In Git, the term "ignore" is used to specify intentionally untracked files that Git should ignore. It doesn't affect the Files that already tracked by Git.
- Sometimes you don't want to send the files to Git service like GitHub. We can specify files in Git to ignore

        .gitignore

## 7. log
- The git log command is used to view the history of committed changes within a Git repository.
- Each set of changes made by a developer is recorded as a commit in Git.
- The git log command shows a default output for quickly reviewing the commit history.

        git log  

## 8. init
- The git init command creates a new Git repository. It can be used to convert an existing, unversioned project to a Git repository or initialize a new, empty repository.
- Most other Git commands are not available outside of an initialized repository, so this is usually the first command you'll run in a new project.

        git init  

## 9. merge
- To merge branches locally, use git checkout to switch to the branch you want to merge into. This branch is typically the main branch.
- Next, use git merge and specify the name of the other branch to bring into this branch.

        git merge <query>  

## 10. gitk
- Gitk is invoked similarly to git log. Executing the gitk command will launch the Gitk UI
- The upper left pane displays the commits to the repository, with the latest on top. The lower right displays the list of files impacted by the selected commit.

        gitk

## 11. status
- The git status command is used to display the state of the repository and staging area.
- It allows us to see the tracked, untracked files and changes. This command will not show any commit records or information

        git status  

## 12. push
- The git push command is used to upload local repository content to a remote repository

        git push <option> 

## 13. pull
- The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content.

        git pull <remote>

## 14. remote
- List the remote connections you have to other repositories.
        
        git remote
## 15. stash
- locally stores all the most recent changes in a workspace and resets the state of the workspace to the prior commit state. A user can retrieve all files put into the stash with the git stash pop
- The git stash command enables you to switch branches without committing the current branch.
- the stash's meaning is "store something safely in a hidden place." 

        git stash  
