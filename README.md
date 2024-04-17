Overview
========
My personal scripts folder; mostly for backup and quick deployment

Checkout `mark` for bookmarking directories in the CLI to avoid typing long paths.

Scripts
=======

# mark #

```
mark [-d] mark_name [mark_destination]
mark -l

Set a symlink bookmark at $HOME/.mk/mark_name that directs to the current directory or mark_destination.

DESCRIPTION
    Bookmarks are stored as symlinks (shortcuts) in $HOME/.mk, and can be accessed like usual:
        mv ~/.mk/mark_name1/somefile ~/path/to/destination
        cd -P ~/.mk/mark_name

    Use -P flag when cd into symlink to resolve dot-dot. Otherwise, your pwd will look like
    ~/.mk/mark_name instead of ~/some/directory/mark_name, and when you try to go back with
    cd .. you will end up in the bookmark directory. You can set an alias in bashrc for
    convenience
        alias cd="cd -P"

    Bookmarks are stored as symlinks, so moving, deleting, etc. will only apply to the bookmark.

OPTIONS
    -d
        Delete bookmark with mark_name instead of normal functionality
    -l
        List all bookmarks available

CONFIGURATIONS
    bashrc:
        export MK="$HOME/.mk"  # avoid typing out ~/.mk
        alias cd="cd -P"    # Automatically resolves symlinks with cd

    You can also bookmark the ~/.mk folder in most GUI file explorers for easy access with GUI
    as well. On Ubuntu, this is done by dragging the folder onto the sidebar.
`mark [-d] mark_name [mark_destination]`

Set a symlink bookmark at `$HOME/.mk/mark_name` that directs to the current directory or
`mark_destination`.
```

# cmakeinit #
```
Synopsis: cmakeinit

Description:
    Sets up a working environment with CMake and git in the current directory

    Initialize CMakeLists.txt with my default settings:
        cmake_minimum_required: 3.22
        project name: working directory name
        CMAKE_EXECUTABLE_SUFFIX .out
        CMAKE_CXX_STANDARD 17
        CMAKE_CXX_STANDARD_REQUIRED True
        CMAKE_EXPORT_COMPILE_COMMANDS ON
```

# csif #
```
Synopsis: csif OPTIONS...

Description:
    SSH into my school computers and mount the remote drive at ~/remote
    
    -t
        SFTP instead of SSH, does not mount remote.

    -s
        Only check the remote status

    -n
        SSH without mounting drive
```

# ezcommit #
```
Synopsis: ezcommit STRING

Description:
    git add -A
    git commit -m STRING
```

# ezmerge #
```
Synopsis: ezmerge

Description:
    Push the current branch, merge to remote, update local main,
    and then delete the current branch.
```

# firstpush #
```
Synopsis: firstpush

Description:
    git push --set-upstream origin current_branch
```

# hwtest #

```
Synopsis: hwtest test_case_num

Description:
    run build/main with input/#.txt, check against expected/#.txt
```

# lcovgen #
```
Synopsis: lcovgen

Description:
    Generate captured code coverage report
```

# lcovinit #
```
Synopsis: lcovinit

Descrption:
    Begin capturing code coverage in ./build/
```

# newsh #
```
Synopsis: newsh FILENAME

Description:
    Set up a new shellscript named FILENAME, initialized with basic
    argument validation and execution permission
```

# regex #
```
Synopsis: regex REGEX_EXPRESSION STRING

Description:
    Checks if the expression matches the string.
```

# run #
```
Synopsis: `run [-x language] [-g] <FILE>`

Description:
    Quickly run FILE.

    When running assembly, automatically starts gdb

    -x language
        Compile with specified language. If no language is specified,
        use the file extension to determine the language.
        Supported: cxx, asm, rust

    -g
        For cxx: instead of running normally, run in gdb.
```

# sshmount #
```
Synopsis: sshmount HOST [SSH_OPTIONS]

Description:
    Opens an SSH connection with HOST and mount the remote home folder on
    ~/remote/HOST/

Author:
    https://github.com/wd5gnr
```

# testscript #
```
Synopsis: testscript

Description:
    Prints "the scripts folder is linked!"; used for checking if scripts
    are added to PATH
```

# jupytervenv
```
Synopsis: jupytervenv

Description:
    Set up jupyter kernel in virtual environment located at ./venv and
    start jupyter lab
```

# gitundo
```
Synopsis: gitundo

Description:
    Undoes the last commit and keeps the changes
```
