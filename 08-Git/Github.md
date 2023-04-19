# Use multiple accounts with Github

* Use https
* Login using token
* Set credentials manager/helper - `git config credential.helper osxkeychain`
* To cache credential for each local directory - `git config --global credential.useHttpPath true`
* Go to Intellij Github plugin config
* Login to Enterprise and Personal account using token
* Then, if local credentials are not cached, a prompt will appear to choose the account. Choose the right one!

## Reference

* https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-personal-account/managing-multiple-accounts#contributing-to-multiple-accounts-using-https-and-personal-access-tokens
  * https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-personal-account/managing-multiple-accounts
* Using SSH 
  * https://gist.github.com/rahularity/86da20fe3858e6b311de068201d279e3
  * https://www.freecodecamp.org/news/manage-multiple-github-accounts-the-ssh-way-2dadc30ccaca/
