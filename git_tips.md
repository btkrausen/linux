# Git Commands and Tips

## Initializing a Repository
- `git init`: Initialize a new Git repository in the current directory.

## Cloning a Repository
- `git clone <repository_url>`: Clone a remote repository to your local machine.

## Checking Status
- `git status`: Check the status of your repository, including modified, staged, and untracked files.

## Adding Changes
- `git add <filename>`: Add specific files to the staging area.
- `git add .`: Add all modified files to the staging area.

## Committing Changes
- `git commit -m "Commit message"`: Commit staged changes with a descriptive message.

## Viewing Commit History
- `git log`: View the commit history of the repository.

## Creating Branches
- `git branch <branch_name>`: Create a new branch.
- `git checkout <branch_name>`: Switch to a different branch.
- `git checkout -b <branch_name>`: Create and switch to a new branch in one step.

## Merging Branches
- `git merge <branch_name>`: Merge changes from a specified branch into the current branch.

## Resolving Conflicts
- During a merge or rebase operation, Git may encounter conflicts that need to be resolved manually.
- Use a text editor to resolve conflicts in the affected files.
- After resolving conflicts, stage the changes using `git add` and commit them.

## Pushing Changes
- `git push <remote_name> <branch_name>`: Push local commits to a remote repository.
- `git push -u <remote_name> <branch_name>`: Set the upstream branch and push changes.

## Pulling Changes
- `git pull <remote_name> <branch_name>`: Fetch changes from a remote repository and merge them into the current branch.

## Viewing Differences
- `git diff`: View the differences between the working directory and the staging area.
- `git diff <commit_id>`: View the differences between the current commit and a specific commit.

## Removing Files
- `git rm <filename>`: Remove a file from both the working directory and the staging area.
- `git rm --cached <filename>`: Remove a file from the staging area but keep it in the working directory.

## Ignoring Files
- Create a file named `.gitignore` in the root directory of your repository.
- Add filenames or patterns of files to be ignored, one per line, in the `.gitignore` file.

## Viewing Branches
- `git branch`: List all branches in the repository.
- `git branch -a`: List all branches, including remote branches.

## Deleting Branches
- `git branch -d <branch_name>`: Delete a local branch.
- `git push <remote_name> --delete <branch_name>`: Delete a remote branch.

## Renaming and Moving Files
- Use the `git mv` command to rename or move files while automatically staging the changes.

## Undoing Changes
- `git checkout -- <filename>`: Discard changes to a specific file in the working directory.
- `git reset HEAD <filename>`: Unstage changes for a specific file.
- `git reset HEAD~`: Undo the last commit and move changes back to the staging area.

## Stashing Changes
- `git stash`: Temporarily stash changes in the working directory.
- `git stash list`: List all stashes.
- `git stash apply`: Apply the most recent stash to the working directory.
- `git stash pop`: Apply and remove the most recent stash from the stash list.

## Tagging Releases
- `git tag <tag_name>`: Create a lightweight tag at the current commit.
- `git tag -a <tag_name> -m "Tag message"`: Create an annotated tag with a message.

## Fetching Remote Changes
- `git fetch`: Fetch changes from a remote repository without merging them into the local branch.
- `git fetch --prune`: Fetch changes and remove any remote branches that have been deleted.

## Rebasing Commits
- `git rebase <branch_name>`: Move the current branch onto <branch_name>, replaying local commits on top of it.
- `git rebase -i <commit_id>`: Interactively rebase commits starting from the specified commit.

## GitHub Integration
- GitHub provides a graphical interface for managing repositories, issues, pull requests, and more.
- Use GitHub Actions for continuous integration and deployment workflows.
- Collaborate with team members by forking repositories, opening pull requests, and reviewing code changes.

## Documentation and Help
- `git help <command>`: Display help for a specific Git command.
- `git --version`: Display the installed version of Git.
- Git documentation is available online at https://git-scm.com/doc.

## Tips
- Commit early and often to track changes incrementally and maintain a detailed history.
- Write descriptive commit messages that explain the purpose of each change.
- Use branches to work on new features or bug fixes independently without affecting the main codebase.
- Review changes before committing or pushing them to ensure code quality and avoid mistakes.
- Regularly fetch and pull changes from remote repositories to stay up to date with the latest changes.
- Practice good version control hygiene by keeping your repository clean and organized.
