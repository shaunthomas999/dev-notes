# Github

## Use multiple accounts with Github

* Use https
* Login using token
* Set credentials helper - `git config credential.helper osxkeychain`
  * Alternative option, Git credentials manager - https://github.com/git-ecosystem/git-credential-manager
    * Download & Install - `brew install --cask git-credential-manager` 
* To cache credential for each local directory - `git config --global credential.useHttpPath true`
* Go to Intellij Github plugin config
* Login to Enterprise and Personal account using token
* Then, if local credentials are not cached, a prompt will appear to choose the account. Choose the right one!

### Reference

* https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-personal-account/managing-multiple-accounts#contributing-to-multiple-accounts-using-https-and-personal-access-tokens
  * https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-personal-account/managing-multiple-accounts
* Using SSH 
  * https://gist.github.com/rahularity/86da20fe3858e6b311de068201d279e3
  * https://www.freecodecamp.org/news/manage-multiple-github-accounts-the-ssh-way-2dadc30ccaca/

## Badges

* https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge
* https://github.com/marketplace/actions/bring-your-own-badge

## Troubleshoot

* If any issue with push/pull, run `echo url=https://<your-github-username>@github.com | git credential reject`
  * it will ask for credentails on next git activity. Provide it and then it will work

## Github CLI

* Make sure to have `read:org` in the authorised token
