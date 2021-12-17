# Work with Git

1. Clone git repo with this command:
```
git clone [repo url]
eg: git clone https://github.com/AnhNguyen20695/Ecomm_App.git
```

2. Change current working directory to the cloned repo:
```
cd Ecomm_App/
```

3. The default branch is "main". Create a local branch to work and commit code without affecting the main branch:
```
git checkout -b [new branch name]
eg: git checkout -b vietanh_api
```

4. Check all branches:
```
git branch -a
```
*** Note: The highlighted branch is the branch you are working on in your local computer.

5. Push the newly created local branch to Github:
```
git push origin [new branch name]
eg: git push origin vietanh_api
```

6. Go to github website, create a new pull request. Then merge the new branch to "main".


# Switch local branched
```
git checkout [branch name]
eg: git checkout dquang_front
```
