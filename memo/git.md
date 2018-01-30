### Git push without password

First, generate the SSH key from your local computer and add it key to your GitHub account ([see details](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)). Essentially, copy the content of `~/.ssh/id_rsa.pub` and paste it to the Github account (`Settings`>`SSH and GPG keys`>`Add SSH key`> Paste into `Key` field.

Then go to your local repo, and set the remote url with 

```bash
git remote set-url origin git@github.com:[user_name]/[repo_name].git
```

Reference: [stackoverflow](https://stackoverflow.com/questions/6565357/git-push-requires-username-and-password)


