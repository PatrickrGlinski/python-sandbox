## Skeleton Project

This Skeleton directory contains all of the basics that is needed to get a new python project up and running. When creating a new project, copy this directory to a new name and edit the files to get started.

The Following is needed for a new project:
-  Proper project layout
-  Automated Tests
-  Modules 
-  Install Scripts


## Virtual Environment Setup

**Install VirtualEnv**
```
    $ pip3 install virtualenv
```
 **Create .venvs in HOME dir to store all environments**

 ```
 $ mkdir ~/.venvs
 ```
 
 **Run virtualenv**
 ```
 $ virtualenv --system-site-packages ~/.venvs/project
 ```

 **Activate Virtual Environment**
 ```
$ . ~/.venvs/project/bin/activate
 ```


### Project Directory Setup
```
mkdir projects
cd projects/
mkdir skeleton-project
cd skeleton-project/
mkdir bin NAME tests docs
```

- /skeleton-project : root
- NAME: will be renamed to whatever we call the main module when creating a new project.

**Create init files**
```
touch NAME/__init__.py
touch tests/__init__.py
```

