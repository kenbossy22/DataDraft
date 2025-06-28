# DataDraft Development Workspace

This repository contains early development work for the DataDraft AI Agent. The project is moving to a new GitHub repository so you can connect to it with Visual Studio Code. Follow the steps below to create the GitHub repo and push this code to it.

## 1. Create a new GitHub repository

1. Log in to [github.com](https://github.com) and click **New repository**.
2. Choose a repository name (for example `DataDraft`) and keep it **public** or **private** depending on your preference.
3. Do **not** initialize the repo with a README or `.gitignore` since this directory already contains a Git history.
4. Click **Create repository** and copy the remote URL shown (e.g. `https://github.com/yourusername/DataDraft.git`).

## 2. Add the GitHub remote and push

From your local terminal, run the following commands in this project folder:

```bash
# Set the new GitHub repo as the remote named "origin"
 git remote add origin <remote-url>
# Push the current history to GitHub
 git push -u origin main  # or "git push -u origin work" if your branch is called work
```

Replace `<remote-url>` with the URL you copied from GitHub. The `-u` flag sets `origin` as the default remote for future pushes.

## 3. Open the repository in VS Code

1. Install [Visual Studio Code](https://code.visualstudio.com/) and the [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) extension (optional).
2. In VS Code, press **F1** (or `Ctrl+Shift+P`) and run **Git: Clone**. Paste the same GitHub repository URL and choose a local folder to clone into.
3. After cloning, VS Code will ask if you want to open the cloned folder. Choose **Open** to start working.
4. Use the built-in **Source Control** sidebar to commit and push changes. You can also run Git commands directly from the integrated terminal.

## 4. Next steps

Once the code is pushed to GitHub, you can continue development in VS Code, create pull requests, and manage issues. This README will remain as a quick reference for setting up the workspace.

