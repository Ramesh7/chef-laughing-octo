# Chef Laughing 🐙

Chef laughing octo laughs at your code when you dont pass its checkstyle , lint and spec criteria. 
==========

We have used out of the box hooks for pre-commit for developement and are taken from [Pre-commits](https://github.com/pre-commit/pre-commit)


### How to use this in your Chef git repo ?

#### Install Dependencies
   We use `python` module to run the 3 exectutables from OS (`foodcritic`, `cookstyle`, `rspec`) you can use any one or all as you want so you can skip un wanted deps.
   Make sure you have installed 
   1. foodcritic: `gem install foodcritic` See also  http://www.foodcritic.io/
   2. cookstyle:  `gem install cookstyle` requires ` Ruby >= 2.4.` See also  https://docs.chef.io/cookstyle.html
   3. rspec:      `gem install rspec` See also  http://www.foodcritic.io/
   4. pre-commit:  `pip install pre-commit` this is needed so that our pre-commits work.
   
#### Usage
1. Create a file `.pre-commit-config.yaml` in your root folder of repo (where you have .git) 
2. Add this to your `.pre-commit-config.yaml`

``` yaml
 repos:
-  repo: https://github.com/grizzly-monkey/chef-laughing-octo.git
    sha: ''   # Use the sha you want to point at release tag or a commit
    hooks:
     - id: check-foodcritic   # if you want to run foodcritic for cookbooks in repo
     - id: check-rspec      # if you want to run rspec for recipies in the repo
     - id: check-cookstyle  # if you want to run cookstyle for cookbooks in repo
 ```


#### Hooks are available in chef-pre-commit-hooks folder

- `check-rspec`
- `check-foodcritic`
- `check-cookstyle` 
